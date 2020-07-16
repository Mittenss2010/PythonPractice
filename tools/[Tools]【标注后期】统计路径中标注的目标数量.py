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
        print("目标-" + item + ":" + str(class_names_dict[item]) + " 个")
    print("当前路径目标总数量：" + str(total_count))

    # for item in class_names_dict:                         # 计算百分比
    #     total_count
    #     precent = class_names_dict[item]/total_count*100
    #     print(item + ': ' + format(precent, '.2f') + '%')
    
if __name__ == "__main__":

    xmlpath = 'G:/@@@@Now_DataPro/00000/'
    # 字典合并
    class_names_dict = {}
    for item in os.listdir(xmlpath):
        if item[-4:] == '.xml':
            #print(item)
            union_dict(class_names_dict, get_labels(xmlpath + item))
    statistic_obj(class_names_dict)

