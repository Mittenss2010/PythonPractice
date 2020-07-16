import json
import os


# key id号，value 文件名
# 检索路径，构建dict
# path = './/'
dirname = 'all_data-191218_32532'

samples_dict = {}
path = os.path.join(dirname)
for unit_index, unit in enumerate(os.listdir(path)):
    filespath = os.path.join(path, unit)
    for files_index, files in enumerate(os.listdir(filespath)):
        if files[-4:] == '.xml':
            key = unit + '_' + str(files_index//2+1)
            samples_dict[key] = files
            # print(key)

print('共记录文件：' + str(len(samples_dict)) + '个')
# path = 'G:/[NOW]cqsy_collection/@@PythonPractice/tools/ignore_files/Samples.json'
# path = 'Samples_MQ.json'
# path = 'Samples_LZ.json'
path = 'Samples_' + dirname + '.json'

with open(path,"w") as f:
    json.dump(samples_dict,f)
    print("加载入文件完成...")
#*******************************************************************************

with open(path,'r') as load_f:
    load_dict = json.load(load_f)
    print('共载入文件：' + str(len(load_dict)) + '个')




#*******************************************************************************
# #dumps 将数据转换成字符串
# json_str = json.dumps(test_dict)
# print(json_str)
# print(type(json_str))


# new_dict = json.loads(json_str)
# print(new_dict)
# print(type(new_dict))

# path = 'G:/[NOW]cqsy_collection/@@PythonPractice/tools/ignore_files/ecord.json'

# with open(path,"w") as f:
#     json.dump(test_dict,f)
#     print("加载入文件完成...")


