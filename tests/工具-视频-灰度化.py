# 视频灰度化

import numpy as np
import cv2

cap = cv2.VideoCapture('rtsp://admin:Mks302302@192.168.43.68:554/ch1/main/av_stream)

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()