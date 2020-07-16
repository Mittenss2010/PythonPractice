
# 图像阈值分割，阈值调节
import cv2
import numpy as np
import time
import imutils


# Create a black image, a window
fileName = "test6.jpg"
print('file name = '+ fileName)

imgGray = cv2.imread(fileName,0)
imgblur = cv2.GaussianBlur(imgGray, (3,3), 0)

#区域分割
time_otsu = time.time()
ret, otsu = cv2.threshold( imgblur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print('OSTU_TimeCost :****     '+ str(round( time.time() - time_otsu, 4))+ ' S')


# 区域计算
time_caclRange = time.time()            #############################################################start cacl
left_Pos = 0
right_Pos = 0
beginIndex = 0
N = 10
maxWidth = 2592
maxHeight = 255
for i in range(otsu.shape[0]):          # 遍历次数 shape[0]
    #print(otsu[i,N])
    if otsu[maxHeight-i,N] < 255:
        left_Pos = i
        break

ref_N = maxWidth - N                    # N 对称值
for i in range(otsu.shape[0]):          # 遍历次数 shape[0]
    #print(otsu[i,ref_N])
    if otsu[maxHeight - i,ref_N] < 255:
        right_Pos = i
        break
print('区域参数********************************')   
print('left_Pos :****      ' + str(left_Pos))
print('right_Pos :****     ' +  str(right_Pos))

maxNone_ROI = max(left_Pos, right_Pos)
print('亮区max =  :****    ' +  str(maxNone_ROI))

balence_diff_Pixes_LR = abs(left_Pos - right_Pos)
print('平衡差 =  :****     ' +  str(balence_diff_Pixes_LR))
print('区域参数END*****************************') 

# 图像裁剪
imgROI = imgblur[beginIndex: (maxHeight -  maxNone_ROI), beginIndex:maxWidth]

print('裁剪区域size()：' + str(imgROI.shape))
print('ROI裁剪_TimeCost :****     '+ str(round( time.time() - time_caclRange, 4))+ ' S')
print('OSTU +  区域裁剪_TimeCost   '+ str(round( time.time() - time_otsu, 4))+ ' S')


time_imResize = time.time() #############################################################start cacl
imgROI = imutils.resize(imgROI, width=1280)       # 缩放
imgblur = imutils.resize(imgblur, width=1280)       # 缩放
otsu = imutils.resize(otsu, width=1280)       # 缩放

cv2.imshow('ROI_frame', imgROI) 
cv2.imshow('imgblur_frame', imgblur) 
cv2.imshow('otsu_frame', otsu)
print('resize & show_TimeCost :****     '+ str(round( time.time() - time_imResize, 4))+ ' S')

k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()