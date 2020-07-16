#train_rec,train_prec, test_rec,test_prec


import os
import shutil
import json
import numpy as np
import matplotlib.pyplot as plt




def get_PRmap_list(path, P_or_R):
    '''
        功能：获取精度列表与step映射
        参数：文件路径
            P_or_R:procession, recall
    '''
    with open(path,'r') as load_f:
        load_dict = json.load(load_f)

    steps = []
    for item in load_dict.keys():
        steps.append(int(item))
    steps.sort()

    if P_or_R == 'procession':
        return np.array(steps), [float(load_dict[str(item)].split(',')[1]) for item in steps]
    if P_or_R == 'recall':
        return np.array(steps), [float(load_dict[str(item)].split(',')[0]) for item in steps]

# 绘制ROC曲线 *******************************************************************

path_1 = 'rocdata_1.json'
path_2 = 'rocdata_2.json'
path_3 = 'rocdata_3.json'

# plt.subplot(2, 1, 1)
# x0,y0 = get_PRmap_list(path_1, 'recall')
# x1,y1 = get_PRmap_list(path_2, 'recall')
# x2,y2 = get_PRmap_list(path_3, 'recall')

# plt.plot(x0, y0, '.-', label = 'R1')
# plt.plot(x1, y1, '.-', label = 'R2')
# plt.plot(x2, y2, '.-', label = 'R3')
# plt.legend(loc='upper right')

# plt.title('Recal')
# plt.ylabel('Recal')

# plt.subplot(2, 1, 2)
# x3,y3 = get_PRmap_list(path_1, 'procession')
# x4,y4 = get_PRmap_list(path_2, 'procession')
# x5,y5 = get_PRmap_list(path_3, 'procession')

# plt.plot(x3, y3, '.-', label = 'P1')
# plt.plot(x4, y4, '.-', label = 'P2')
# plt.plot(x5, y5, '.-', label = 'P3')

# plt.title('Procession')
# plt.ylabel('procession')

# plt.legend(loc='upper right')
# plt.show()


# 1000 step+之后的均值，标准差，方差***********************************************


def cal_mean_var_std(values, after_step):
    mean = np.mean(values[after_step:])
    var = np.var(values[after_step:])
    std = np.std(values[after_step:], ddof = 1)
    return mean,var,std


interval = 20
x0,y1 = get_PRmap_list(path_1, 'recall')
x0,y2 = get_PRmap_list(path_2, 'recall')
x0,y3 = get_PRmap_list(path_3, 'recall')

# stc_val1 = cal_mean_var_std(y1, 1000//interval)
# stc_val2 = cal_mean_var_std(y2, 1000//interval)
# stc_val3 = cal_mean_var_std(y3, 1000//interval)

# aver_stc_val = (np.array(stc_val1) + np.array(stc_val1) + np.array(stc_val1))/3

# print(f'1000 Step后，recall 均值：{stc_val1[0]:4.4f} 方差：{stc_val1[1]:4.4f} 标准差：{stc_val1[2]:4.4f} ')
# print(f'1000 Step后，recall 均值：{stc_val2[0]:4.4f} 方差：{stc_val2[1]:4.4f} 标准差：{stc_val2[2]:4.4f} ')
# print(f'1000 Step后，recall 均值：{stc_val3[0]:4.4f} 方差：{stc_val3[1]:4.4f} 标准差：{stc_val3[2]:4.4f} ')



x0,y4 = get_PRmap_list(path_1, 'procession')
x0,y5 = get_PRmap_list(path_2, 'procession')
x0,y6 = get_PRmap_list(path_3, 'procession')

# stc_val4 = cal_mean_var_std(y4, 1000//interval)
# stc_val5 = cal_mean_var_std(y5, 1000//interval)
# stc_val6 = cal_mean_var_std(y6, 1000//interval)


# print(f'1000 Step后，procession 均值：{stc_val1[0]:4.4f} 方差：{stc_val1[1]:4.4f} 标准差：{stc_val1[2]:4.4f} ')
# print(f'1000 Step后，procession 均值：{stc_val2[0]:4.4f} 方差：{stc_val2[1]:4.4f} 标准差：{stc_val2[2]:4.4f} ')
# print(f'1000 Step后，procession 均值：{stc_val3[0]:4.4f} 方差：{stc_val3[1]:4.4f} 标准差：{stc_val3[2]:4.4f} ')

def cal_f1_stc_val(y_p, y_r, after_step):
    f1_list = 2*np.array(y_p)*np.array(y_r)/(np.array(y_p)+np.array(y_r))
    f1_mean = np.mean(f1_list[after_step:])
    f1_var = np.var(f1_list[after_step:])
    f1_std = np.std(f1_list[after_step:], ddof = 1)  # 无偏标准差

    return f1_mean,f1_var,f1_std

f1_stc_val1 = cal_f1_stc_val(y1, y4, interval)
f1_stc_val2 = cal_f1_stc_val(y3, y5, interval)
f1_stc_val3 = cal_f1_stc_val(y3, y6, interval)

print(f'1000 Step后，F1 均值：{f1_stc_val1[0]:4.4f} 方差：{f1_stc_val1[1]:4.4f} 标准差：{f1_stc_val1[2]:4.4f} ')
print(f'1000 Step后，F1 均值：{f1_stc_val2[0]:4.4f} 方差：{f1_stc_val2[1]:4.4f} 标准差：{f1_stc_val2[2]:4.4f} ')
print(f'1000 Step后，F1 均值：{f1_stc_val3[0]:4.4f} 方差：{f1_stc_val3[1]:4.4f} 标准差：{f1_stc_val3[2]:4.4f} ')
