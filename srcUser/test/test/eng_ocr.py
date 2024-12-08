import cv2
import numpy as np
import tensorflow as tf
import random

# 미리 학습된 딥러닝 모델을 로드합니다 (예: 손글씨 인식을 위한 CRNN 모델)
# model = tf.keras.models.load_model('handwriting_recognition_model.h5')

# 손글씨 이미지를 불러옵니다.
image = cv2.imread('/Users/hoon./Documents/GitHub/HCI/src/test/output_image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이진화 처리
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# 윤곽선 찾기
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 각 알파벳을 감싸는 Bounding Box 그리기 및 회전 각도 파악
for contour in contours:
    # 최소 외접 사각형을 구합니다.
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    
    # 회전 각도 가져오기
    angle = rect[-1]
    
    # 영역 잘라내기 및 회전 보정
    width, height = int(rect[1][0]), int(rect[1][1])
    src_pts = box.astype("float32")
    dst_pts = np.array([[0, height-1], [0, 0], [width-1, 0], [width-1, height-1]], dtype="float32")
    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    warped = cv2.warpPerspective(gray, M, (width, height))
    
    # 딥러닝 모델로 문자 인식 (여기서는 가정)
    # input_image = cv2.resize(warped, (input_size, input_size))
    # input_image = input_image / 255.0
    # input_image = np.expand_dims(input_image, axis=[0, -1])
    # predicted_text = model.predict(input_image)
    # text = decode_prediction(predicted_text)
    
    # 무작위 색상 생성
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # Bounding Box 그리기
    cv2.drawContours(image, [box], 0, color, 2)
    cv2.putText(image, f'Angle: {angle:.2f}', (int(rect[0][0]), int(rect[0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

# 결과 출력
cv2.imshow('Alphabet Segmentation with Rotation Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
