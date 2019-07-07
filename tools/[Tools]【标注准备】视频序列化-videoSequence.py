'''
视频序列化
打印视频的文件属性
配置视频序列化的采集属性

'''

import numpy as np
import cv2


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

    
cap=cv2.VideoCapture('ok.mp4')        #文件名及格式
print_cap_prop(cap)                   # 打印属性信息
frameCount = int(cap.get(cv2.CAP_PROP_POS_FRAMES))    # 初始化帧号
sampleRate = int(cap.get(cv2.CAP_PROP_FPS))          # 视频采样率，每秒采集1frame 
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))   

while(frameCount<total_frames):
    ret , frame = cap.read()
    frameCount = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    #cv2.imshow('frame', frame)
    if frameCount % sampleRate == 0:
        cv2.imwrite(str(frameCount) + '.jpg',  frame)
        print("帧存储index：" + str(frameCount))

    if cv2.waitKey(30) &0xFF == ord('q'):  #按q键退出
        break

#when everything done , release the capture
cap.release()
cv2.destroyAllWindows()
