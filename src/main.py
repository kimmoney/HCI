
from SDK import DotPadSDK
from data.py.libs import *
from data.ui.main import Ui_MainWindow
from data.py.image_process import text_to_image_array
from data.py.libs import *
from data.ui.main import Ui_MainWindow
from data.ui.course_unit import Ui_Form as UI_CourseUnit
window_map = np.array([[0]*60]*40)
# result_map = np.array([[0]*60]*40)
result_map ,result_img = text_to_image_array("개")
activity_map = np.array([[0]*60]*40)
before_map = result_map.copy()
# result_img= Image.new("RGB", (60, 400), color=(0, 0, 0))
state = "window"




class DotPadApp(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(DotPadApp, self).__init__()
        # Load ui
        self.setupUi(self)
        # 초기 페이지 설정
        self.sdk = DotPadSDK("iPad")  # DotPad SDK 초기화
        self.device = None

        self.stacked_main.setCurrentWidget(self.login)
        # 버튼 클릭 이벤트 연결 - 로그인 -> 메인
        self.btn_login_geust.clicked.connect(lambda: self.stacked_main.setCurrentWidget(self.menu))
        self.btn_login_login.clicked.connect(lambda: self.stacked_main.setCurrentWidget(self.menu))
        self.input_login_id.returnPressed.connect(lambda: self.stacked_main.setCurrentWidget(self.menu))
        self.input_login_pw.returnPressed.connect(lambda: self.stacked_main.setCurrentWidget(self.menu))

        # 버튼 클릭 이벤트 연결 - 메인 -> 연결중
        self.btn_learning.clicked.connect(lambda: self.stacked_main.setCurrentWidget(self.connecting))
        # 버튼 클릭 이벤트 연결 - 닷패드 연결 -> 완료시 학습단계
        self.btn_learning.clicked.connect(self.connect_device)
# 임시
        # self.stacked_main.setCurrentWidget(self.course)

        # 버튼 클릭 이벤트 연결 - 학습단계 -> 메인
        self.btn_curse2home.clicked.connect(lambda: self.stacked_main.setCurrentWidget(self.menu))

        # 닷패드 sdk 추가

        # 캔버스 생성
        self.canvas = PaintWidget(self)
        self.layout_painting.addWidget(self.canvas)
        course_data = {"level1": ['ㄱ','ㄴ','ㄱ','ㅏ','ㅐ','가','간','개'],"level2": ['ㄱ','ㄴ','ㄱ','ㅏ','ㅐ','가','간','개'],"level3": ['ㄱ','ㄴ','ㄱ','ㅏ','ㅐ','가','간','개'],}
        for course in course_data:
            index = 0
            for i in course_data[course]:
                getattr(self,course).layout().addWidget(courseUnitClass(self,i),index%2,index//2)
                index += 1
        
        self.audio_output = QAudioOutput()
        self.media_player = QMediaPlayer()
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.mediaStatusChanged.connect(self.on_media_status_changed)

    # 닷패드 디바이스 연결 비동기 작업
    async def async_connect_device(self):
        print("Searching for DotPad devices...")
        try:
            self.devices = await self.sdk.request()
            if not self.devices:
                raise Exception("No DotPad devices found.")
            self.device = self.devices[0]
            print(f"Try connecting device: {self.device.name}")
            connected = await self.sdk.connect(self.device)
            if connected:
                print(f"Connected to {self.device.name}")
                self.stacked_main.setCurrentWidget(self.course)

                # 키 이벤트 리스너 시작
                await self.add_key_event_listener()
            else:
                print("Failed to connect.")
                self.stacked_main.setCurrentWidget(self.menu)

        except Exception as e:
            print(f"Error during connection: {e}")
    # 닷패드 디스플레이 연결 
    def connect_device(self):
        """버튼 클릭 이벤트에서 비동기 작업 실행"""
        asyncio.create_task(self.async_connect_device())
    # 그래픽 데이터 표시 비동기 작업
    async def async_display_graphic(self):
        if self.device:
            print("Displaying graphic data...")
            await self.sdk.display_graphic_data(self.device.name, self.input.text())
    # 그래픽 데이터 표시
    def display_graphic(self):
        """버튼 클릭 이벤트에서 비동기 작업 실행"""
        asyncio.create_task(self.async_display_graphic())
    # 그래픽 데이터 리셋 비동기 작업
    async def async_reset_graphic(self):
        if self.device:
            print("Resetting graphic data...")
            await self.sdk.reset_graphic_data(self.device.name)
    # 그래픽 데이터 리셋
    def reset_graphic(self):
        
        asyncio.create_task(self.async_reset_graphic())
    # 픽셀 데이터 표시 비동기 작업
    async def add_key_event_listener(self):
        # 닷패드 fucntion key 이벤트 콜백 정의
        async def key_event_callback(event_code):
            global state,before_map
            print(f"Key event received: {event_code}")
            # 키 이벤트에 따라 동작 match
            match event_code:
                # Function key 1 : 그래픽 데이터 리셋
                case "8":
                    # 닷패드 리셋
                    await self.sdk.reset_graphic_data(self.device.name)
                    # 인터페이스 리셋
                    self.canvas.reset_canvas()
                # Function key 2 : 위치 찾기 모드
                case "4":
                    # 모드 전환
                    state = "activity"
                # Function key 3 : 결과 확인 모드
                case "2":
                    # 결과 화면 출력
                    await self.sdk.display_graphic_data(self.device.name, "".join(binary_to_braille_unicode(result_map)))
                    # 모드 전환
                    before_map = result_map
                    state = "result"
                # Function key 4 : 사용자 화면 모드
                case "1":
                    # 사용자 화면 출력
                    await self.sdk.display_graphic_data(self.device.name, "".join(binary_to_braille_unicode(window_map)))
                    # 모드 전환
                    before_map = window_map
                    state = "window"
                # Function key LP : 메뉴로 돌아가기
                case"LP":
                    self.stacked_main.setCurrentWidget(self.course)
                # Function key RP : 검증모드로 전환
                case"RP":
                    self.stacked_main.setCurrentWidget(self.validation)
                    score = self.calculate_similarity_with_tolerance(window_map,result_map)
                    print(f"유사도: {score}")
                    if score<90:
                        self.play_tts(f"유사도가 {int(score)}점으로 기준보다 낮습니다. 다시 시도해주세요. 코스 선택으로 이동합니다.")
                    else:
                        self.play_tts(f"유사도가 {int(score)}점으로 기준을 통과했습니다. 코스 선택으로 이동합니다.")
                    # self.play_tts("검증모드로 전환합니다.")
                        
                
        try:
            await self.sdk.add_listener_key_event(self.device.name, key_event_callback)
            print("Key event listener added. Waiting for events...")
        except Exception as e:
            print(f"Error during adding key event listener: {e}")


    def calculate_similarity_with_tolerance(self,image1, image2, tolerance=1):
        """
        한 픽셀 이동을 허용하면서 두 이미지의 유사도를 계산.
        
        Parameters:
            image1 (numpy array): 첫 번째 이진화 이미지
            image2 (numpy array): 두 번째 이진화 이미지
            tolerance (int): 이동 허용 픽셀 수 (기본값 1)
        
        Returns:
            float: 100점 만점의 유사도 점수
        """
        # 이미지 크기가 동일한지 확인
        assert image1.shape == image2.shape, "두 이미지의 크기가 같아야 합니다."

        # image2에 대한 확장 (이동 허용 범위 생성)
        expanded_image2 = binary_dilation(image2, structure=np.ones((2*tolerance+1, 2*tolerance+1)))

        # image1의 픽셀 중 expanded_image2와 일치하는 픽셀 계산
        matching_pixels = np.sum((image1 == 1) & (expanded_image2 == 1))

        # image1에서 1인 픽셀 총 수
        total_pixels = np.sum(image1 == 1)

        # 유사도 점수 계산
        similarity_score = matching_pixels / total_pixels * 100 if total_pixels > 0 else 0
        return similarity_score
    
    def play_tts(self,text):
        # 텍스트를 음성으로 변환하여 임시 파일에 저장
        # text = "안녕하세요. PySide에서 TTS를 실행합니다."
        tts = gTTS(text=text, lang='ko')

        # 임시 파일 생성
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
            temp_filename = temp_file.name
            tts.save(temp_filename)
            print(f"TTS 저장 파일: {temp_filename}")

        # 임시 파일을 QMediaPlayer로 재생
        self.media_player.setSource(QUrl.fromLocalFile(temp_filename))
        self.media_player.play()
    def on_media_status_changed(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            
            # 임시 파일 삭제
            import os
            if hasattr(self, 'temp_filename') and os.path.exists(self.temp_filename):
                os.remove(self.temp_filename)
                print(f"임시 파일 삭제: {self.temp_filename}")
            self.stacked_main.setCurrentWidget(self.course)

# 캔버스에 그림그리는 class
class PaintWidget(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.sdk = parent.sdk
        # 모범 답안 글자
        self.letter = "각"
        # 그림을 저장할 변수
        self.pixmap = QPixmap(600, 400)  # QPixmap으로 초기화
        self.pixmap.fill(Qt.white)  # 배경을 흰색으로 채움
        self.before_points = (0,0,0,0,"00")
        # 그릴 때 사용할 펜 설정
        self.drawing = False
        # 연속 그림을 그릴 때 이전 좌표 저장
        self.last_point = QPoint()
        # 마우스 좌표 저장할 리스트
        self.points_list = []
        # 사운드 피드백 클래스 정의
        self.sound_feedback = sound_live.SoundThread()
        # 사운드 피드백 시작
        self.sound_feedback.start()
    # 창이 띄워지면 닷패드 및 캔버스 초기화
    # def showEvent(self, event):
    #     self.reset_canvas()
    # 캔버스 리셋
    def reset_canvas(self):
        # map 전역변수 사용
        global window_map,result_map,activity_map
        # 사용자 화면 초기화
        window_map = np.array([[0]*60]*40)
        # 모범답안 초기화
        result_map ,result_img = text_to_image_array(str(self.letter))
        # 이동관련 초기화
        activity_map = np.array([[0]*60]*40)
        # 배경 흰색 채우기
        self.pixmap.fill(Qt.white)
        # 변경사항 저장
        self.update()
        # 닷패드 그래픽 데이터 리셋
        self.parent.reset_graphic()
    # 화면 터치시 그리기 모드 시작
    def mousePressEvent(self, event):
        # 마우스를 누를 때
        if event.button() == Qt.LeftButton:
            # 그리기 상태 = True
            self.drawing = True
            # 지난 좌표 저장
            self.last_point = event.pos()
    # 마우스 이동시 그리기
    def mouseMoveEvent(self, event):
        # 마우스를 움직일 때
        if event.buttons() & Qt.LeftButton and self.drawing:
            painter = QPainter(self.pixmap)  # QPixmap에서 QPainter 사용
            pen = QPen(Qt.black, 25, Qt.SolidLine)  # 펜 설정 (색상, 두께)
            pen.setCapStyle(Qt.RoundCap)
            painter.setPen(pen)
            
            x = max(0,min(59, event.pos().x()/self.size().width()*60))
            y = max(0,min(39, event.pos().y()/self.size().height()*40))
            dot_x = int(x/2)
            dot_y = int(y/4)
            match state:
                case "window":
                    painter.drawLine(self.last_point, event.pos())  # 선을 그림
                    self.last_point = event.pos()   
                    self.update()  # 화면 갱신
                    if window_map[int(y)][int(x)] != 1:
                        window_map[int(y)][int(x)] = 1
                        asyncio.create_task(mainWindow.sdk.display_pixel_data(mainWindow.device.name,binary_to_braille_unicode(window_map,(dot_y,dot_x)),dot_y+1,dot_x))
                case "result":
                    pass
                case "activity":
                    if int(x)!= int(self.before_points[0]) or int(y) != int(self.before_points[1]):
                        activity_map = before_map.copy()
                        print(dot_x,dot_y,self.before_points[2],self.before_points[3])
                        if not (dot_x == self.before_points[2] and dot_y == self.before_points[3]):
                            asyncio.create_task(mainWindow.sdk.display_pixel_data(mainWindow.device.name,self.before_points[-1],self.before_points[3]+1,self.before_points[2]))
                        before_pixel = binary_to_braille_unicode(activity_map,(dot_y,dot_x))
                        activity_map[int(y)][int(x)] = 1
                        
                        asyncio.create_task(mainWindow.sdk.display_pixel_data(mainWindow.device.name,binary_to_braille_unicode(activity_map,(dot_y,dot_x)),dot_y+1,dot_x))
                        self.before_points = (x,y,dot_x,dot_y,before_pixel)
            self.sound_feedback.update_values(self.size().height() - event.pos().y(), event.pos().x() / self.size().width(), True)


                    

    def mouseReleaseEvent(self, event):
        # 마우스를 놓으면 그림을 종료
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.sound_feedback.update_values(400 - self.last_point.y(), self.last_point.x() / 600, False)
            asyncio.create_task(mainWindow.sdk.display_pixel_data(mainWindow.device.name,self.before_points[-1],self.before_points[3]+1,self.before_points[2]))
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

    


    # def analyze_image(self):
    #     global result_map, result_img

    #     # QPixmap -> OpenCV 이미지 변환
    #     img1 = qpixmap_to_cv_image(self.pixmap)
    #     img2 = cv2.cvtColor(np.array(result_img), cv2.COLOR_RGB2BGR)
    def analyze_image(self):
        global result_map, result_img
        # 일단 이미지 저장
        self.pixmap.save("test.png")
        ImageOps.invert(result_img).save("result.png")
        image1_path = "test.png"
        image2_path = "result.png"
        # Step 1: Resize both images to 60x40
        target_size = (60, 40)

        image1 = Image.open(image1_path).resize(target_size)
        image2 = Image.open(image2_path).resize(target_size)

        # Step 2: Convert the first image (result.png) to inverted grayscale
        # image1 = ImageOps.invert(ImageOps.grayscale(image1))

        # Step 3: Convert both images to numpy arrays for comparison
        array1 = np.array(image1, dtype=np.float32) / 255.0  # Normalize to [0, 1]
        array2 = np.array(image2.convert("L"), dtype=np.float32) / 255.0  # Convert second image to grayscale and normalize

        # Step 4: Compute similarity using minimal modification error
        error = np.mean((array1 - array2) ** 2)  # Mean Squared Error (MSE)
        similarity = 1 - error  # Convert error to similarity (1 means identical)
        plt.subplot(1, 2, 1)
        plt.imshow(array1, cmap="gray")
        plt.title("Result")
        plt.axis("off")
        plt.subplot(1, 2, 2)
        plt.imshow(array2, cmap="gray")
        plt.title("Test")
        plt.axis("off")
        plt.show()
        
        
        return similarity








def binary_to_braille_unicode(binary_data,pos=(0,0)):
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
    if pos != (0,0):
        blocks_array = [blocks_array[pos[0]*30+pos[1]]]
    for block in blocks_array:
        braille_value = 0x2800
        for bit_index, bit in enumerate(block):
            if bit == 1:
                braille_value += 1 << braille_map[bit_index]
        # print(block, chr(braille_value))
        result_array.append(f"{braille_value - 0x2800:02x}")

    return "".join(result_array)

                
def qpixmap_to_cv_image(qpixmap):
    """QPixmap을 OpenCV의 NumPy 배열로 변환"""
    qimage = qpixmap.toImage()
    qimage = qimage.convertToFormat(QImage.Format.Format_RGB888)
    width = qimage.width()
    height = qimage.height()
    ptr = qimage.bits()
    arr = np.array(ptr).reshape((height, width, 3))  # NumPy 배열로 변환
    return cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)



class courseUnitClass(QWidget,UI_CourseUnit):
    def __init__(self,parent,keyword):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.keyword = keyword
        self.result_map, self.result_img = text_to_image_array(keyword)
        # pillow image -> qpixmap
        scaled_result_map = 255-(self.result_map * 255).astype(np.uint8)

        # NumPy 배열에서 QImage로 변환
        height, width = scaled_result_map.shape
        qimage = QImage(scaled_result_map.data, width, height, width, QImage.Format_Grayscale8)

        # QPixmap 생성
        self.image_keword = QPixmap.fromImage(qimage)

        # 이미지를 지정된 크기에 맞게 비율 유지하며 조정
        target_size = QSize(234, 118)
        self.image_keword = self.image_keword.scaled(target_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # QLabel에 이미지 설정
        self.image.setPixmap(self.image_keword)

        # 텍스트 설정
        self.name.setText(keyword)

    def mousePressEvent(self, event):
        print(self.keyword)
        self.parent.canvas.letter = self.keyword
        QTimer.singleShot(0, self.play_sound)
        self.parent.canvas.reset_canvas()
        self.parent.stacked_main.setCurrentWidget(self.parent.painting)
        # 결과 화면 출력
        asyncio.create_task(self.parent.sdk.display_graphic_data(self.parent.device.name, "".join(binary_to_braille_unicode(result_map))))
        global state,before_map
        # 모드 전환
        state = "result"
        before_map = result_map.copy()
        # sound play path

        # .wav 파일 경로 설정
        # wav_file = 'example.wav'

        # asyncio.create_task(self.play_sound())
    def play_sound(self):
        # .wav 파일 경로 설정
        wav_file = f"src/data/py/sound/output({self.keyword}).wav"
        # .wav 파일 읽기
        data, samplerate = sf.read(wav_file)
        # 데이터 출력
        print(f"Data shape: {data.shape}, Samplerate: {samplerate}")
        # 오디오 재생
        sd.play(data, samplerate)
        # 재생이 끝날 때까지 대기
        # sd.wait()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    mainWindow = DotPadApp()
    mainWindow.show()

    with loop:
        loop.run_forever()


