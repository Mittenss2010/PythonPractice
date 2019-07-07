import numpy as np
import cv2
cap=cv2.VideoCapture('001.mp4')                #文件名及格式

frameCount = 0

while(True):
	#capture frame-by-frame
    ret , frame = cap.read()
    frameCount+=1
    #if frameCount%30 == 0 and frameCount<15000:
    print(frameCount)
    #cv2.imshow('frame', frame)
    cv2.imwrite(str(frameCount) + '.jpg',  frame)
    if cv2.waitKey(30) &0xFF == ord('q'):  #按q键退出
        break
#when everything done , release the capture
cap.release()
cv2.destroyAllWindows()

print(frameCount)