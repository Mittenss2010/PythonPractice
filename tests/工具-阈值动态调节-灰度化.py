# 视频灰度化

import numpy as np
import cv2

## 控制条
cv2.namedWindow('image_thresh')
def nothing(x):
    pass
cv2.createTrackbar('thrash','image_thresh',0,255, nothing)

## main
cap = cv2.VideoCapture('rtsp://admin:Mks302302@192.168.43.68:554/ch1/main/av_stream')

while(cap.isOpened()):
    ret, frame = cap.read()

    ## 动态加载参数
    thresh = cv2.getTrackbarPos('thrash','image_thresh')

    ## 参数操作
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,binary_frame = cv2.threshold( imgGray, thresh, 255, cv2.THRESH_BINARY)


    ## 图像展示
    cv2.imshow('frame',binary_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()