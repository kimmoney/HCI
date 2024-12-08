



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
