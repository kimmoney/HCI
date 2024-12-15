import re
from bleak import BleakClient, BleakScanner

class DotPadSDK:
    device_map = {}

    def __init__(self):
        self.DOTPAD_PREFIX = "iPad"
        # self.DOTPAD_PREFIX = "DotPad320"
        self.DOTPAD_SERVICE = "49535343-fe7d-4ae5-8fa9-9fafd205e455"
        self.DOTPAD_CHARACTERISTIC = "49535343-1e4d-4bd9-ba61-23c647249616"

    async def request(self):
        print("Scanning for devices...")
        devices = await BleakScanner.discover()
        for device in devices:
            if device.name and self.DOTPAD_PREFIX in device.name:
                print(f"Found device: {device.name}")
                return device
        raise Exception("No matching Bluetooth devices found.")

    async def connect(self, device):
        if not device:
            raise ValueError("No Bluetooth device selected")

        client = BleakClient(device)
        try:
            await client.connect()
            print(f"Connected to {device.name}")
            self.device_map[device.name] = {
                "client": client,
                "characteristic": self.DOTPAD_CHARACTERISTIC,
            }
            return True
        except Exception as e:
            print(f"Failed to connect: {e}")
            return False

    async def disconnect(self, device_name):
        if device_name in self.device_map:
            client = self.device_map[device_name]["client"]
            await client.disconnect()
            del self.device_map[device_name]
            print(f"Disconnected from {device_name}")
        else:
            print(f"Device {device_name} is not connected.")

    async def display_graphic_data(self, device_name, data):
        if device_name not in self.device_map:
            raise Exception("Device is not connected.")
        
        client = self.device_map[device_name]["client"]
        characteristic = self.device_map[device_name]["characteristic"]
        data_bytes = DotPadData.get_request_data(data, False)
        for chunk in data_bytes:
            await client.write_gatt_char(characteristic, bytearray.fromhex(chunk))
        print("Graphic data sent successfully.")

    async def reset_graphic_data(self, device_name):
        reset_data = DotPadData.get_reset_data(300)
        await self.display_graphic_data(device_name, reset_data)


    async def display_pixel_data(self, device_name, data, row, index, graphic_mode = False):
        if graphic_mode:
            row+=1
        if device_name not in self.device_map:
            raise Exception("Device is not connected.")
        
        client = self.device_map[device_name]["client"]
        characteristic = self.device_map[device_name]["characteristic"]
        data_bytes = DotPadData.get_request_line_data(row, index, data, False)
        await client.write_gatt_char(characteristic, bytearray.fromhex(data_bytes))
        print("Pixel data sent successfully.")




    async def add_listener_key_event(self, device_name, callback):
        if device_name not in self.device_map:
            raise Exception("Device is not connected.")
        
        client = self.device_map[device_name]["client"]
        characteristic = self.device_map[device_name]["characteristic"]

        async def notification_handler(sender, data):
            """Handle notifications asynchronously."""
            hex_data = "".join(f"{byte:02x}" for byte in data)
            notify_module = DotPadNotifyModule(hex_data, characteristic)

            # 비동기 콜백 호출
            await notify_module.set_panning_key_event(callback)
            await notify_module.set_function_key_event(callback)

        await client.start_notify(characteristic, notification_handler)
        print("Key event listener added successfully.")


class DotPadNotifyModule:
    PANNING_KEY = "aa55000900031200"
    FUNCTION_KEY = "aa55000900033200"

    def __init__(self, hex_packet, characteristic):
        self.characteristic = characteristic
        self.receive_hex_packet = hex_packet

    async def set_panning_key_event(self, callback):
        if self.receive_hex_packet.startswith(self.PANNING_KEY):
            key_code = int(self.receive_hex_packet[18:20], 16)
            if key_code == 4:
                await callback("LP")
            elif key_code == 2:
                await callback("RP")

    async def set_function_key_event(self, callback):
        if self.receive_hex_packet.startswith(self.FUNCTION_KEY):
            function_key = int(self.receive_hex_packet[15:17], 16)
            await callback(str(function_key))


class DotPadSendModule:
    send_map_data = {}
    send_word_wrap_list = []
    word_wrap_page_no = -1

    @staticmethod
    def set_braille_word_wrap_list(wrapped_data):
        DotPadSendModule.send_word_wrap_list = [
            DotPadData.get_request_line_data(0, 0, data, True)
            for data in wrapped_data
        ]
        DotPadSendModule.word_wrap_page_no = -1

    @staticmethod
    async def send_braille_word_wrap(characteristic, page_no):
        DotPadSendModule.word_wrap_page_no = page_no
        data = DotPadSendModule.send_word_wrap_list[page_no - 1]
        await characteristic.write_value(bytearray.fromhex(data))

    @staticmethod
    def set_send_data(line_id, data, is_ack):
        DotPadSendModule.send_map_data[line_id] = {
            "command_data": data,
            "is_ack": is_ack,
        }

