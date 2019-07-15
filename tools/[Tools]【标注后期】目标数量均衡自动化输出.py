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

class ObjectBalanceTools():
    '''
        数据均衡工具类

    '''
    def __init__(self,xmlsPath):
        self.xmlsPath = xmlsPath
        #self.get_xmlsPath(xmlsPath)
        pass

    def get_xmlsPath(self, xmlsPath):
        for item in os.listdir(xmlpath):
            if item[-4:] == '.xml':
                print(item)

    def get_labels(self, anno_path):
        """
            功能：解析xml，获取class名称，及个数
            返回：字典：{ 'classname': num, ...}
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

    def delete_label(self, anno_path, class_name):
        '''
        解析：xml，删除指定 class_name 名称
        返回：新的xml
        '''
        count=0
        tree = ET.parse(anno_path)                              #, "UTF-8"
        root = tree.getroot()
        classnames = {}                                         # 统计classnames 及 num
        for obj in root.iter('object'):
            cls_name = obj.find('name').text.strip().lower()    # 获取classname
            if cls_name == class_name:
                root.remove(obj)
                count+=1

        # print()
        dirName = anno_path.split('/')[-2]
        fileName = anno_path.split('/')[-1]
        originPath = anno_path[:-len(fileName + dirName)-2]
        outputPath = originPath + '/newXmls/'
        if not os.path.exists(outputPath):
            os.mkdir(outputPath)
        
        print(outputPath)
        print("移除：" + class_name + ' ' + str(count) + ' 个')

        tree.write(outputPath + fileName, "UTF-8")
        return classnames



# 数据自动化均衡
if __name__ == "__main__":
    xmlpath = './ignore_files/xmls/'
    xmlpath = 'G:/cqsy_collection/cqsy_python_practice/tools/ignore_files/xmls/'

    objBalanceTools = ObjectBalanceTools(xmlpath)


    # 字典合并
    # class_names_dict = {}
    # for item in os.listdir(xmlpath):
    #     if item[-4:] == '.xml':
    #         print(item)
    #         delete_label(xmlpath + item, 'diao_qia')
    # print(class_names_dict)
    # delete_label(xmlpath, 'diao_qia')
    # 类名 + 系数字典 