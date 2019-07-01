import sys
sys.path.append('../')                       # 添加模块导入路径


if __name__ == "__main__":

# 构造list
    testList = []
    for i in range(10):
        testList.append([i, i+1])
    print(testList)

# 通过list构造字典
    testDict = {}
    for item in testList:
        testDict[item[0]] = item[1]

    print(testDict)


# 测试python，最大count
# 测试多模型，显卡预测
# 测试