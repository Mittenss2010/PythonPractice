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
    for key, value in B.items():
        if key in A:
            A[key] += value
        else:
            A[key] = value

def get_labels(anno_path):
    tree = ET.parse(anno_path)        
    root = tree.getroot()
    classnames = {}                                        
    for obj in root.iter('object'):
        cls_name = obj.find('name').text.strip().lower()   
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

    for index, item in enumerate(sorted(class_names_dict, key=class_names_dict.get, reverse = True)):
        #print(item, class_names_dict[item])
        precent = class_names_dict[item]/total_count*100
        print(item + ',')
        print(str(index+1) +'_' +  item + ': ' + format(precent, '.4f') + '%')

def return_classnames_list(Path):
    f = open(Path, 'r')                   
    classnames_list = list()
    for line in f.readlines():                          
        line = line.strip()                             
        if not len(line) or line.startswith('#'):       
            continue                                    
        classnames_list.append(line)                    
    return classnames_list

if __name__ == "__main__":

    xmlsPath = 'G:/@@@@Now_DataPro/0323_labels/temp_ch2/'

    # names_Path = 'F:/数据集版本管理/Mix_base_test_40656/voc.names'

    # classnames_list = return_classnames_list(names_Path)
    class_names_dict = {}
    # 针对单个文件夹
    for item in tqdm(os.listdir(xmlsPath)):
        if item[-4:] == '.xml':
            #print(xmlsPath + item)
            union_dict(class_names_dict, get_labels(xmlsPath + item))

    statistic_obj(class_names_dict)