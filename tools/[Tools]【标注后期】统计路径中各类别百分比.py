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

    for item in sorted(class_names_dict, key=class_names_dict.get, reverse = True):
        #print(item, class_names_dict[item])
        precent = class_names_dict[item]/total_count*100
        print(item + ': ' + format(precent, '.2f') + '%')

    # # 字典值排序
    # for item in class_names_dict:                         # 计算百分比 
    #     precent = class_names_dict[item]/total_count*100
    #     print(item + ': ' + format(precent, '.2f') + '%')

if __name__ == "__main__":
    # xmlpath = './ignore_files/xmls/'
    # xmlpath = 'D:/windows_v1.8.1/【数据】智能行为识别仪/【数据】异常行为识别 300张-第4批/TEMP/'
    # xmlpath = 'G:/【cqsy_collection】/2019-07-16-mix/'
    
    #xmlpath = 'G:/【cqsy_collection】/2019-07-16-mix/'
    #xmlpath = 'G:/datasets-if/'
    #xmlsPath = 'G:/【cqsy_collection】/数据标注管理/【数据集】测试过的数据集/2019-07-19/'
    # xmlsPath = 'G:/【cqsy_collection】/数据标注管理/【数据集】测试过的数据集/2019-07-20-表演过的数据集-showatdoor/'
    # xmlsPath = 'G:/2019-07-21/'
    xmlsPath = 'G:/2019-07-22/'
    #xmlsPath = 'G:/20190722/'
    xmlsPath = 'G:/Totrain-20190726/'

   # xmlsPath = 'G:/【cqsy_collection】/数据标注管理/【已标注】接收的图片/2019-07-22/300/'
    # 字典合并
    class_names_dict = {}
    
    # 针对单个文件夹
    for item in tqdm(os.listdir(xmlsPath)):
        if item[-4:] == '.xml':
            #print(xmlsPath + item)
            union_dict(class_names_dict, get_labels(xmlsPath + item))
    statistic_obj(class_names_dict)


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