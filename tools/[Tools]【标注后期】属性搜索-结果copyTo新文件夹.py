#导入相关库
import numpy as np
import os
import shutil
import time
from tqdm import tqdm 

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

'''
    列表：要搜索的属性列表
'''
classnames_list = [ 'a',
                    's',
                    'tushengduanjie_tou',
                    'gongie',
                    'shiutao',
                    'zuanguan_roi',
                    'bxdiaoqian',
                    'bxingdianqian',
                    'pangpenqi',
                    'anquanlian\\',
                    'anquanmao——red',
                    'shiutao'
                    ]

def get_xmls_cotainedlabel(filename, xmlsPath, classnames_list):
    """
        Parse xml file and return labels.
        解析xml，并根据字典中的项目来修订新的名称
    """

    anno_path = xmlsPath + filename
    tree = ET.parse(anno_path)
    root = tree.getroot()

    for obj in root.findall('object'):                      # 使用list not iter  
        cls_name = obj.find('name').text.strip().lower()    # 获取classname
        for item in classnames_list:
            if cls_name == item:
                father_Path = get_fatherPath(xmlsPath)
                newPath = father_Path + '/' + item + '/'
                if not os.path.exists(newPath):
                    os.mkdir(newPath)
                xmlnewPath = newPath + filename
                print(anno_path)
                print(xmlnewPath)
                shutil.move(anno_path, xmlnewPath)
                shutil.move(anno_path[:-4] + '.jpg', xmlnewPath[:-4] + '.jpg')
                #time.sleep(1)
                return 
                # 文件移动

def get_fatherPath(xmlsPath):
    dirName = xmlsPath.split('/')[-2]
    father_Path = xmlsPath[:-len(dirName)-2]
    return father_Path

def getNewPath(xmlsPath, classnames_list):
    newPathList = []

    father_Path = get_fatherPath(xmlsPath)

    for item in classnames_list:
        xmlsPath_new = father_Path + '/' + item + '/'
        #print(xmlsPath_new)
        if not os.path.exists(xmlsPath_new):
            os.mkdir(xmlsPath_new)
        newPathList.append(xmlsPath_new)
        print(xmlsPath_new)
    return newPathList


if __name__ == "__main__":


   # xmlsPath = 'G:/【cqsy_collection】/数据标注管理/1670/'
    # xmlsPath = 'G:/2019-07-21/'
    # xmlsPath = 'G:/300/'
    # xmlsPath = 'G:/2019-07-22/'
    xmlsPath = 'G:/Totrain-20190726/'

    xmlsPath_list = getNewPath(xmlsPath, classnames_list)

    for filename in tqdm(os.listdir(xmlsPath)):
        if filename[-4:] == '.xml':
            #print(filename)
            get_xmls_cotainedlabel(filename, xmlsPath, classnames_list)