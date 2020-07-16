import os
import shutil
import json


info_list = []

unit_dict = {}
scene_dict = {}
lightstate_dict = {}
weahter_dict = {}
content_dict = {}
date_dict = {}


info_list.append(unit_dict)
info_list.append(scene_dict)
info_list.append(lightstate_dict)
info_list.append(weahter_dict)
info_list.append(content_dict)
info_list.append(date_dict)


path = 'Samples_all_data-191218_32532.json'


with open(path,'r') as load_f:
    load_dict = json.load(load_f)
    all_data_num = len(load_dict)
    print('共载入文件：' + str(all_data_num) + '个')


# 获取每个维度，每种状态的数据个数
for index, item in enumerate(load_dict):
    elementdata = load_dict[item][:-4].split('_')

    for index, item in enumerate(info_list):
        if elementdata[index] not in info_list[index]:
            info_list[index][elementdata[index]] = 0
        info_list[index][elementdata[index]] += 1


# 打印输出每个dict各自的数据比例
# 各个井队数据比例
print('各井队数据比例*******************************************')
for item in info_list[0]:
    print(item + ':' + f'{info_list[0][item]/all_data_num:8.3%}')


print('各场景数据比例*******************************************')
for item in info_list[1]:
    print(item + ':' + f'{info_list[1][item]/all_data_num:8.3%}')


print('各时段数据比例*******************************************')
for item in info_list[2]:
    print(item + ':' + f'{info_list[2][item]/all_data_num:8.3%}')


print('各天气数据比例*******************************************')
for item in info_list[3]:
    print(item + ':' + f'{info_list[3][item]/all_data_num:8.3%}')


print('各内容数据比例*******************************************')
for item in info_list[4]:
    print(item + ':' + f'{info_list[4][item]/all_data_num:8.3%}')



# 获取各个场景的10个数据，计算总的数据量


def print_combindict():
    for index, item in enumerate(scence_dict):
        #可视化打印方式 
        print('\t' + str(index+1) + '队伍_时段_天气_作业:' + item + ':' 
                   + str(scence_dict[item])+ ' '+ ' %'*scence_dict[item])
    






# # bugs fix
# 从原始数据库中调出命名出现问题的项，进行重命名，再加入数据库
# fileList=[]
# for index, item in enumerate(load_dict):
#     elementdata = load_dict[item][:-4].split('_')
#     if len(elementdata)==6:
#         fileList.append(load_dict[item])
# print(fileList)


# path = './all_data-191207_32532/'
# samples_dict = {}
# for unit_index, unit in enumerate(os.listdir(path)):
#     for files_index, file in enumerate(os.listdir(path + unit)):
#         if file[-4:] == '.xml':
#             if file in fileList:
#                 shutil.move(path + unit + '/' + file, './bugfiles/' + file)
#                 shutil.move(path + unit + '/' + file[:-4] + '.jpg', './bugfiles/' + file[:-4] + '.jpg')

#                 # key = unit + '_' + str(files_index//2+1)
#                 # samples_dict[key] = file
#                 # print(key)