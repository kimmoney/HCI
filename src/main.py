from data.py.libs import *
from data.ui.main import Ui_MainWindow
import numpy as np
from PySide6.QtCore import QSize
import data.py.test_sound as test_sound
import sys
import asyncio
from PySide6.QtWidgets import QApplication, QMainWindow,QLineEdit, QPushButton, QVBoxLayout, QWidget
from qasync import QEventLoop
from SDK import DotPadSDK




import sys
import asyncio
# from PyQt5.QtWidgets import QApplication, QMainWindow,QLineEdit, QPushButton, QVBoxLayout, QWidget
from qasync import QEventLoop
from SDK import DotPadSDK

CELL300_GRAPHIC_FULL = "4f09090909090909090100000000000000804000000020042024242424a4c4c040000080c0408040804080408040000000000000000000000000003807000000000000000000000000000080c0e044000000100210121212123226a4c4c0c0602404200420042004a04400000000000000000000000000180300000000000000000000000080c0e06434060000000881c8490909091913322624241412021002100210023006000000000000000000000000000801000000000000000000000080e06434161a03000000002024844000000809191312120a090108010801080118030000804000000000000000000000000000000080c0c0c0c0c0c0e074161a0b098140000000101222844000000008090909010000000000000000080100002004000000000000000000000000000080e064242424a4e4741e0b0981c060040000000809112284400000000000000000000000000000000000000010824000000000000000000000000080e07416121212b2f6de4b8140a064140200000000000811a2c440000000000000000000000000000000000000082184400000000000000000000000a0741e0b090909b97fafc5e04430160a010000000000000831a6440000000000000000000000000000000000000010a2c44000000000000000000000b05e0b01000000b8dff3663406180b01000000000000000018b3c6400000000000000000000000000000000000000831a64400000000000000000000b84f0100000000382f3d975a0308010000000000000000000839a7440000000000000000000000000000000000000018338640000000000000"


class DotPadApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sdk = DotPadSDK()  # DotPad SDK 초기화
        self.device = None

        self.setWindowTitle("DotPad Controller")
        self.setGeometry(100, 100, 300, 200)

        # 버튼 추가
        self.canvas = PaintWidget()
        self.canvas.show()
        self.initUI()

    def initUI(self):
        self.button_connect = QPushButton("Connect to DotPad")
        self.button_display = QPushButton("Display Graphic Data")
        self.button_reset = QPushButton("Reset Graphic Data")
        self.input = QLineEdit()

        self.button_connect.clicked.connect(self.connect_device)
        self.button_display.clicked.connect(self.display_graphic)
        self.button_reset.clicked.connect(self.canvas.reset_canvas)
        self.button_reset.clicked.connect(self.reset_graphic)

        

        layout = QVBoxLayout()
        layout.addWidget(self.button_connect)
        layout.addWidget(self.button_display)
        layout.addWidget(self.input)
        layout.addWidget(self.button_reset)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def showEvent(self, Event):
        # self.connect_device()
        return super().showEvent(Event)


    async def async_connect_device(self):
        print("Searching for DotPad devices...")
        try:
            self.device = await self.sdk.request()
            print(f"Device found: {self.device.name}")
            connected = await self.sdk.connect(self.device)
            if connected:
                print(f"Connected to {self.device.name}")

                # 키 이벤트 리스너 시작
                await self.add_key_event_listener()
            else:
                print("Failed to connect.")
        except Exception as e:
            print(f"Error during connection: {e}")

    def connect_device(self):
        """버튼 클릭 이벤트에서 비동기 작업 실행"""
        asyncio.create_task(self.async_connect_device())

    async def async_display_graphic(self):
        if self.device:
            print("Displaying graphic data...")
            await self.sdk.display_graphic_data(self.device.name, self.input.text())

    def display_graphic(self):
        """버튼 클릭 이벤트에서 비동기 작업 실행"""
        asyncio.create_task(self.async_display_graphic())

    async def async_reset_graphic(self):
        if self.device:
            print("Resetting graphic data...")
            await self.sdk.reset_graphic_data(self.device.name)

    def reset_graphic(self):
        """버튼 클릭 이벤트에서 비동기 작업 실행"""
        asyncio.create_task(self.async_reset_graphic())

    async def add_key_event_listener(self):
        """키 이벤트 리스너 추가"""
        async def key_event_callback(event_code):
            print(f"Key event received: {event_code}")
            if event_code == "4":
                print("hello")
                await self.sdk.display_graphic_data(self.device.name, CELL300_GRAPHIC_FULL)
            elif event_code == "8":
                print("world")
                await self.sdk.reset_graphic_data(self.device.name)
            elif event_code == "2":
                for i in range(10):
                    await self.sdk.display_pixel_data(self.device.name, "ffffff0000000000000000000000000000000000000000", i+5, 18)
            elif event_code == "1":  
                for i in range(10):
                    await self.sdk.display_pixel_data(self.device.name, "000000", i+5, 5)

        try:
            await self.sdk.add_listener_key_event(self.device.name, key_event_callback)
            print("Key event listener added. Waiting for events...")
        except Exception as e:
            print(f"Error during adding key event listener: {e}")
    

