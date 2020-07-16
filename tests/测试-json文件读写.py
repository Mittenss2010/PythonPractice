import json                                                                         
data = {'aaa':'bbb'}  
jsonfile = open('G:/00000_sit.json', 'w', encoding='utf-8')      #打开一个名字为‘user_info.json’的空文件
json.dump(data, jsonfile, ensure_ascii=False, indent=4)         #字典转成json,字典转换成字符串s

## json 文件读入

# with open('00000_back.json', 'r') as f:
#     human_data = json.load(f)