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
       (16, 7), (17, 7), (18, 7), (19, 7), (20, 7), (21, 7), (22, 7), (23, 7), (24, 7), (25, 7),
        (26, 7), (27, 7), (28, 7), (29, 7), (28, 8), (29, 8), (28, 9), (29, 9), (28, 10), (29, 10),
        (28, 11), (28, 12), (28, 13), (28, 14), (27, 14), (27, 15), (27, 16), (27, 17), (26, 17),
        (26, 18), (26, 19), (25, 19), (25, 20), (24, 20), (24, 21), (24, 22), (23, 22), (23, 23),
        (22, 23), (22, 24), (21, 24), (21, 25), (20, 25), (20, 26), (19, 26), (19, 27), (18, 27),
        (17, 27), (17, 28), (16, 28), (15, 28), (15, 29),
        (36, 3), (36, 4), (36, 5), (36, 6), (36, 7), (36, 8), (36, 9), (36, 10), (36, 11), (36, 12), (36, 13), (36, 14), (36, 15), (36, 16), (36, 17), (36, 18), (36, 19), (36, 20), (36, 21), (36, 22), (36, 23), (36, 24), (36, 25), (36, 26), (36, 27), (36, 28), (36, 29), (36, 30), (36, 31), (36, 32), (36, 33), (36, 34), (36, 35), 
        (37, 17), (37, 18), (38, 17), (38, 18), (39, 17), (39, 18), (40, 17), (40, 18), (41, 17), (41, 18), (42, 17), (42, 18), (43, 17), (43, 18), 
        (44, 2), (44, 3), (44, 4), (44, 5), (44, 6), (44, 7), (44, 8), (44, 9), (44, 10), (44, 11), (44, 12), (44, 13), (44, 14), (44, 15), (44, 16), (44, 17), (44, 18), (44, 19), (44, 20), (44, 21), (44, 22), (44, 23), (44, 24), (44, 25), (44, 26), (44, 27), (44, 28), (44, 29), (44, 30), (44, 31), (44, 32), (44, 33), (44, 34), (44, 35), (44, 36), (44, 37)

    ]

    # 좌표 입력 시뮬레이션
    simulate_drawing(coordinates, sound_thread)

    # 스레드 종료
    sound_thread.stop()
    print("WAV 파일 저장 완료!")

    sys.exit(app.exec_())


        