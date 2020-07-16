#导入相关库
import numpy as np
import os
import cv2
import shutil
from tqdm import tqdm

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

# 统计数据集中待平衡的类，目标数量
# 根据新数据随机抽取一定量的目标数据
# 对这些目标数据中对应的目标进行擦除

def erasure_label(filename, filePath, filePath_new, classname):
    """
        Parse xml file and return labels.
        功能：解析xml，并根据字典中的项目来修订图像,并删除xml中对应的目标
        参数：xml名
             picPath
             picPath_new
    """
    pic_path = filePath + filename[:-4] + '.jpg'              # 图像路径
    pic_path_new = filePath_new + filename[:-4] + '.jpg'
    img = cv2.imread(pic_path)                             

    anno_path = filePath + filename
    tree = ET.parse(anno_path)
    root = tree.getroot()

    for obj in root.findall('object'):                      # 使用list not iter  
        cls_name = obj.find('name').text.strip().lower()    # 获取classname
        if cls_name == classname:
            # 提取坐标信息
            bndbox = obj.find('bndbox')
            xmin = bndbox.find('xmin').text.strip().lower()
            ymin = bndbox.find('ymin').text.strip().lower()
            xmax = bndbox.find('xmax').text.strip().lower()
            ymax = bndbox.find('ymax').text.strip().lower()
            img[int(ymin):int(ymax),int(xmin):int(xmax)] = (0,0,0)
            # 移除相应的xml元素
            
            
    cv2.imwrite(pic_path_new,img)



if __name__ == "__main__":


    dirname = 'test_img/'

    originPath = 'G:/[NOW]cqsy_collection/PythonPractice/tools/ignore_files/'

    file_PathNew = originPath + dirname[:-1] + '_PathNew/'
    if not os.path.exists(file_PathNew):
       os.mkdir(file_PathNew)
    
    filePath = originPath + dirname
    for filename in tqdm(os.listdir(filePath)):
        if filename[-4:] == '.xml':
            erasure_label(filename, filePath, file_PathNew, 'bxingdiaoqian')
            break