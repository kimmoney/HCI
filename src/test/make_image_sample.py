from PIL import Image, ImageDraw, ImageFont
import random
import math

def create_text_image(text, font_path, output_path, image_size=(500, 300), font_size=30, text_position=(50, 100)):
    # 흰 배경 이미지 생성
    image = Image.new('RGB', image_size, color='white')
    
    # 드로우 객체 생성
    draw = ImageDraw.Draw(image)
    
    # 폰트 로드
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"Font file not found: {font_path}")
        return
    
    # 각 글자를 개별적으로 +-20도 이내로 랜덤 회전하여 추가
    x, y = text_position
    for char in text:
        angle = random.uniform(-20, 20)  # -20도에서 20도 사이의 랜덤 각도
        char_image = Image.new('RGBA', (font_size * 2, font_size * 2), (255, 255, 255, 0))
        char_draw = ImageDraw.Draw(char_image)
        char_draw.text((font_size / 2, font_size / 2), char, font=font, fill='black')
        char_image = char_image.rotate(angle, resample=Image.BICUBIC, expand=True)
        image.paste(char_image, (x, y), char_image)
        x += font_size  # 각 글자 간의 간격을 추가
    
    # 이미지 저장
    image.save(output_path)
    print(f"Image saved to {output_path}")

# 사용 예시
text = "abcdefg"
font_path = "/Users/hoon./Documents/GitHub/HCI/src/test/PretendardVariable.ttf"  # 사용하는 폰트 파일의 경로
output_path = "output_image.png"
create_text_image(text, font_path, output_path)
