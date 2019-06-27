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


if __name__ == "__main__":

    testList = []
    for i in range(10):
        testList.append([i, i+1])
    print(testList)

    testDict = {}
    for item in testList:
        testDict[item[0]] = item[1]

    print(testDict)


# 测试python，最大count

# 测试多模型，显卡预测

# 测试