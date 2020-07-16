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



def delete_obj_inclsname(filepath):
    '''
        删除指定类别的标记框
        # 传入-文件，类别
        # 传出-文件
    '''
    tree = ET.parse(path_filename)
    root = tree.getroot()

    for obj in root.findall('object'):
        cls_name = obj.find('name').text.strip().lower()        # 获取 classname
        if cls_name == 'anquanlian':
            root.remove(obj)
        if cls_name == 'zhuanpan             static':                         # 模板类中要添加到目标文件夹的节点
            root.remove(obj)
        if cls_name == 'yeqidaqian_close     static':
            root.remove(obj)
        if cls_name == 'yeqidaqian           static':                         # 模板类中要添加到目标文件夹的节点
            root.remove(obj)
        if cls_name == 'diaoqia              static':                         # 模板类中要添加到目标文件夹的节点
            root.remove(obj)
        if cls_name == 'gunzifangbuxin              static':                         # 模板类中要添加到目标文件夹的节点
            root.remove(obj)

    tree.write(path_filename, "UTF-8")

if __name__ == "__main__":
    xmlsPath = 'G:/@@20200714/005-aql_no/'

    for filename in tqdm(os.listdir(xmlsPath)):
        if filename[-4:] == '.xml':
            path_filename = xmlsPath + filename
            delete_obj_inclsname(path_filename)

