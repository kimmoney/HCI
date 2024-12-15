from data.py.libs import *
from data.ui.main import Ui_MainWindow
# 데코레이터로 UI 로드를 적용한 MainWindow 클래스

# @load_ui("main")
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.stacked_main.setCurrentWidget(self.login)
        self.btn_login_geust.clicked.connect(lambda: self.stacked_main.setCurrentWidget(self.menu))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())





#     sys.exit(app.exec_())

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    # screen = Main_simulatorClass()
    #WindowClass의 인스턴스 생성
    # window = PaintWidget()
    main = MainWindow()
    # main = Main_simulatorClass() 
    
    # sys.exit(app.exec_())



    #프로그램 화면을 보여주는 코드
    # window.show()
    main.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()




