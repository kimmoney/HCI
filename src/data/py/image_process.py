from data.py.libs import *

# def text_to_image_array(text, image_size=(60, 40), font_path="src/data/SC/NotoSerifSC-ExtraLight.otf"):
def text_to_image_array(text, image_size=(60, 40), font_path="src/data/SC/Pretendard-Thin.ttf"):
    """
    주어진 텍스트를 이진화된 이미지의 numpy 배열로 변환합니다.
    """
    # Step 1: Pillow를 사용하여 텍스트 이미지 생성
    img = Image.new("RGB", (1200, 800), color=(0, 0, 0))  # 큰 검은색 배경
    draw = ImageDraw.Draw(img)

    # 지정된 폰트 로드 (폰트 크기 설정)
    font = ImageFont.truetype(font_path, size=500)
    # 텍스트 크기를 계산하여 배치
    text_bbox = draw.textbbox((0, 0), text, font=font)  # 텍스트의 경계 박스
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (img.width - text_width) // 2  # 중앙 X 좌표
    text_y = (img.height - text_height) // 2  # 중앙 Y 좌표
    # 텍스트를 이미지에 그리기
    draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255))  # 흰색 텍스트
    # 텍스트의 실제 경계 영역 잘라내기 (상하 여백 5% 추가)
    if len(text)==2:
         extra_padding = int(text_height * 0.3)  # 상하 여백 계산
    else:
        extra_padding = int(text_height * 0.05)
        extra_padding_x = int(text_width * 0.3)
    cropped_img = img.crop((
        text_bbox[0] + text_x - extra_padding_x, 
        text_bbox[1] + text_y - extra_padding, 
        text_bbox[2] + text_x + extra_padding_x, 
        text_bbox[3] + text_y + extra_padding
    ))
    # Pillow 이미지를 OpenCV 형식으로 변환
    open_cv_image = np.array(cropped_img)
    open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
    # Step 2: 이미지를 원하는 크기로 조정
    resized_img = cv2.resize(open_cv_image, image_size)
    # Step 3: 이미지를 그레이스케일로 변환
    grayscale_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    # Step 4: 이진화된 배열로 변환
    binary_array = (grayscale_img > 128).astype(int)  # 0과 1로 변환

    return binary_array, cropped_img
