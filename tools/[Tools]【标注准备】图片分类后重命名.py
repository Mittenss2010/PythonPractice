'''
视频序列化
打印视频的文件属性
配置视频序列化的采集属性

'''

import numpy as np
import cv2
import os
import time
import shutil


# video_path = 'D:/windows_v1.8.1/【数据】智能行为识别仪/【数据】行为识别-第5批/hiv00010.mp4'

imageSavePath = 'G:/data/YeqidaqianWorking/'
address = '50627_'
# sub_address = 'QJ_'
# sub_address = 'ZTM_'
sub_address = 'SZF_'
scene = 'YeqidaqianWorking'

imagesNewPath = './New_' + scene + '/'

if not os.path.exists(imagesNewPath):
    os.mkdir(imagesNewPath)


for filename, index in enumerate(os.listdir(imageSavePath)):

    shutil.move(imageSavePath + filename,imagesNewPath )
    print(filename)
    print(index)

    # now = time.strftime('%Y-%m-%d-%H-%M-%S_',time.localtime(time.time()))
    # savePath = imageSavePath + address + sub_address + now + str(frameCount) + '.jpg'

