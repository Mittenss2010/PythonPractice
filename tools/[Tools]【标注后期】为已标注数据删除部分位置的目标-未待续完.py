#导入相关库
import numpy as np
import os
import shutil
from tqdm import tqdm

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET





def read_xml(in_path):
    '''读取并解析xml文件
       in_path: xml路径
       return: ElementTree'''
    #tree = ET()
    tree = ET.parse(in_path)
    return tree


def find_nodes(tree, path):
    '''查找某个路径匹配的所有节点
       tree: xml树
       path: 节点路径'''
    return tree.findall(path)


if __name__ == "__main__":

    path = 'G:/cqsy_collection/cqsy_python_practice/tools/ignore_files/'
    xmlsPath_new = path + 'test_addobj_xmls'  + '/'                             # 要修改的文件夹名称
    # nameList = ['yeqidaqian','bxingdiaoqian']         # 模板类中要删除的节点
    nameList = ['bxingdiaoqian']         # 模板类中要删除的节点

    for filename in os.listdir(xmlsPath_new):
        if filename[-4:] == '.xml':
            path_filename = xmlsPath_new + filename
            tree_new = read_xml(path_filename)
            root = tree_new.getroot()

            target_objs = []                                                    # 待添加目标obj
            for obj in root.findall('object'):
                cls_name = obj.find('name').text.strip().lower()                # 获取 classname
                if cls_name in nameList:
                    root.remove(obj)
                    print(cls_name)
            print(path_filename)
            tree_new.write(path_filename, "UTF-8")
