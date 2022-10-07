# Ref: https://www.youtube.com/watch?app=desktop&v=O3b8lVF93jU&feature=youtu.be

import cv2
from matplotlib.pyplot import box
from tracker import *

tracker = EuclideanDistTracker()

# 처리할 동영상 불러오기.
video = cv2.VideoCapture('highway.mp4')

# 동영상으로부터 움직이는 물체 감지.
# 단, 실제로 움직이는 물체를 감지하는 것이 아닌, 변화가 적은 화소를 찾으므로 후처리가 필요하다.
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    # 동영상으로부터 단일 프레임 읽기.
    ret, frame = video.read()
    height, width, _ = frame.shape

    # 이미지 인식을 수행할 영역 지정. (Region of Interest)
    roi = frame[340:720, 500:800]

    # roi에서 배경 제거.
    mask = object_detector.apply(roi)
    # 그림자 등 완전히 하얗게 처리된 영역이 아니면 무시.
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    # 배경을 제거한 후 경계를 추출한다.
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 물체 추적을 위한 리스트.
    detected = []
    for cnt in contours:
        # 추출된 경계 내부의 영역의 크기에 따라서 크기가 일정 수준보다 작으면 무시.
        area = cv2.contourArea(cnt)
        if area < 100:
            continue

        # 추출한 경계를 녹색으로 'Frame'에 표시.
        # cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
        x, y, w, h = cv2.boundingRect(cnt)

        # 물체 추적을 위해 detected에 감지된 물체 정보 추가.
        detected.append([x, y, w, h])

    # 트래커를 이용해 물체 추적. (감지된 물체에 고유번호 부여)
    boxes_ids = tracker.update(detected)
    print(boxes_ids)
    for box_id in boxes_ids:
        # 추적한 물체의 고유번호와 경계 출력.
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # 필요한 항목을 창의 띄워 출력.
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Region of Interest', roi)

    # 각 프레임마다 30 밀리초 동안 키 입력 대기.
    key = cv2.waitKey(30)
    # <ESC> 감지 시 동영상 출력 중단.
    if key == 27:
        break

# 동영상 출력 중단 및 모든 창 닫기.
video.release()
cv2.destroyAllWindows()