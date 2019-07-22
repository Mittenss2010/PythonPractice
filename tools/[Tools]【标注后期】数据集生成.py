import os
import shutil
import math
import random
from tqdm import tqdm


class ConstructDatasets():

    def __init__(self, dataPath, train_percent, val_percent):
        self.temp_train_images = '/datasets/train/images/'
        self.temp_train_labels = '/datasets/train/labels/'
        self.temp_val_images = '/datasets/val/images/'
        self.temp_val_labels = '/datasets/val/labels/'

        self.train_imgs = 'train_imgs'
        self.val_imgs = 'val_imgs'
        self.train_labels = 'train_labels'
        self.val_labels = 'val_labels'

        self.path_dict = {}
        self.dataPath = dataPath
        self.train_percent = train_percent
        self.val_percent = val_percent

        self.disp_data_state()

    def get_fatherPath(self, xmlsPath):
        dirName = xmlsPath.split('/')[-2]
        father_Path = xmlsPath[:-len(dirName)-2]
        return father_Path

    def disp_data_state(self):
        fileCount = len(os.listdir(self.dataPath))

        print('文件数量：' + str(fileCount))
        self.data_num = int(fileCount/2)
        print('数据数量：' + str(self.data_num))

        self.train_num = math.ceil(self.data_num * self.train_percent)
        self.val_num = int(self.data_num * self.val_percent)

        print('训练集数量：' + str(self.train_num))
        print('验证集数量：' + str(self.val_num))
        print('数据总量：' + str(self.train_num + self.val_num))


    # 构建目录结构
    def construct_fileFrame(self):
        fatherpath = self.get_fatherPath(self.dataPath)

        self.path_dict[self.train_imgs] = fatherpath + self.temp_train_images
        self.path_dict[self.val_imgs] = fatherpath + self.temp_val_images
        self.path_dict[self.train_labels] = fatherpath + self.temp_train_labels
        self.path_dict[self.val_labels] = fatherpath + self.temp_val_labels
        for item in self.path_dict:
            if not os.path.exists(self.path_dict[item]):
                os.makedirs(self.path_dict[item])
                print(self.path_dict[item])

    def select_and_move(self):
        # 建立.xml文件list
        xml_list = []
        for filename in os.listdir(self.dataPath):
            if filename[-3:] == 'xml':
                xml_list.append(filename[:-3])

        # 验证集数据
        val_random_xmllist = random.sample(xml_list, self.val_num)
        for item in tqdm(val_random_xmllist):
            img_src = self.dataPath + item + 'jpg'
            img_dst = self.path_dict[self.val_imgs] + item + 'jpg'
            xml_src = self.dataPath + item + 'xml'
            xml_dst = self.path_dict[self.val_labels] + item + 'xml'

            shutil.copy(img_src,img_dst)
            shutil.copy(xml_src,xml_dst)

            # print(img_src)
            # print(img_dst)
            # print(xml_src)
            # print(xml_dst)
        # print(len(val_random_xmllist))

        # 训练集
        train_random_xmllist = [item for item in xml_list if item not in set(val_random_xmllist)]
        for item in tqdm(train_random_xmllist):
            img_src = self.dataPath + item + 'jpg'
            img_dst = self.path_dict[self.train_imgs] + item + 'jpg'
            xml_src = self.dataPath + item + 'xml'
            xml_dst = self.path_dict[self.train_labels] + item + 'xml'

            shutil.copy(img_src,img_dst)
            shutil.copy(xml_src,xml_dst)

        print('数据总量：' + str(len(train_random_xmllist) + len(val_random_xmllist)))



if __name__ == "__main__":
    
    # dataPath = 'G:/【cqsy_collection】/数据标注管理/【数据集】测试过的数据集/2019-07-20-表演过的数据集-showatdoor/'

    dataPath = 'G:/2019-07-22/'
    # dataPath = 'G:/VOCdevkit/'

    # 验证集比例
    val_percent = 0.1
    train_percent = 0.9

    constructer = ConstructDatasets(dataPath,train_percent, val_percent)
    constructer.construct_fileFrame()
    constructer.select_and_move()
