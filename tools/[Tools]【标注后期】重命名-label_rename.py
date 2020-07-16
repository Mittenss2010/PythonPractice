#导入相关库
import numpy as np
import os
import shutil
from tqdm import tqdm

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET



def rename_label(filename, xmlsPath):
    """
        Parse xml file and return labels.
        解析xml，并根据字典中的项目来修订新的名称
    """
    anno_path = xmlsPath + filename
    tree = ET.parse(anno_path)
    root = tree.getroot()

    for obj in root.findall('object'):                      # 使用list not iter  
        cls_name = obj.find('name').text.strip().lower()    # 获取classname
        if cls_name == 'anquanlian					 static':
            obj.find('name').text = 'anquanlian'
        if cls_name == 'yusan				 static':
            obj.find('name').text = 'yusan'

    tree.write(anno_path, "UTF-8")


if __name__ == "__main__":


    xmlsPath = 'G:/@@20200714/static/'
    for filename in tqdm(os.listdir(xmlsPath)):
        if filename[-4:] == '.xml':
            rename_label(filename, xmlsPath)
