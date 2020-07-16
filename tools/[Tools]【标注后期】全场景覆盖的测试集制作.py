import json
import os
from tqdm import tqdm
import random
import shutil



time_seg = {'Ri':'Ri',
            'Ye':'Ye'}

weathers = {'Qing':'Qing',
            'Yu':'Yu',
            'Yin':'Yin'
            }

uints = ['30106','30109','30656','40008','40023','40025','40562','40565','40583',
            '40589Y','40625','40648','40656','40903','50082','50289','50578','50627']

operations = ['QiZuan','XiaZuan','ZuanJin','BiaoYan','XiaTaoGuan','QiTa','XiaZuanJu',
              'DiaoQianLaJin','JianXiu','ShuangQianJinKou','WuRen','XieZuanTou',
              'CeJing','DianHan','DiaoZuanJu','TingZuan','TiZuanJu']

print('所有场景的组合情况有：')
print(len(time_seg) * len(weathers) * len(uints) * len(operations))



def print_combindict(scene_dict, thresh):
    for index, item in enumerate(scene_dict):
        if scene_dict[item] > thresh:
            print('\t' + str(index+1) + '队伍_时段_天气_作业:' + item + ':' 
                    + str(scene_dict[item]))

def make_combindict( scene_dict):
    for uint in uints:
        for seg in time_seg:
            for weather in weathers:
                for operation in operations:
                    key = uint + '_' + seg+'_'+weather+'_'+operation
                    scene_dict[key] = 0

if __name__ == "__main__":


    dirname = 'all_data-191218_32532'
    path = os.path.join(dirname)
    json_path = 'Samples_' + dirname + '.json'

    # 检索数据记录
    with open(json_path,'r') as load_f:
        load_dict = json.load(load_f)
        print('共载入文件：' + str(len(load_dict)) + '个')

    scene_dict = {}

    # 统计有多少种场景


    # 每种场景的数据数量*********************************************************
    for item in tqdm(load_dict):
        scenedata = load_dict[item][:-4].split('_')
        uint = scenedata[0]
        time_seg = scenedata[2]
        weather = scenedata[3]
        operation = scenedata[4]
        key = uint + '_' + time_seg+'_'+weather+'_'+operation
        if key not in scene_dict:
            scene_dict[key] = []
        scene_dict[key].append(load_dict[item])
    
    # thresh = 10
    # print_combindict(scene_dict, thresh)

    # 构建用来移动的数据列表******************************************************
    cover_all_dict = {}
    for item in tqdm(scene_dict):
        if len(scene_dict[item]) > 20:
            # 随机抽取20个组数据作为测试集
            print(item)
            # if key not in cover_all_dict:
            #     cover_all_dict[item] = []
            cover_all_dict[item] = random.sample(scene_dict[item], 20)
            print(len(cover_all_dict[item]))
    
    print("测试数据集数量: ")
    print(len(cover_all_dict)*20)




# 移动待测试的数据集**************************************************************

    testdata_path = 'test_data'
    if not os.path.exists(testdata_path):
        os.mkdir(testdata_path)

    count = 0
    for scene in cover_all_dict:
        for filename in cover_all_dict[scene]:
            filepath = os.path.join(dirname, filename.split('_')[0],filename)
            new_filepath = os.path.join(testdata_path,filename)
            print(filepath)
            print(new_filepath)
            count+=1
            shutil.copy(filepath, new_filepath)
            shutil.copy(filepath[:-4] + '.jpg', new_filepath[:-4] + '.jpg')


# path = 'test_dataset_' + dirname + '.json'

# with open(path,"w") as f:
#     json.dump(samples_dict,f)
#     print("加载入文件完成...")
