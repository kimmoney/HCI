import sys
import numpy as np
import sounddevice as sd
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QSlider, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QThread, Signal


class SoundThread(QThread):
    """ 사운드 재생을 위한 QThread """
    update_sound = Signal(float, float, bool)  # a, b, switch 상태를 업데이트하는 시그널

    def __init__(self):
        super().__init__()
        self.a = 100  # 기본 주파수 조절 값
        self.b = 0.5  # 좌우 볼륨 비율
        self.switch_on = False  # 스위치 상태 (True: 재생, False: 정지)
        self.running = True  # 스레드 실행 플래그

    def run(self):
    # """ QThread에서 실행될 내용 """
        def callback(outdata, frames, time, status):
            if status:
                print(f"Status: {status}")  # 상태 체크를 위해 오류 발생 시 출력

            if self.switch_on:
                t = (np.arange(frames) + callback.time) / 44100 # 시간 벡터 계산

                # print(44100* self.a /100,"-----")
                callback.time += frames  # 시간 경과 업데이트

                # 주파수 계산 (1440Hz + a 값으로 변경)
                base_frequency = 440
                frequency = base_frequency + (self.a - 100)  # 주파수 계산
                tone = 0.1 * np.sin(2 * np.pi * frequency * t)

                # 좌우 볼륨 조절 (b 값에 따라 결정)
                left_volume = max(0, min(1,  self.b))
                right_volume = max(0, min(1,1 - self.b))

                # 좌우 채널 볼륨 조정 후 스테레오 음으로 변환
                # outdata[:, 0] = tone * left_volume  # 왼쪽 채널
                # outdata[:, 1] = tone * right_volume  # 오른쪽 채널
                outdata[:, 1] = tone * left_volume  # 왼쪽 채널
                outdata[:, 0] = tone * right_volume  # 오른쪽 채널
            else:
                outdata.fill(0)  # 스위치가 꺼져 있으면 무음 처리

        # 시간 초기화
        callback.time = 0

        # 오디오 스트리밍 시작
        with sd.OutputStream(channels=2, callback=callback, samplerate=44100, blocksize=1024):
            while self.running:
                self.msleep(400)  # 0.4초마다 대기


    def update_values(self, a, b, switch_on):
        """ 주파수, 볼륨, 스위치 상태 업데이트 """
        if self.a != a or self.b != b or self.switch_on != switch_on:
            print(a, b, switch_on)
            # self.a = a
            if a < 0:
                self.a = 0
            else:
                self.a = a
            
            self.b = b
            self.switch_on = switch_on

    def stop(self):
        """ 스레드 종료 """
        self.running = False
        self.quit()
        self.wait()
