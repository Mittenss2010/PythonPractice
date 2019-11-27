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

nameList = ['yeqidaqian','yeqidaqian_close','yeqidaqian_open','taoguanqian','zhuanpan',
            'shudongkou','shudongkou_open','gunzifangbuxin','diaoqia','diaoqia_xiaozi',
            'diaoquan','anquanqiawa','tisi_tou','zuantouhezi','bxingdiaoqian','tishengduanjie',
            'shengdiaozuanju','zuangan_tou','zuangan_ping','anquanlian','anquanlian_no','ren',
            'anquanmao','anquanmao_no','kouzhao','humujing','shoutao','shou','gongxie','tuoxie',
            'miehuoqi','huoguang','dianhanguang','dianhanmianzhao','dianhanshoutao','fanguangfu',
            'gouzuangan','qiaogangdajin','dunzheguani','banshou','shuiping','yusan','zhitui',
            'zhitui_wugangban','diaowu','wurenkongzhishi','youche','dagou','baoxiandai','xiehusi',
            'jiaodeng','qihulan','douzuanju','daiersai','budaiersai','shouzhualangan']            # 模板类中要删除的目标


if __name__ == "__main__":
    xmlsPath_new = 'F:/DetectionData/data_zhengli/ztm/'

    for filename in os.listdir(xmlsPath_new):
        if filename[-4:] == '.xml':
            path_filename = xmlsPath_new + filename
            tree_new = read_xml(path_filename)
            root = tree_new.getroot()

            for obj in root.findall('object'):
                cls_name = obj.find('name').text.strip().lower()                # 获取 classname
                if cls_name not in nameList:
                    root.remove(obj)
                    # print(cls_name)
            # print(path_filename)
            tree_new.write(path_filename, "UTF-8")

