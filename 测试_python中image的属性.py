import cv2
import numpy as np

if __name__ == "__main__":
    
    # 标准的属性列表*************************************************************
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