import os
import shutil
import time

# 不同文件夹数据，文件重名处理

xmlsPath = './VOCdevkit/'
xmlsPath_new = './不成对的文件/'

if not os.path.exists(xmlsPath_new):
    os.mkdir(xmlsPath_new)


# 构建jpg集合与xml集合
xml_set = set()
jpg_set = set()
xml_list = []
jpg_list = []


for filename in os.listdir(xmlsPath):
    if filename[-4:] == '.xml':
        xml_list.append(filename[:-4])
        if filename[:-4] in xml_set:
                print(filename)
        xml_set.add(filename[:-4])


for filename in os.listdir(xmlsPath):
    if filename[-4:] == '.jpg':
        jpg_list.append(filename[:-4])
        if filename[:-4] in jpg_set:
                print(filename)
        jpg_set.add(filename[:-4])

print(len(xml_set))
print(len(jpg_set))
print(len(xml_list))
print(len(jpg_list))


# 输出两集合中不相同的元素
# print(xml_set.symmetric_difference(jpg_set))

tempSet = xml_set.symmetric_difference(jpg_set)
for item in tempSet:
    # print(item)
    if item not in xml_set:
        filename = item + '.jpg'
        shutil.move(xmlsPath + filename, xmlsPath_new + filename)
        print(filename)
    if item not in jpg_set:
        filename = item + '.xml'
        shutil.move(xmlsPath + filename, xmlsPath_new + filename)
        print(filename)


# temp = {}
# for filename in os.listdir(xmlsPath):
#     if filename[-4:] == '.jpg':
#         temp[filename[:-4] + '.xml'] = 1

# # 找xml是否在jpg文件中
# for filename in os.listdir(xmlsPath):
#     if filename[-4:] == '.xml':
#         if filename not in temp:
#             shutil.move(xmlsPath + filename, xmlsPath_list[0] + filename)
#             print(filename)


    # 互相剔除xml，jpg文件，取交集
    # xmlsPath = 'G:/cqsy_collection/数据标注管理/data_0603/'
    # xmlsPath_list = getNewPath(xmlsPath, classnames_list)