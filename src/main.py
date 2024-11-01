import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
import test_sound
main_simulator = uic.loadUiType("src/main_simulator.ui")[0]


class Main_simulatorClass(QMainWindow, main_simulator) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.statusBar().hide()
        self.dotunit_list = [[DotUnit() for j in range(60)]for i in range(40)]
        self.clear_screen()
        for i in range(40):
            for j in range(60):
                self.screen_grid.addWidget(self.dotunit_list[i][j], i, j)


    def clear_screen(self):
        # 레이아웃에 있는 모든 항목을 지우는 함수
        while self.screen_grid.count():
            item = self.lascreen_gridyout.takeAt(0)  # 첫 번째 항목을 가져옴
            widget = item.widget()        # 해당 항목의 위젯을 가져옴
            if widget is not None:
                widget.deleteLater()      # 위젯이 있다면 삭제
            self.screen_grid.removeItem(item)  # 레이아웃에서 항목 제거
class DotUnit(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("⦁")
        self.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored))
        self.setCheckable(True)
        self.setStyleSheet(  """QPushButton:checked {
                                    background-color : rgba(0,0,0,0);
                                    border : none;
                                    color: black;
                                    font-size : 20px;
                                }
                                QPushButton:!checked {
                                    background-color : rgba(0,0,0,0);
                                    border : none;
                                    color: rgb(228, 228, 228);
                                font-size : 20px;
                                }""")




import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QMouseEvent,QImage
from PyQt5.QtCore import Qt, QPoint


class PaintWidget(QWidget):
    def __init__(self):
        self.screen = screen
        self.screen.show()
        super().__init__()
        self.setWindowTitle("Simple Paint Program with List Output")
        self.setGeometry(100, 100, 600, 400)

        # 그림을 저장할 변수
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)  # 배경을 흰색으로 채움

        # 그릴 때 사용할 펜 설정
        self.drawing = False
        self.last_point = QPoint()

        # 마우스 좌표 저장할 리스트
        self.points_list = []
        self.sound_feedback = test_sound.SoundThread()
        self.sound_feedback.start()


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
            self.screen.dotunit_list[round(self.last_point.y()/10)][round(self.last_point.x()/10)] .setChecked(True)

            print(400-self.last_point.y(),self.last_point.x()/600)
            self.sound_feedback.update_values( 400- self.last_point.y(),self.last_point.x()/600, True)
            self.update()  # 화면 갱신

    def mouseReleaseEvent(self, event):
        # 마우스를 놓으면 그림을 종료
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.sound_feedback.update_values( 400- self.last_point.y(),self.last_point.x()/600, False)

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

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    screen = Main_simulatorClass()
    #WindowClass의 인스턴스 생성
    window = PaintWidget()
    # main = Main_simulatorClass() 
    
    # sys.exit(app.exec_())



    #프로그램 화면을 보여주는 코드
    window.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()