class DotPadData:
    @staticmethod
    def get_reset_data(size):
        return "00" * size

    @staticmethod
    def get_request_data(data, is_text_mode):
        data_bytes = DotDataUtil.hex_to_bytes(data)
        chunked_data = DotPadData._get_request_data_chunk_list(data_bytes, 30)
        return DotPadData._get_command_chunk_list(chunked_data, is_text_mode)

    @staticmethod
    def get_request_line_data(line, start, data, is_text_mode):
        data_bytes = DotDataUtil.hex_to_bytes(data)
        return DotPadData._get_command_chunk_line(line, start, data_bytes, is_text_mode)

    @staticmethod
    def _get_request_data_chunk_list(data, chunk_size):
        return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    @staticmethod
    def _get_command_chunk_list(chunks, is_text_mode):
        return [
            DotPadData._get_command_chunk_line(index + 1, 0, chunk, is_text_mode)
            for index, chunk in enumerate(chunks)
        ]

    @staticmethod
    def _get_command_chunk_line(line, start, data, is_text_mode):
        protocol = DotPadProtocol
        payload = (
            protocol.get_sync() +
            protocol.get_length(len(data) + 6) +
            protocol.get_dest_id(line) +
            protocol.get_command_type() +
            protocol.get_display_mode(is_text_mode) +
            protocol.get_start_cell(start) +
            protocol.get_data_body(data) +
            protocol.get_checksum(
                protocol.get_dest_id(line),
                protocol.get_command_type(),
                protocol.get_display_mode(is_text_mode),
                protocol.get_start_cell(start),
                protocol.get_data_body(data)
            )
        )
        return "".join(payload)

class DotPadProtocol:
    @staticmethod
    def get_sync():
        return ["AA", "55"]

    @staticmethod
    def get_length(data_length):
        return ["00", DotDataUtil.decimal_to_hex(data_length)]

    @staticmethod
    def get_dest_id(dest_id):
        return [DotDataUtil.decimal_to_hex(dest_id)]

    @staticmethod
    def get_command_type():
        return ["02", "00"]

    @staticmethod
    def get_display_mode(is_text_mode):
        return ["80"] if is_text_mode else ["00"]

    @staticmethod
    def get_start_cell(start_cell):
        return [DotDataUtil.decimal_to_hex(start_cell)]

    @staticmethod
    def get_data_body(data):
        return DotDataUtil.bytes_to_hex_list(data)

    @staticmethod
    def get_checksum(*args):
        checksum = 165
        for arg in args:
            for value in arg:
                checksum ^= int(value, 16)
        return [DotDataUtil.decimal_to_hex(checksum)]

class DotDataUtil:
    @staticmethod
    def hex_to_bytes(hex_string):
        if len(hex_string) % 2 != 0:
            raise ValueError("Hex string must have an even number of digits")
        return bytearray.fromhex(hex_string)

    @staticmethod
    def decimal_to_hex(decimal):
        return f"{decimal:02x}"

    @staticmethod
    def bytes_to_hex_list(byte_data):
        return [f"{byte:02x}" for byte in byte_data]

class BrailleWordWrap:
    DOUBLE_ZERO = "00"

    def __init__(self, cell_size, braille_hex_data):
        self.cell_size_hex = cell_size * 2
        self.braille_hex_data = braille_hex_data

    def to_wrapped_hex(self):
        hex_segments = self._process_hex_data()
        return self._generate_wrapped_hex_list(hex_segments)

    def _process_hex_data(self):
        data_segments = self.braille_hex_data.split(self.DOUBLE_ZERO)
        return [segment.strip() + self.DOUBLE_ZERO for segment in data_segments]

    def _generate_wrapped_hex_list(self, segments):
        wrapped_list = []
        current_segment = []

        for segment in segments:
            if len("".join(current_segment)) + len(segment) > self.cell_size_hex:
                wrapped_list.append(self._pad_segment("".join(current_segment)))
                current_segment = []
            current_segment.append(segment)

        if current_segment:
            wrapped_list.append(self._pad_segment("".join(current_segment)))

        return wrapped_list

    def _pad_segment(self, segment):
        while len(segment) < self.cell_size_hex:
            segment += "0"
        return segment
