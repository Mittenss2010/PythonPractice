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
        if index < 1000:
            steps.append(index)
            print(index)
            r_mean_value.append(int(load_dict[item].split(',')[0].split('.')[0]))
            g_mean_value.append(int(load_dict[item].split(',')[1].split('.')[0]))
            b_mean_value.append(int(load_dict[item].split(',')[2].split('.')[0]))
            r_std_value .append(int(load_dict[item].split(',')[3].split('.')[0]))
            g_std_value .append(int(load_dict[item].split(',')[4].split('.')[0]))
            b_std_value .append(int(load_dict[item].split(',')[5].split('.')[0]))

    return steps, r_mean_value, g_mean_value, b_mean_value, r_std_value ,g_std_value ,b_std_value 

# 绘制ROC曲线 *******************************************************************

path_1 = 'Samples_attr_all_data-191218_32532.json'
values = get_PRmap_list(path_1)

plt.subplot(6, 1, 1)
plt.plot(values[0], values[1], '.', label = 'r_mean')
plt.title('Attr1')
plt.legend(loc='upper right')
plt.ylabel('r_mean')

plt.subplot(6, 1, 2)
plt.plot(values[0], values[2], '.', label = 'g_mean')
plt.title('Attr2')
plt.legend(loc='upper right')
plt.ylabel('g_mean')

plt.subplot(6, 1, 3)
plt.plot(values[0], values[3], '.', label = 'b_mean')
plt.title('Attr3')
plt.legend(loc='upper right')
plt.ylabel('b_mean')


plt.subplot(6, 1, 4)
plt.plot(values[0], values[4], '.', label = 'r_std')
plt.title('Attr4')
plt.legend(loc='upper right')
plt.ylabel('r_std_value')

plt.subplot(6, 1, 5)
plt.plot(values[0], values[5], '.', label = 'g_std')
plt.title('Attr5')
plt.legend(loc='upper right')
plt.ylabel('g_std_value')

plt.subplot(6, 1, 6)
plt.plot(values[0], values[6], '.', label = 'b_std')
plt.title('Attr6')
plt.legend(loc='upper right')
plt.ylabel('b_std_value')


plt.show()

