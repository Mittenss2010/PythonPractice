#导入相关库
import numpy as np
import os
import shutil
from tqdm import tqdm

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


def union_dict(A, B):
    '''
        字典合并值相加

    '''
    for key, value in B.items():
        if key in A:
            A[key] += value
        else:
            A[key] = value

def get_labels(anno_path):
    """
        Parse xml file and return labels.
        解析xml，获取class名称，及个数
        class 1:1
        class 2:5
        class 3:1
        class 4:5
        返回字典：{ 'classname': num, ...}
    """
    tree = ET.parse(anno_path)        #, "UTF-8"
    root = tree.getroot()
    classnames = {}                                        # 统计classnames 及 num
    for obj in root.iter('object'):
        cls_name = obj.find('name').text.strip().lower()   # 获取classname
        if cls_name not in classnames:
            classnames[cls_name] = 1
        else:
            classnames[cls_name] +=1
    return classnames

def statistic_obj(class_names_dict):
    total_count = 0
    for item in class_names_dict:
        total_count += class_names_dict[item]             # 计算目标总数
        
    print(total_count)


# from collections import defaultdict 
# d = defaultdict(int)
# for w in text.split():   
#     d[w] += 1

# 然后你可以得到一个单词列表，按照使用频率sorted(d, key=d.get)排序 - 排序迭代字典键，使用单词出现次数作为排序键。

# for w in sorted(d, key=d.get, reverse=True):   
#     print w, d[w]

    for index, item in enumerate(sorted(class_names_dict, key=class_names_dict.get, reverse = True)):
        #print(item, class_names_dict[item])
        precent = class_names_dict[item]/total_count*100
        print(str(index+1) +'_' +  item + ': ' + format(precent, '.4f') + '%')

    # # 字典值排序
    # for item in class_names_dict:                         # 计算百分比 
    #     precent = class_names_dict[item]/total_count*100
    #     print(item + ': ' + format(precent, '.2f') + '%')

def return_classnames_list(Path):
    f = open(Path, 'r')                   #以读方式打开文件
    classnames_list = list()
    for line in f.readlines():                          #依次读取每行
        line = line.strip()                             #去掉每行头尾空白
        if not len(line) or line.startswith('#'):       #判断是否是空行或注释行
            continue                                    #是的话，跳过不处理
        classnames_list.append(line)                             #保存
    return classnames_list

if __name__ == "__main__":


    # xmlsPath = 'G:/data/40656-数据集/【接收】/20190813-no/chouyan/'
    xmlsPath = 'F:/数据集版本管理/20190914_datasets/tmp'
    names_Path = 'F:/数据集版本管理/20190914_datasets/voc.names'
    
    classnames_list = return_classnames_list(names_Path)
    class_names_dict = {}
    
    # 针对单个文件夹
    for item in tqdm(os.listdir(xmlsPath)):
        if item[-4:] == '.xml':
            #print(xmlsPath + item)
            union_dict(class_names_dict, get_labels(xmlsPath + item))
    statistic_obj(class_names_dict)
    
    for item in class_names_dict:
        if item not in classnames_list:
            print('不在类目录中的类名：' + item)
    
    #针对多个层级
    # dirPath = 'G:/datasets-7018/'
    # trainxmls = 'train/labels/'
    # testxmls = 'val/labels/'

    # xmlsPath = dirPath + trainxmls
    # for item in tqdm(os.listdir(xmlsPath)):
    #     if item[-4:] == '.xml':
    #         #print(xmlsPath + item)
    #         union_dict(class_names_dict, get_labels(xmlsPath + item))
   
    # xmlsPath = dirPath + testxmls
    # for item in tqdm(os.listdir(xmlsPath)):
    #     if item[-4:] == '.xml':
    #         #print(xmlsPath + item)
    #         union_dict(class_names_dict, get_labels(xmlsPath + item))
    # statistic_obj(class_names_dict)