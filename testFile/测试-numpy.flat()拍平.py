import sys
sys.path.append('../')                       # 添加模块导入路径

import cv2
import numpy as np

if __name__ == "__main__":
# 测试   img.flat         # 返回数组的一维迭代器
# 将100*2的列表数据，表达为200*1
    testData = np.array([range(100),range(100)]) 
    print(testData.shape)            # 返回数组shape
    print(testData[0])               # 获取[0]维度的数据
    print(testData.flat[0])          # 返回数组的一维迭代器
    print(testData.flat[99])         # 返回数组的一维迭代器
    print(testData.flat[100])        # 数据拍平，一维线性化
    print(testData.flat[199])        # 数据拍平，一维线性化

    # 根据Net（X）输出进行结果分析2019年6月23日 18:17:04

    # for item in net(x):
    # # print('item')                       # 网络原始输出（1*100*1）（1*100*1）（1*100*4）
    # print(item)                           # 为什么输出多一维？？
    # # print(item.shape)
    # # print(item.dtype)        

    # print('item[0]********************')  # 网络降维输出（100*1）（100*1）（100*4）
    # print(item[0].asnumpy() )             # 降维，并转为Numpy
    # print(item[0].shape)                  
    # print(item[0].dtype)    