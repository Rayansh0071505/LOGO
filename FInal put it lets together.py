import cv2
import numpy as np

#preprocessing
cap = cv2.VideoCapture(1)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

logo = cv2.imread("C:\\Users\\Rayan\\Downloads\\logo.png")
size = 100
logo = cv2.resize(logo, (size, size))
gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

while True:
    _, frame = cap.read()

    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)

    roi = frame[-size - 10:-10, -size - 10:-10] # providing width and height to logo or space
    roi[np.where(mask)] = 0
    roi += logo
    # we put mask here as where took only non zero value while mask contain non zero value
    # as threshold already filter all zero value now it look like black

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break