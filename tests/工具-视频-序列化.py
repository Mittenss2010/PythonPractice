视频序列化

import numpy as np
import cv2
import os
​
# def video_sequence( )
​
sample_freq = 150                        # 采样率
strfolderName = 'VideoSequence'          # 视频序列文件夹名称
video_name = '30531_钻台面_20190305.mp4' # 文件名

# 判断存在,创建新的数据集路径
isExists=os.path.exists('./'+ strfolderName)
if not isExists:
    os.mkdir('./' + strfolderName) 
cap = cv2.VideoCapture(video_name)

count_frame = 0                # 帧计数 
count_sample = 0               # 采样输出计数
count_first_nframe = 100       # 前n帧计数

while(cap.isOpened()):                            #  遍历整个文件夹
#while(cap.isOpened() and count_frame<100):       #  遍历前 nFrame

    ret, frame = cap.read()
    count_frame+=1
    
    if count_frame % sample_freq == 0:
        count_sample+=1
        path = './VideoSequence/'
        img_name = video_name[:5] + '_' + video_name[-12:-4] + '_' + str(count_sample) + '.jpg'
        cv2.imwrite(path + img_name, frame)

cap.release()
sample_freq = 150                        # 采样率
strfolderName = 'VideoSequence'          # 视频序列文件夹名称
video_name = '30531_钻台面_20190305.mp4' # 文件名
​
# 判断存在,创建新的数据集路径
isExists=os.path.exists('./'+ strfolderName)
if not isExists:
    os.mkdir('./' + strfolderName) 
cap = cv2.VideoCapture(video_name)
​
count_frame = 0                # 帧计数 
count_sample = 0               # 采样输出计数
count_first_nframe = 100       # 前n帧计数
​
while(cap.isOpened()):                            #  遍历整个文件夹
#while(cap.isOpened() and count_frame<100):       #  遍历前 nFrame
​
    ret, frame = cap.read()
    count_frame+=1
    
    if count_frame % sample_freq == 0:
        count_sample+=1
        path = './VideoSequence/'
        img_name = video_name[:5] + '_' + video_name[-12:-4] + '_' + str(count_sample) + '.jpg'
        cv2.imwrite(path + img_name, frame)
​
cap.release()