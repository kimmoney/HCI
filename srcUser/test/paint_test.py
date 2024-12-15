import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QMouseEvent,QImage
from PyQt5.QtCore import Qt, QPoint

class PaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Paint Program with List Output")
        self.setGeometry(100, 100, 800, 600)

        # 그림을 저장할 변수
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)  # 배경을 흰색으로 채움

        # 그릴 때 사용할 펜 설정
        self.drawing = False
        self.last_point = QPoint()

        # 마우스 좌표 저장할 리스트
        self.points_list = []

    def mousePressEvent(self, event):
        # 마우스를 누르면 그림을 시작
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        # 마우스를 움직일 때 그림 그리기
        if event.buttons() & Qt.LeftButton and self.drawing:
            painter = QPainter(self.image)
            pen = QPen(Qt.black, 3, Qt.SolidLine)  # 펜 설정 (색상, 두께)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())  # 선을 그림
            self.last_point = event.pos()
            
            # 현재 그린 위치를 리스트에 추가
            self.points_list.append((self.last_point.x(), self.last_point.y()))

            # 리스트 출력
            print(self.points_list)

            self.update()  # 화면 갱신

    def mouseReleaseEvent(self, event):
        # 마우스를 놓으면 그림을 종료
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        # QImage를 화면에 그림
        canvas_painter = QPainter(self)
        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())

    def resizeEvent(self, event):
        # 윈도우 크기가 변경되면 이미지도 리사이즈
        new_image = QImage(self.size(), QImage.Format_RGB32)
        new_image.fill(Qt.white)
        painter = QPainter(new_image)
        painter.drawImage(QPoint(0, 0), self.image)
        self.image = new_image

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = PaintWidget()
#     window.show()
#     sys.exit(app.exec_())



import winsound
import keyboard


def play_sound(frequency):
    """ 주파수와 지속 시간을 입력받아 소리 재생 """
    winsound.Beep(frequency, 1000000)
    print(f"Playing sound with frequency: {frequency}")
def stop_sound():
    """ 소리 정지 """
    winsound.Beep(37, 0)
while True:
    if keyboard.is_pressed('a'):
        stop_sound()
        play_sound(440)
    elif keyboard.is_pressed('s'):
        stop_sound()
        play_sound(494) # 도# (C#)
    elif keyboard.is_pressed('d'):
        stop_sound()
        play_sound(523)
    elif keyboard.is_pressed('f'):
        stop_sound()
        play_sound(587)
