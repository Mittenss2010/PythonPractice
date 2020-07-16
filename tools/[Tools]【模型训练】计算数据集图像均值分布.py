
import json
import os
from tqdm import tqdm
import cv2

attr_dict = {}

if __name__ == "__main__":
    
    dirname = 'all_data-191218_32532'

    for unit in tqdm(os.listdir(dirname)):
        for filename in tqdm(os.listdir(os.path.join(dirname, unit))):
            if filename[-4:] == '.jpg':
                img = cv2.imread(os.path.join(dirname, unit, filename))
                (mean , stddv) = cv2.meanStdDev(img)
                mean_str = [str(x) for x in mean[:,0]]
                stddv_str = [str(x) for x in stddv[:,0]]
                value = ','.join(mean_str) + '_'  + ','.join(stddv_str) 
                attr_dict[filename] = value
    
    print('共记录目标：' + str(len(attr_dict)) + '个')
    path = 'Samples_attr_' + dirname + '.json'
    with open(path,"w") as f:
        json.dump(attr_dict,f)
        print("写入文件完成...")





