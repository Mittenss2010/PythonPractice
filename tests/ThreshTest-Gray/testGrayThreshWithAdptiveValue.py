
import cv2
import numpy as np
import time

for i in range(25):
    filename = "test" + str(i) + ".jpg"
    imgGray = cv2.imread(filename ,0)


    # 计算平均灰度值
    start = time.time()
    print(imgGray.mean(0).mean())

    print('TimeCost :****     '+ str(round( time.time() - start, 4))+ ' S')

    cv2.imshow('image',imgGray)

    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
