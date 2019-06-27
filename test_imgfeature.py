#! /usr/bin/env python
# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : 
#   File name   : test.py
#   Author      : MQ
#   Created date: 2019-06-21 18:11:35
#   Description :
#
#================================================================

import sys
sys.path.append('../')                       # 添加模块导入路径


## class Layout_code_element 测试
# from rule import Layout_code_element

# if __name__ == "__main__":
#     lce = Layout_code_element('1','10')
#     print(lce.dir)
#     print(lce.length)

## class LayoutCode 测试
import cv2
import numpy as np

if __name__ == "__main__":
    
    # img = cv2.imread('test.jpg')   # numpy.ndarray 类型
    # # print(img)            三维数组
    # print(img.shape)        # 数组的形状
    # print(img.dtype)        # 数组元素的数据类型对象
    # print(img.size)         # 数组中元素个数  132*132*3
    # print(img.itemsize)     # 数组中单个元素的字节长度
    # print(img.data)         # <memory at 0x000001BA8D9FDE58>指向存放数组数据的python buffer对象
    # print(img.ndim)         # 数组的维度
    # print(img.flat)         # 返回数组的一维迭代器
    # print(img.nbytes)       # 数组中所有元素的字节长度
    # print(img.imag)         # 返回数组的虚部
    # print(img.real)         # 返回数组的实部

# 测试   img.flat         # 返回数组的一维迭代器
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