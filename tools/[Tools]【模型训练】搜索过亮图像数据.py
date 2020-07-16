#train_rec,train_prec, test_rec,test_prec


import os
import shutil
import json
import numpy as np
import matplotlib.pyplot as plt

def get_PRmap_list(path):
    '''
        功能：获取图像文件名与精度列表与step映射
        参数：文件路径
            P_or_R:procession, recall
    '''
    with open(path,'r') as load_f:
        load_dict = json.load(load_f)
    steps = []
    r_mean_value = []
    g_mean_value = []
    b_mean_value = []
    r_std_value  = []
    g_std_value  = []
    b_std_value  = []

    for index, item in enumerate(load_dict):
        r = int(load_dict[item].split(',')[0].split('.')[0])
        g = int(load_dict[item].split(',')[1].split('.')[0])
        b = int(load_dict[item].split(',')[2].split('.')[0])

        if r > 200 or g>200 or b > 200:
            print(item)
        # steps.append(index)

path_1 = 'Samples_attr_all_data-191218_32532.json'
get_PRmap_list(path_1)

