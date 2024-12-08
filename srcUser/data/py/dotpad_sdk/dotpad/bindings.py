import ctypes
from ctypes import c_int, c_char_p, c_wchar_p, c_uint8, POINTER, CFUNCTYPE, c_bool

# DLL 로드
try:
    dotpad_sdk = ctypes.WinDLL("DotPadSDK.dll")
except OSError:
    raise ImportError("Could not load DotPadSDK.dll. Ensure the DLL is available.")

# DOT_PAD_SDK_ERROR 정의
DOT_PAD_SDK_ERROR = c_int

# 함수 시그니처 정의
dotpad_sdk.DOT_PAD_INIT.argtypes = [c_int]
dotpad_sdk.DOT_PAD_INIT.restype = DOT_PAD_SDK_ERROR

dotpad_sdk.DOT_PAD_DEINIT.argtypes = []
dotpad_sdk.DOT_PAD_DEINIT.restype = DOT_PAD_SDK_ERROR

dotpad_sdk.DOT_PAD_DISPLAY.argtypes = [c_char_p]
dotpad_sdk.DOT_PAD_DISPLAY.restype = DOT_PAD_SDK_ERROR

dotpad_sdk.DOT_PAD_DISPLAY_DATA.argtypes = [POINTER(c_uint8), c_int, c_bool]
dotpad_sdk.DOT_PAD_DISPLAY_DATA.restype = DOT_PAD_SDK_ERROR

# Python 클래스
class DotPad:
    def __init__(self, port_number: int, device_type: int = None):
        if device_type is None:
            self.error_code = dotpad_sdk.DOT_PAD_INIT(port_number)
        else:
            self.error_code = dotpad_sdk.DOT_PAD_INIT_WITH_DEVICE_TYPE(port_number, device_type)

    def deinit(self):
        return dotpad_sdk.DOT_PAD_DEINIT()

    def display_file(self, file_path: str):
        return dotpad_sdk.DOT_PAD_DISPLAY(file_path.encode('utf-8'))

    def display_data(self, data: bytes, refresh: bool = False):
        data_array = (c_uint8 * len(data))(*data)
        return dotpad_sdk.DOT_PAD_DISPLAY_DATA(data_array, len(data), refresh)
