#导入相关库
import numpy as np
import os
import shutil

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

    for item in class_names_dict:                         # 计算百分比 
        precent = class_names_dict[item]/total_count*100
        print(item + ': ' + format(precent, '.2f') + '%')

if __name__ == "__main__":
    # xmlpath = './ignore_files/xmls/'
    # xmlpath = 'D:/windows_v1.8.1/【数据】智能行为识别仪/【数据】异常行为识别 300张-第4批/TEMP/'
    # xmlpath = 'G:/cqsy_collection/2019-07-16-mix/'
    
    #xmlpath = 'G:/cqsy_collection/2019-07-16-mix/'
    xmlpath = 'G:/cqsy_collection/数据标注管理/2019-07-16-mix-624(me 已改名)/'
    # xmlpath = 'G:/cqsy_collection/数据标注管理/newXmls/'

    # 字典合并
    class_names_dict = {}
    for item in os.listdir(xmlpath):
        if item[-4:] == '.xml':
            #print(xmlpath + item)
            union_dict(class_names_dict, get_labels(xmlpath + item))
    statistic_obj(class_names_dict)

