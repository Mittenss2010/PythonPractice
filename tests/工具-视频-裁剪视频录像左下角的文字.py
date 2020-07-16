import cv2
#from gluoncv import model_zoo, data, utils
import os

path = './Video/'
for item in os.listdir(path):
    filepath = path + item
    videoCapture = cv2.VideoCapture(filepath)
    width,height = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), 
            int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print(width,height)
    #读帧
    success, frame = videoCapture.read()
    cropped = frame[int(height/9*8):height, 0:int(width/3)]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite(item[:-4] + '.jpg', cropped)
    videoCapture.release()

