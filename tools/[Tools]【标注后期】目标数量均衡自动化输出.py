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
        #self.get_xmlsPath(xmlsPath)
        self.xmlsPath = xmlsPath                      # 原始输入路径
        self.xmlsPath_new = self.get_xmlsPath_new()   # 新路径
        self.cur_classnames_dict = {}                 # 当前类目标数量字典

        pass

    def through_all_xmlsPath(self):
        for filename in os.listdir(self.xmlsPath):
            if filename[-4:] == '.xml':
                class_names = self.get_labels(self.xmlsPath + filename)

                # 判断是否有新的类别，若有加入新的类别，作为加入待选,加入待选后，必然导致不均衡
                classname_outof_dict = []                    
                for key in class_names:
                    if key not in self.cur_classnames_dict:
                        #print("classname_outof_dict-key:" + key)
                        classname_outof_dict.append(key)

                if len(classname_outof_dict) > 0:                        # 删除非列表中的项,并存储
                    self.delete_labels(filename, classname_outof_dict)
                    self.update_cur_classnames_dict()
                    continue                                           # branch one
                else:
                    # 没有新的类别，再计算类别的 max，min，
                    maxClassNameKey = max(self.cur_classnames_dict, key=self.cur_classnames_dict.get)
                    minClassNameKey = min(self.cur_classnames_dict, key=self.cur_classnames_dict.get)              # 
                    # 若新构造路径中数据不平衡
                    if self.cur_classnames_dict[minClassNameKey] < self.cur_classnames_dict[maxClassNameKey]:      # 最小的数量 < 最大数量
                        # 只更新最小数量的类别的信息，多余删除,并存储
                        minKeyList = []                                         # 提取所有minkey名称
                        for key in self.cur_classnames_dict:
                            if self.cur_classnames_dict[key] == self.cur_classnames_dict[minClassNameKey]:
                                minKeyList.append(key)
                        # 若文件中含有 minKeyList元素，删除所有非minKeyList元素，并存储。
                        if self.is_classnames_in_xml(filename, minKeyList):
                            self.delete_labels(filename, minKeyList)
                            self.update_cur_classnames_dict()
                            continue
                        else:
                           # 若文件中没有 minKeyList元素，跳过文件，到下一个
                            continue
                    # 若数据平衡
                    else:
                        shutil.copy(self.xmlsPath + filename, self.xmlsPath_new + filename)                        # 直接复制文件到
                        self.update_cur_classnames_dict()

    def is_classnames_in_xml(self, filename, classnames_list):
        anno_path = self.xmlsPath + filename
        xml_classnames_dict = self.get_labels(anno_path)
        
        flage = False                        
        for item in classnames_list:
            if item in xml_classnames_dict:     # 如果存在一项
                flage = True                    # 就说明包含由最小项
        return flage

    def update_cur_classnames_dict(self):
        '''
            更新新路径下，xmls的不同类型的数量字典
        '''
        class_names_dict = {}
        for item in os.listdir(self.xmlsPath_new):
            if item[-4:] == '.xml':
                #print(item)
                union_dict(class_names_dict, self.get_labels(self.xmlsPath_new + item))
        self.cur_classnames_dict = class_names_dict
        self.statistic_obj_in_Dict()

    def statistic_obj_in_Dict(self):
        total_count = 0
        for item in self.cur_classnames_dict:
            total_count += self.cur_classnames_dict[item]             # 计算目标总数
            print("目标-" + item + ":" + str(self.cur_classnames_dict[item]) + " 个")
        print("当前路径目标总数量：" + str(total_count))

    def get_xmlsPath_new(self):
        '''
            根据现有路径，构造存储输出文件的路径
        '''
        dirName = self.xmlsPath.split('/')[-2]
        originPath = self.xmlsPath[:-len(dirName)-2]
        new_path = originPath + '/newXmls/'
        # print(new_path)
        if not os.path.exists(new_path):
            os.mkdir(new_path)
        return new_path

    def get_xmlsPath(self, xmlsPath):
        '''
            遍历现有路径，输出路径下的文件
        '''
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

    def delete_labels(self, filename, class_names):
        '''
        功能：解析：xml，删除非 class_names(list)中的节点
        返回：新的xml
        '''
        anno_path = self.xmlsPath + filename
        tree = ET.parse(anno_path)                                 #, "UTF-8"
        root = tree.getroot()

        for obj in root.findall('object'):                      # 使用list not iter  
            cls_name = obj.find('name').text.strip().lower()    # 获取classname
            if cls_name not in class_names:
                root.remove(obj)
                print(obj)
        tree.write(self.xmlsPath_new + filename, "UTF-8")       # xml中写入中文

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

    def get_objDict(self, xmlsPath):
        '''
            功能：每次添加新的xml后，更新当前类比的统计字典
            参数：new xmls的path
            返回：new xmls的属性统计
        '''
        for item in os.listdir(xmlpath):
            if item[-4:] == '.xml':
                print(item)

# 数据自动化均衡
if __name__ == "__main__":
    # xmlpath = './ignore_files/xmls/'

    xmlpath = 'G:/cqsy_collection/cqsy_python_practice/tools/ignore_files/xmls/'

    objBalanceTools = ObjectBalanceTools(xmlpath)

    # objBalanceTools.get_xmlsPath_new()                             # 测试路径创建
    # objBalanceTools.update_cur_classnames_dict()                   # 测试统计刷新
    # listobj = ['gun_zi_fang_bu_xin', 'ye_qi_da_qian']              # 测试移除属性
    # objBalanceTools.delete_labels('50627_201809_172.xml', listobj)
    objBalanceTools.through_all_xmlsPath()

