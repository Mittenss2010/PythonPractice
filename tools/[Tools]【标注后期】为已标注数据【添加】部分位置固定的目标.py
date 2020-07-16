#导入相关库
import numpy as np
import os
import shutil
from tqdm import tqdm

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


# detection中的类别属性
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

    xmlsPath_new = 'G:/@@20200714/005-aql_no/'# 要修改的文件夹名称
    xmlPath = 'G:/@@20200714/001.xml'  # 模板文件路径

    nameList = []                    
    tree = read_xml(xmlPath)
    objects = find_nodes(tree, "object")

    for filename in os.listdir(xmlsPath_new):
        if filename[-4:] == '.xml':
            path_filename = xmlsPath_new + filename
            tree_new = read_xml(path_filename)
            root = tree_new.getroot()

            # 提取目标框对象
            # 遍历objs，找到对应名称的 obj，加入objs new
            target_objs = []                                                    # 待添加目标obj
            for obj in objects:                                     # 
                cls_name = obj.find('name').text.strip().lower()    # 获取 classname
                # if cls_name == 'zhuanpan':                         # 模板类中要添加到目标文件夹的节点
                #     target_objs.append(obj)
                # if cls_name == 'anquanlian_no':                         # 模板类中要添加到目标文件夹的节点
                #     target_objs.append(obj)
                # if cls_name == 'yeqidaqian_close':                         # 模板类中要添加到目标文件夹的节点
                #     target_objs.append(obj)
                # if cls_name == 'yeqidaqian':                         # 模板类中要添加到目标文件夹的节点
                #     target_objs.append(obj)
                # if cls_name == 'gunzifangbuxin':                         # 模板类中要添加到目标文件夹的节点
                #     target_objs.append(obj)
                if cls_name == 'diaoqia':                         # 模板类中要添加到目标文件夹的节点
                    target_objs.append(obj)
            print(target_objs)

            for item in target_objs:
                root.insert(6, item)      # obj位置上添加元素
            print(path_filename)
            tree_new.write(path_filename, "UTF-8")

