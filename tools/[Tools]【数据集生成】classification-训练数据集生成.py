import os
import shutil
import math
import random
from tqdm import tqdm

class ConstructDatasets():

    def __init__(self, dataPath, train_percent, val_percent):
        self.temp_train_images = '/train_valid/train/'
        self.temp_val_images = '/train_valid/valid/'
        self.classes_dict = {}
        self.classes_dict_val = {}

        self.dataPath = dataPath

        self.train_percent = train_percent
        self.val_percent = val_percent
        self.disp_data_state()

    def disp_data_state(self):

        fileCount = 0
        for classname in os.listdir(self.dataPath):
            files_path = self.dataPath + classname + '/'
            fileCount += len(os.listdir(files_path))
        print('数据数量：' + str(fileCount))

        # self.data_num = int(fileCount/2)
        # print('数据数量：' + str(self.data_num))

        self.train_num = math.ceil(fileCount * self.train_percent)
        self.val_num = int(fileCount * self.val_percent)

        print('训练集数量：' + str(self.train_num))
        print('验证集数量：' + str(self.val_num))
        print('数据总量：' + str(self.train_num + self.val_num))

    def get_fatherPath(self):
        father_Path = self.dataPath[:-6]
        return father_Path

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
    dataPath = 'G:/【NOW】codeAnalysis/files-TF/temp/'

    # 验证集比例
    val_percent = 0.1
    train_percent = 1- val_percent

    constructer = ConstructDatasets(dataPath, train_percent, val_percent)
    constructer.construct_fileFrame()
    constructer.select_and_move() 

