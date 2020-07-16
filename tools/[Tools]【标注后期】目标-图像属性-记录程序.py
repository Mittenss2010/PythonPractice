import json
import os
from tqdm import tqdm

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET



def getObjInfo(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()

    obj_info = []
    # key:目标局部id
    # value:目标类别
    for obj in root.findall('object'):    # 使用 obj list
        cls_name = obj.find('name').text.strip().lower()    # 获取classname
        obj_info.append(cls_name)
    return obj_info


# key：index
# value：图像名称_目标名称_目标局部id
# 检索路径，构建dict
dirname = 'all_data-191218_32532'

obj_dict = {}
path = os.path.join(dirname)
for unit_index, unit in tqdm(enumerate(os.listdir(path))):
    files_path = os.path.join(path, unit)
    for files_index, files in enumerate(os.listdir(files_path)):
        if files[-4:] == '.xml':
            key = unit + '_' + str(files_index//2+1)
            # xml解析
            filepath = os.path.join(path, unit, files)
            # print(filepath)
            obj_info = getObjInfo(filepath)
            # print(obj_info)
            for obj_id, obj in enumerate(obj_info):
                obj_key = key + '_' + str(obj_id)
                content = files + '-' + obj + '_' + str(obj_id)
                obj_dict[obj_key] = content

# for item in target_dict:
#     print(item)
#     print(target_dict[item])

print('共记录目标：' + str(len(obj_dict)) + '个')
path = 'Samples_Object_' + dirname + '.json'
with open(path,"w") as f:
    json.dump(obj_dict,f)
    print("写入文件完成...")

# #*******************************************************************************

with open(path,'r') as load_f:
    load_dict = json.load(load_f)
    print('共载入目标：' + str(len(load_dict)) + '个')

