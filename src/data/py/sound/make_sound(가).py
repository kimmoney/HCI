from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
import sounddevice as sd
import soundfile as sf

class SoundThread(QThread):
    """사운드 재생 및 WAV 파일 저장을 위한 QThread"""
    def __init__(self, filename="output.wav"):
        super().__init__()
        self.filename = filename  # 저장할 WAV 파일 이름
        self.file = sf.SoundFile(self.filename, mode='w', samplerate=44100, channels=2, subtype='PCM_16')
        self.a = 100  # 주파수 기본값
        self.b = 0.5  # 패닝 기본값
        self.switch_on = True
        self.running = True

    def run(self):
        """QThread 실행"""
        def callback(outdata, frames, time, status):
            if status:
                print(f"Status: {status}")

            if self.switch_on:
                t = (np.arange(frames) + callback.time) / 44100
                callback.time += frames

                base_frequency = 440
                frequency = base_frequency + (self.a - 100)  # 주파수 계산
                tone = 0.1 * np.sin(2 * np.pi * frequency * t)

                # 패닝 계산
                left_volume = (1 - self.b) ** 2
                right_volume = self.b ** 2

                # 좌우 채널 데이터 생성
                outdata[:, 0] = tone * left_volume  # 왼쪽 채널
                outdata[:, 1] = tone * right_volume  # 오른쪽 채널

                # WAV 파일에 저장
                self.file.write(outdata)
            else:
                outdata.fill(0)

        callback.time = 0
        with sd.OutputStream(channels=2, callback=callback, samplerate=44100, blocksize=1024):
            while self.running:
                self.msleep(10)

    def update_values(self, a, b, switch_on):
        """실시간으로 주파수와 패닝 업데이트"""
        self.a = a
        self.b = b
        self.switch_on = switch_on

    def stop(self):
        """스레드 종료 및 파일 닫기"""
        self.running = False
        self.file.close()  # WAV 파일 저장 종료
        self.quit()
        self.wait()

# 좌표 -> 사운드 매핑 함수
def coordinate_to_sound(x, y):
    """캔버스 좌표를 주파수와 패닝 값으로 변환"""
    # 주파수 매핑
    min_freq = 440
    max_freq = 1440
    a = min_freq + (max_freq - min_freq) * (y / 40)
    a = 900 - y * 20

    # 패닝 매핑
    b = x / 60

    return a, b

# 좌표 입력 이벤트 시뮬레이션
def simulate_drawing(coordinates, sound_thread):
    """좌표 입력에 따라 사운드를 갱신"""
    for x, y in coordinates:
        a, b = coordinate_to_sound(x, y)
        sound_thread.update_values(a, b, True)
        QThread.msleep(40)  # 0.04초 대기

# 실행
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    sound_thread = SoundThread("output.wav")  # 저장할 WAV 파일 이름
    sound_thread.start()

    # 좌표 리스트
    coordinates = [
        #ㄱ
        (16, 6), (17, 6), (18, 6), (19, 6), (20, 6), (21, 6), (22, 6), (23, 6), (24, 6),  (25, 6), (26, 6), (27, 6), (28, 6), (29, 6), (30, 6), (31, 6), (32, 6), 
        (31, 7),  (32, 7), (31, 8), (32, 8), (31, 9), (32, 9), (31, 10), (31, 11), (31, 12), (30, 13),  (31, 13), (30, 14), (29, 15), (30, 15), (29, 16), (28, 17), (29, 17), (28, 18),  (27, 19), (28, 19), (26, 20), (27, 20), (26, 21), (25, 22), (26, 22), (24, 23),  (25, 23), (23, 24), (24, 24), (21, 25), (22, 25), (23, 25), (20, 26), (21, 26),  (19, 27), (20, 27), (17, 28), (18, 28), (19, 28), (15, 29), (16, 29), (17, 29),
        #ㅏ
        (41, 2), (41, 3), (41, 4), (41, 5), (41, 6), (41, 7), (41, 8), (41, 9), (41, 10), (41, 11), (41, 12), (41, 13), (41, 14), (41, 15), (41, 16), (41, 17), (41, 18),  (41, 19), (41, 20), (41, 21), (41, 22), (41, 23), (41, 24), (41, 25), (41, 26),  (41, 27), (41, 28), (41, 29), (41, 30), (41, 31), (41, 32), (41, 33), (41, 34),  (41, 35), (41, 36), (41, 37), 
        (42, 17), (43, 17), (44, 17), (45, 17), (46, 17),  (47, 17), (48, 17)
    ]

    # 좌표 입력 시뮬레이션
    simulate_drawing(coordinates, sound_thread)

    # 스레드 종료
    sound_thread.stop()
    print("WAV 파일 저장 완료!")

    sys.exit(app.exec_())
   