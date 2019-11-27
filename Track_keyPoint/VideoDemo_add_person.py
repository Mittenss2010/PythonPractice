from __future__ import division                        # 2.7中默认的整数除法是地板除，而导入了__future__之后，就是精确除了
import argparse, time, logging, os, math, tqdm, cv2    # 导入外围模块

import numpy as np


import matplotlib.pyplot as plt

# 构造视频相关参数
video_path = './ignore_video/002.mp4'
cap = cv2.VideoCapture(video_path)                # 文件名及格式
# time.sleep(1)                                     # 原为摄像头拍摄 letting the camera autofocus
axes = None
num_frames = 1000
person01 = cv2.imread('./ignore_video/persons/person01.jpg')

width = person01.shape[0]
height = person01.shape[1]

# print(person01.shape[0])
# print(person01.shape[1])


for i in range(num_frames):

    print("当前是第：" + str(num_frames))
    ret, frame = cap.read()
    num_frames+=1

    # person01.jpg
    frame[100:100+width, 100:100+height] = person01     # wh
    
    # cv2.imwrite()
    cv2.imshow("img", frame)
    cv2.waitKey(50)

cap.release()