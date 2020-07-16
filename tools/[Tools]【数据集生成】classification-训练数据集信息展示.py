import os
import shutil
import math
import random
from tqdm import tqdm


LARGE_NUM = 1000000000


class ConstructDatasets():

    def __init__(self, dataPath, train_percent, val_percent):
        self.temp_train_images = '/train_valid/train/'
        self.temp_val_images = '/train_valid/valid/'
        self.classes_dict = {}
        self.classes_dict_balance = {}
        self.classnum_table = {}
        self.dataPath = dataPath
        self.train_percent = train_percent
        self.val_percent = val_percent

        self.minClass_num = 100000000000
        self.disp_data_state()



    def disp_data_state(self):
        
        for classname in os.listdir(self.dataPath):
            files_path = self.dataPath + classname + '/'
            num = len(os.listdir(files_path))
            self.classnum_table[num] = classname

            if self.minClass_num > num:
                self.minClass_num = num

        print(self.minClass_num)        
        print(self.classnum_table[self.minClass_num])


    def get_fatherPath(self):
        father_Path = self.dataPath[:-6]
        return father_Path

    def construct_fileFrame_balance(self):
        
        fatherPath = self.get_fatherPath()
        # 遍历，对每个类创建路径
        for classaname in os.listdir(self.dataPath):
            dstpath = fatherPath + 'new' + '/' + classaname + '/'
            if not os.path.exists(dstpath):
                os.makedirs(dstpath)
            print(dstpath)

        # 按照最少的数据数量输出新的数据集
        # 找到最小的数据数量的类别
        # 从其他的类随机提取同样数量的样本
        # 原始文件路径
        # 目标文件路径

    def select_and_move_balance(self):
        # 建立 class的 dict, 包含不同类的 filelist
        for classname in os.listdir(self.dataPath):
            files_path = self.dataPath + classname + '/'
            self.classes_dict[classname] = []
            for filename in os.listdir(files_path):
                self.classes_dict[classname].append(filename)
            # print(self.classes_dict[classname])

        fatherPath = self.get_fatherPath()
        for classname in os.listdir(self.dataPath):
            self.classes_dict_balance[classname] = random.sample(self.classes_dict[classname], self.minClass_num)
            print(len(self.classes_dict_balance[classname] ))

            for item in tqdm(self.classes_dict_balance[classname]):
                img_src = self.dataPath + classname + '/' +  item
                img_dst = fatherPath + 'new' + '/' + classname + '/' + item
                shutil.copy(img_src, img_dst)

    # 构建目录结构
    def construct_fileFrame(self):

        fatherPath = self.get_fatherPath()
        # 遍历，对每个类创建路径
        for classaname in os.listdir(self.dataPath):
            dstpath_train = fatherPath + self.temp_train_images + classaname + '/'
            dstpath_valid = fatherPath + self.temp_val_images + classaname + '/'

            if not os.path.exists(dstpath_train):
                os.makedirs(dstpath_train)
            if not os.path.exists(dstpath_valid):
                os.makedirs(dstpath_valid)
            # print(dstpath_train)
            # print(dstpath_valid)


    def select_and_move(self):

        # 建立 class的 dict, 包含不同类的 filelist
        for classname in os.listdir(self.dataPath):
            files_path = self.dataPath + classname + '/'
            self.classes_dict[classname] = []
            for filename in os.listdir(files_path):
                self.classes_dict[classname].append(filename)
        # 验证 dict 
        # for item in self.classes_dict:
        #     print(self.classes_dict[item])

        # 验证集数据 move
        fatherPath = self.get_fatherPath()
        for classname in os.listdir(self.dataPath):
            self.classes_dict_val[classname] = random.sample(self.classes_dict[classname], self.val_num)
            for item in tqdm(self.classes_dict_val[classname]):
                img_src = self.dataPath + classname + '/' +  item
                img_dst = fatherPath + self.temp_val_images + classname + '/' + item
                shutil.copy(img_src, img_dst)
                # break

        # 训练集
        for classname in os.listdir(self.dataPath):
            train_random_list = [item for item in self.classes_dict[classname] if item not in set(self.classes_dict_val[classname])]
            for item in tqdm(train_random_list):
                img_src = self.dataPath + classname + '/' +  item
                img_dst = fatherPath + self.temp_train_images + classname + '/' + item
                shutil.copy(img_src,img_dst)
                # break


if __name__ == "__main__":
    # 移动原始分类数据集(temp)到当前路径
    # 移动生成文件到当前路径
    dataPath = 'F:/分类数据-数据集版本管理/toTest-11112/'

    # 验证集比例
    val_percent = 0.1
    train_percent = 1- val_percent
    constructer = ConstructDatasets(dataPath, train_percent, val_percent)
    constructer.construct_fileFrame_balance()
    constructer.select_and_move_balance()