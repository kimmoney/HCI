import sys
from PySide6.QtWidgets import *
# from PySide6 import uic
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
# import test_sound
# main_simulator = uic.loadUiType("src/main_simulator.ui")[0]
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys
from os import path
import images_rc
# import Qimage
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtGui import QPainter, QPen, QColor, QBrush, QPolygon
from PySide6.QtCore import QPoint
# UI 파일이 위치한 디렉토리 설정
ui_path = path.join(sys.path[0], "data/ui")
print(f"UI Path: {ui_path}")  # 경로를 확인하는 디버깅 출력

# UI 파일을 자동으로 로드하는 데코레이터
def load_ui(ui_file_path):
    def decorator(cls):
        original_init = cls.__init__  # 기존 __init__ 메서드를 저장

        def new_init(self, *args, **kwargs):
            # 기존 __init__ 메서드 호출
            original_init(self, *args, **kwargs)
            
            # UI 파일 경로 설정 및 확인
            full_ui_path = path.join(ui_path, ui_file_path) + ".ui"
            print(f"Full UI Path: {full_ui_path}")  # UI 파일 전체 경로 출력

            if not path.exists(full_ui_path):
                raise FileNotFoundError(f"UI file not found at {full_ui_path}")

            # QUiLoader를 사용해 UI 파일을 로드
            loader = QUiLoader()
            ui_file = QFile(full_ui_path)
            if not ui_file.open(QFile.ReadOnly):
                raise RuntimeError(f"Unable to open UI file: {full_ui_path}")

            self.ui = loader.load(ui_file, self)
            ui_file.close()
            # 로드한 UI를 메인 윈도우로 설정
            self.setCentralWidget(self.ui)
        
        cls.__init__ = new_init  # 새로운 __init__ 메서드로 교체
        return cls
    return decorator
