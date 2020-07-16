import os
import shutil
import time
import random

if __name__ == "__main__":

    # 重命名方法：
    # 将队号，场景，时间，天气，作业等高度一致或相似的内容移至tmp文件夹
    path = 'G:/【@@日常工作区】/20191203-数据标注文件批量改名/tmp/'                         # 【根据本地路径修改】
    path_new = 'G:/【@@日常工作区】/20191203-数据标注文件批量改名/tmp_new/'                 # 【根据本地路径修改，tmp_new和tmp同级目录】
    if not os.path.exists(path_new):
        os.mkdir(path_new)

    # 根据tmp文件夹中的相似场景内容对文件前缀进行命名
    # 井队_场景_日(夜)_天气_作业_时间.mp4
    newname_prifix = '40656_ZTM_Ye_Qing_XiaZuan_BiaoYan_20190409_'                      # 【根据场景内容修改】

    for item in os.listdir(path):
        if item[-4:] == '.xml':
            id = str(time.time()).split('.')[0] + str(time.time()).split('.')[1]            # 新文件名后缀id
            newname = newname_prifix + id                                       # 新文件名
            shutil.move(path + item, path_new + newname + '.xml')
            shutil.move(path + item[:-4] + '.jpg', path_new + newname + '.jpg')
            print(newname)
        