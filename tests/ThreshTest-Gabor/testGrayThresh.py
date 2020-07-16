
# 图像阈值分割，阈值调节
import cv2
import numpy as np

# Create a black image, a window
imgGray = cv2.imread("ROI323.jpg",0)

cv2.namedWindow('image_thresh')

def nothing(x):
    pass

# create trackbars for color change
cv2.createTrackbar('thrash','image_thresh',0,255, nothing)

while(1):
    # get current positions of four trackbars
    thresh = cv2.getTrackbarPos('thrash','image_thresh')

    imgblur = cv2.GaussianBlur(imgGray,(3,3),0)
    ret, otsu = cv2.threshold(imgblur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    ret,binary_frame = cv2.threshold( imgGray, thresh, 255, cv2.THRESH_BINARY)

    cv2.imshow('image',imgGray)
    cv2.imshow('binary_frame',binary_frame)

    cv2.imshow('otsu_frame',otsu) 
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
