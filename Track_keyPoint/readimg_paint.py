import cv2
import numpy as np

img = cv2.imread('./ignore_video/001.jpg')

height = img.shape[0]
width = img.shape[1]

# person = src[200:300, 200:400]
img[xmin:xmax, ymin:ymax] = (0,0,255)
img[500:600, 600:700] = (0,0,255)
# mask = np.ones([height+2, width+2, 1], np.uint8)
# mask[500:600, 500:600] = 0

# cv2.floodFill(img, mask, (500, 500), (255 ,255, 255), cv2.FLOODFILL_MASK_ONLY)

cv2.imshow('show', img)
cv2.waitKey(0)