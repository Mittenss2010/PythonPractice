import os
import shutil
import time

# 不同文件夹数据，文件重名处理

xmlsPath = './165/'
xmlsPath_new = './new/'

if not os.path.exists(xmlsPath_new):
    os.mkdir(xmlsPath_new)

address = '50627_'
sub_address = 'ZTM_'

# 统计xml文件名称字典
temp = {}
temp_set = set()
for filename in os.listdir(xmlsPath):
    if filename[-4:] == '.xml':
        temp_set.add(filename[:-4] + '.jpg')
        # temp[filename[:-4] + '.jpg'] = 1

# 找jpg是否在xml文件中
for filename in os.listdir(xmlsPath):
    if filename[-4:] == '.jpg':
        if filename in temp_set:
            now = time.strftime('%Y-%m-%d-%H-%M-%S_',time.localtime(time.time()))
            newPath = xmlsPath_new + address + sub_address + now
            shutil.copy(xmlsPath + filename[:-4] + '.xml', newPath + filename[:-4] + '.xml')
            shutil.copy(xmlsPath + filename, newPath + filename)
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