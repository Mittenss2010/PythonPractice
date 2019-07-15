#导入相关库
import numpy as np
import os
import shutil

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

'''
    字典：要修改的旧，新名称
'''
classnames_dict = {
            'yeqidaqian_close':'yeqidaqian_close',
            'roi_zhuan_pan':'zhuanpan_roi',
            'anquanlian':'anquanlian_no'
            }


def rename_label(anno_path):
    """
        Parse xml file and return labels.
        解析xml，并根据字典中的项目来修订新的名称
    """
    tree = ET.parse(anno_path)
    root = tree.getroot()

    for obj in root.iter('object'):
        cls_name = obj.find('name').text.strip().lower()   # 获取classname
        cls_name = classnames_dict[cls_name]               # 更新classname
        obj.set('name',cls_name)

        if cls_name not in classnames_dict:
            continue
    tree.write('output.xml', "UTF-8")


if __name__ == "__main__":
    for i in os.list:   
        print(rename_label('test.xml'))