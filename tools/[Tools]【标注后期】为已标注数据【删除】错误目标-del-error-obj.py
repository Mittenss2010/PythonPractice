import numpy as np
import os
import shutil
from tqdm import tqdm
import xml.etree.cElementTree as ET

def read_xml(in_path):
    tree = ET.parse(in_path)
    return tree

def find_nodes(tree, path):
    return tree.findall(path)


def delete_obj_inclsname(filepath, classname):
    '''
        删除指定类别的标记框
        # 传入-文件，类别
        # 传出-文件
    '''
    count = 0
    tree = ET.parse(path_filename)
    root = tree.getroot()

    for obj in root.findall('object'):
        cls_name = obj.find('name').text.strip().lower()        # 获取 classname
        if cls_name == classname:
            root.remove(obj)
            count+=1
            
    tree.write(path_filename, "UTF-8")
    return count

if __name__ == "__main__":
    xmlsPath = 'G:/@@label_obj/video-out-0527/'
    xmlsPath = 'G:/@@label_obj/50699_2020-05-29AnquanlianNo_/temp/'

    ## yeqidaqian
    ## yeqidaqian_close
    count = 0
    for filename in tqdm(os.listdir(xmlsPath)):
        if filename[-4:] == '.xml':
            path_filename = os.path.join(xmlsPath, filename)
            count += delete_obj_inclsname(path_filename, 'zhuanpan')
    print('共移除对象{}个'.format(count))