window_map = np.array([[0]*60]*40)
result_map = np.array([[0]*60]*40)
activity_map = np.array([[0]*60]*40)


class PaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Paint Program with List Output")
        self.setGeometry(100, 100, 1200, 800)

        # 그림을 저장할 변수
        self.pixmap = QPixmap(600, 400)  # QPixmap으로 초기화
        self.pixmap.fill(Qt.white)  # 배경을 흰색으로 채움

        # 그릴 때 사용할 펜 설정
        self.drawing = False
        self.last_point = QPoint()

        # 마우스 좌표 저장할 리스트
        self.points_list = []
        self.sound_feedback = test_sound.SoundThread()
        self.sound_feedback.start()
    def reset_canvas(self):
        global window_map,result_map,activity_map
        window_map = np.array([[0]*60]*40)
        result_map = np.array([[0]*60]*40)
        activity_map = np.array([[0]*60]*40)
        self.pixmap.fill(Qt.white)
        self.update()

    def mousePressEvent(self, event):
        # 마우스를 누르면 그림을 시작
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        # 마우스를 움직일 때 그림 그리기
        if event.buttons() & Qt.LeftButton and self.drawing:
            painter = QPainter(self.pixmap)  # QPixmap에서 QPainter 사용
            pen = QPen(Qt.black, 5, Qt.SolidLine)  # 펜 설정 (색상, 두께)
            painter.setPen(pen)
            
            x = max(0,min(59, event.pos().x()/self.size().width()*60))
            y = max(0,min(39, event.pos().y()/self.size().height()*40))
            if window_map[int(y)][int(x)] != 1:
                painter.drawLine(self.last_point, event.pos())  # 선을 그림
                self.last_point = event.pos()
                self.sound_feedback.update_values(400 - self.last_point.y(), self.last_point.x() / 600, True)
                self.update()  # 화면 갱신
                window_map[int(y)][int(x)] = 1
                # print(window_map)
                print(x,y)
                braille_hex_values=binary_to_braille_unicode(window_map)
                # print("".join(braille_hex_values))
                asyncio.create_task(mainWindow.sdk.display_graphic_data(mainWindow.device.name, "".join(braille_hex_values)))
                # # print(braille_hex_values)
                # for row in braille_hex_values:
                #     print("".join(row),end="")


    def mouseReleaseEvent(self, event):
        # 마우스를 놓으면 그림을 종료
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.sound_feedback.update_values(400 - self.last_point.y(), self.last_point.x() / 600, False)

    def paintEvent(self, event):
        # QPixmap을 화면에 그림
        canvas_painter = QPainter(self)
        canvas_painter.drawPixmap(self.rect(), self.pixmap, self.pixmap.rect())

    def resizeEvent(self, event):
        # 윈도우 크기가 변경되면 QPixmap도 리사이즈
        new_pixmap = QPixmap(self.size())  # 새로운 QPixmap 생성
        new_pixmap.fill(Qt.white)
        painter = QPainter(new_pixmap)
        painter.drawPixmap(QPoint(0, 0), self.pixmap)  # 기존 pixmap을 그려줌
        self.pixmap = new_pixmap













def binary_to_braille_unicode(binary_data):
    """
    2400개의 2진수를 60x40 형태로 변환한 뒤, 2x4 블록으로 그룹화하여 점자 Unicode 값에서 0x2800을 뺀 값을 16진수로 변환.
    :param binary_data: 길이 2400인 1D numpy array (0과 1로 구성)
    :return: 점자 Unicode 값 (0x2800을 뺀 값, 16진수)의 2D 리스트
    """
    blocks_array = []
    for y in range(0,10):
        for x in range(0,30):
            blocks_array.append([binary_data[4*y][2*x],binary_data[4*y][2*x+1],binary_data[4*y+1][2*x],binary_data[4*y+1][2*x+1],binary_data[4*y+2][2*x],binary_data[4*y+2][2*x+1],binary_data[4*y+3][2*x],binary_data[4*y+3][2*x+1]])
    result_array = []
    braille_map = [0,4,1,5,2,6,3,7]

    for block in blocks_array:
        braille_value = 0x2800
        for bit_index, bit in enumerate(block):
            if bit == 1:
                braille_value += 1 << braille_map[bit_index]
        # print(block, chr(braille_value))
        result_array.append(f"{braille_value - 0x2800:02x}")

    return "".join(result_array)
            
            


# if __name__ == "__main__" :
#     #QApplication : 프로그램을 실행시켜주는 클래스
#     app = QApplication(sys.argv) 
#     # screen = Main_simulatorClass()
#     #WindowClass의 인스턴스 생성
#     window = PaintWidget()
#     # main = MainWindow()
#     # main = Main_simulatorClass() 
    
#     # sys.exit(app.exec_())



#     #프로그램 화면을 보여주는 코드
#     window.show()

#     #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
#     app.exec_()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    mainWindow = DotPadApp()
    mainWindow.show()

    with loop:
        loop.run_forever()


