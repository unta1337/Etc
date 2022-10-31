from cv2 import calibrationMatrixValues
import numpy as np
import cv2

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 640)

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.imwrite('camera_test.jpg', frame)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()