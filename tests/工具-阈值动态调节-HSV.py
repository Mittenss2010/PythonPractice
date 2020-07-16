# 视频 HSV
import numpy as np
import cv2

## 控制条
cv2.namedWindow('HSV_thresh')

def nothing(x):
    pass

# H:  0— 180
# S:  0— 255
# V:  0— 255

cv2.createTrackbar('THRESH_H_MAX', 'HSV_thresh', 0, 180, nothing)
cv2.createTrackbar('THRESH_H_MIN', 'HSV_thresh', 0, 180, nothing)
cv2.createTrackbar('THRESH_S_MAX', 'HSV_thresh', 0, 255, nothing)
cv2.createTrackbar('THRESH_S_MIN', 'HSV_thresh', 0, 255, nothing)
cv2.createTrackbar('THRESH_V_MAX', 'HSV_thresh', 0, 255, nothing)
cv2.createTrackbar('THRESH_V_MIN', 'HSV_thresh', 0, 255, nothing)

## main
cap = cv2.VideoCapture('rtsp://admin:Mks302302@192.168.43.68:554/ch1/main/av_stream')

while(cap.isOpened()):
    ret, frame = cap.read()

    ## 动态加载参数
    _H_MAX = cv2.getTrackbarPos('THRESH_H_MAX','HSV_thresh')
    _H_MIN = cv2.getTrackbarPos('THRESH_H_MIN','HSV_thresh')
    _S_MAX = cv2.getTrackbarPos('THRESH_S_MAX','HSV_thresh')
    _S_MIN = cv2.getTrackbarPos('THRESH_S_MIN','HSV_thresh')
    _V_MAX = cv2.getTrackbarPos('THRESH_V_MAX','HSV_thresh')
    _V_MIN = cv2.getTrackbarPos('THRESH_V_MIN','HSV_thresh')

    ## 参数操作
    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # cvtColor(src, hsv, CV_BGR2HSV);
    dst = np.zeros(frame.size, frame.dtype)

    HSV_MIN = np.array([_H_MIN, _S_MIN, _V_MIN])
    HSV_MAX = np.array([_H_MAX, _S_MAX, _V_MAX])
    mask = cv2.inRange(imgHSV, HSV_MIN, HSV_MAX)

    ## 图像展示
    frame = cv2.resize(frame,(800,600))
    mask = cv2.resize(mask,(800,600))

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()