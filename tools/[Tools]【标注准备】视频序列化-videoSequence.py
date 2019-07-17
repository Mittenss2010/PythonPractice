'''
视频序列化
打印视频的文件属性
配置视频序列化的采集属性

'''

import numpy as np
import cv2
import os
import time


def print_cap_prop(cap):
    '''
    打印显示视频的部分属性信息
    '''
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))   

    print("分辨率：" + str(width), str(height))
    print("帧率：" + str(fps))
    print("总帧数：" + str(total_frames))

# video_path = 'D:/windows_v1.8.1/【数据】智能行为识别仪/【数据】行为识别-第5批/hiv00010.mp4'
video_path = '2019年7月16日 182207(50627)钻台面数据表演Clip.mp4'

imageSavePath = './01/'
address = '50627_'
sub_address = 'ZTM_'


cap=cv2.VideoCapture(video_path)        #文件名及格式
print_cap_prop(cap)                   # 打印属性信息
frameCount = int(cap.get(cv2.CAP_PROP_POS_FRAMES))    # 初始化帧号
sampleRate = int(cap.get(cv2.CAP_PROP_FPS))          # 视频采样率，每秒采集1frame 
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))   

while(frameCount<total_frames):
    ret , frame = cap.read()
    frameCount = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    #cv2.imshow('frame', frame)
    if frameCount % sampleRate == 0:
        if not os.path.exists(imageSavePath):
            os.mkdir(imageSavePath)
        now = time.strftime('%Y-%m-%d-%H-%M-%S_',time.localtime(time.time()))
        savePath = imageSavePath + address + sub_address + now + str(frameCount) + '.jpg'
        cv2.imwrite(savePath, frame)
        print(savePath)
        print("帧存储index：" + str(frameCount))
        
        #break
    # if cv2.waitKey(30) &0xFF == ord('q'):  #按q键退出
    #     break

#when everything done , release the capture
cap.release()
cv2.destroyAllWindows()
