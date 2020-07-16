
## 查找轮廓，打印轮廓数据结构
import cv2 

img = cv2.imread('003.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(binary, 3, 2)


for contour in contours:   ## 多个轮廓
    for item in contour:   ## 一个轮廓
        print(item)
        print(item[0].dtype)
        print(item[0][0].dtype)

        cv2.putText(img, "(%d,%d)" % (item[0][0], item[0][1]), (item[0][0] + 2, item[0][1] + 2),  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        break

print(hierarchy)

## 以数字3的轮廓为例
# cnt = contours[0]  # 第一个轮廓
# print(cnt)
# cv2.drawContours(img, contours, -1, (0,0,255), 3)  


## M中包含了很多轮廓的特征信息，
# 比如M['m00']表示轮廓面积，与前面cv2.contourArea()计算结果是一样的。
# 质心也可以用算：

## 计算质心
cnt = contours[0]  # 取第一个轮廓
print(cnt)
M = cv2.moments(cnt)
cx, cy = M['m10'] // M['m00'], M['m01'] // M['m00']  # (205, 281)
center = (int(cx), int(cy))
print(center)

cv2.circle(img, center, 2, (255,0,0), thickness=2, lineType=8, shift=0)


## 匹配Hu矩，和计算矩关系不大
print(cv2.matchShapes(cnt, cnt, 1, 0.0))  # 0.0


cv2.imshow('img', img)
cv2.waitKey(0)