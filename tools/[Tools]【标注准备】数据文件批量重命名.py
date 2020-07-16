import os
import shutil

path = './ZTM/'

for item in os.listdir(path):
    src = path + item
    dst = path + item[:6] + 'ZTM_' + item[6:]
    print(src)
    print(dst)

    shutil.move(src, dst)
