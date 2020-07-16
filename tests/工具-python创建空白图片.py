# python-opencv创建空白图片(背景颜色自定义)


# 在python使用opencv的过程中常常需要新建空白图片，
# 官方没有直接的解决方案，
# 使用如下方法即可轻松创建空白图片，背景颜色自定义。

import numpy as np
import cv2

# 使用Numpy创建一张A4(2105×1487)
img = np.zeros((2105,1487,3), np.uint8)

# 使用白色填充图片区域,默认为黑色
img.fill(255)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()