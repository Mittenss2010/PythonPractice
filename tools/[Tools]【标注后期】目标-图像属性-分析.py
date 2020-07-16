# 计算每个类别的各个，场景覆盖率
# 设置目标在每个场景的，上限，如，目标在每种场景的出现次数为10个 
# 根据约束，记录要复制的数据名。
# 判断是否足够

import json
import os
from tqdm import tqdm


# 统计目标的场景比例
# 所有场景，列出网格dict
time_seg = {'Ri':'Ri',
            'Ye':'Ye'}

weathers = {'Qing':'Qing',
            'Yu':'Yu',
            'Yin':'Yin'
            }

uints = ['30106','30109','30656','40008','40023','40025','40562','40565','40583',
            '40589Y','40625','40648','40656','40903','50082','50289','50578','50627']



def print_combindict(obj_dict):
    for index, item in enumerate(obj_dict):
        #可视化打印方式 
        # print('\t' + str(index+1) + '队伍_时段_天气:' + item + ':' 
        #            + str(obj_dict[item])+ ' '+ ' %'*obj_dict[item])
        if obj_dict[item] != 0:
            print('\t' + str(index+1) + '_类别_队伍_时段_天气:' + item + ':' 
                    + str(obj_dict[item]))

def make_combindict( obj_dict):

    if len(obj_dict)!=0:
        for item in obj_dict:
            obj_dict[item] = 0
    else:
        for classname in classnames:
            for uint in uints:
                for seg in time_seg:
                    for weather in weathers:
                            key = classname+ '_' +uint + '_' + seg+'_'+weather
                            obj_dict[key] = 0


if __name__ == "__main__":
    

    dirname = 'all_data-191218_32532'
    path = os.path.join(dirname)
    json_path = 'Samples_Object_' + dirname + '.json'

    # 检索数据记录
    with open(json_path,'r') as load_f:
        load_dict = json.load(load_f)
        print('共载入文件：' + str(len(load_dict)) + '个')

    obj_dict = {}

    # 统计每个类的目标数量
    # for item in tqdm(load_dict):
    #     # "30106_1_0": "30106_ZTM_Ri_Qing_QiZuan_20190311_15753837768295088.xml-shoutao_0"
    #     classname = load_dict[item].split('-')[1].split('_')[0]
    #     if classname not in objdict:
    #         objdict[classname] = 1
    #     objdict[classname] +=1

    # print(f'当前数据标注了 {len(objdict):5.0f} 个类别')

    # for item in objdict:
    #     print(item)
    #     print(objdict[item])

     # 统计每个类别在所有场景下的分布
    # make_combindict(obj_dict)
    
    # for item in tqdm(load_dict):
    #     # "30106_1_0": "30106_ZTM_Ri_Qing_QiZuan_20190311_15753837768295088.xml-shoutao_0"
    #     classname = load_dict[item].split('-')[1].split('_')[0]
    #     scene = load_dict[item].split('-')[0].split('_')
    #     uint = scene[0]
    #     time_seg = scene[2]
    #     weather = scene[3]
    #     obj_key = classname+ '_' +uint + '_' + time_seg+'_'+weather
    #     if obj_key not in obj_dict:
    #         obj_dict[obj_key] = 0
    #     obj_dict[obj_key] += 1

    # print_combindict(obj_dict)

# 测试集无需平衡，只需要覆盖到每一个场景即可



