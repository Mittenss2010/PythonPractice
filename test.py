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
from rule import Layout_code_element
from rule import Layout_code_matrix

if __name__ == "__main__":

    obj_classes = ['yeqidaqian','bihemen','zhuanpan']
    prohibit_type = 0           # 缺位禁止
    check_class = 'bihemen'

    # 构造方位码矩阵
    # temp =  [[None,0,0],
    #         [0,None,0],
    #         [0,0,None]]

    element_Matrix = []
    element_list = []
    element_list.append(None)
    element_list.append(Layout_code_element('0','2'))
    element_list.append(Layout_code_element('4','1'))
    element_Matrix.append(element_list)

    element_list = []
    element_list.append(Layout_code_element('2','3'))
    element_list.append(None)
    element_list.append(Layout_code_element('3','3'))
    element_Matrix.append(element_list)

    element_list = []
    element_list.append(Layout_code_element('8','3'))
    element_list.append(Layout_code_element('8','3'))
    element_list.append(None)
    element_Matrix.append(element_list)

    lce = Layout_code_matrix(element_Matrix, obj_classes ,prohibit_type, check_class)
