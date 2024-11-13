import torch
import cv2
import time
import numpy as np

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/TTTTTTTT/yolov5_master/yolov5_master/runs/train/TTT122/weights/best.pt')

# 웹캠 캡처 객체 생성 (기본 웹캠의 인덱스는 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

# 탐지 추적을 위한 변수 초기화
detected = False
detected_start_time = None
last_message_time = None

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    
    if not ret:
        print("프레임을 가져올 수 없습니다.")
        break

    # 프레임을 모델에 입력하기 위해 전처리
    results = model(frame)

    # 결과를 OpenCV로 그리기
    current_detected = False
    for *xyxy, conf, cls in results.xyxy[0]:
        label = f'{model.names[int(cls)]} {conf:.2f}'
        xyxy = [int(i) for i in xyxy]
        cv2.rectangle(frame, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (0, 255, 0), 2)
        cv2.putText(frame, label, (xyxy[0], xyxy[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # 탐지된 객체가 있으면 current_detected를 True로 설정
        current_detected = True

    # 탐지 상태 변경 시 시간 기록
    if current_detected:
        if not detected:
            detected_start_time = time.time()
            detected = True
        elif time.time() - detected_start_time >= 2:
            if last_message_time is None or time.time() - last_message_time >= 1:
                print("약을 인식했습니다. 약을 복용해주세요")
                last_message_time = time.time()
    else:
        detected = False
        detected_start_time = None
        last_message_time = None

    # 프레임을 창에 표시
    cv2.imshow('Webcam', frame)

    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 및 창 닫기
cap.release()
cv2.destroyAllWindows()