import numpy as np
import cv2

xml = '../haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(xml)

mosaic_img = cv2.imread('bear.jpg')

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while(True):
    ret, frame = cap.read() 
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.05, 5)

    for x,y,w,h in faces:
        t = cv2.resize(mosaic_img, dsize=(h, w), interpolation=cv2.INTER_LINEAR)
        frame[y:y + h, x:x + w] = t

    cv2.imshow('result', frame)
        
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()