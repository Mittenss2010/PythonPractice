import shutil
import os

path = 'G:/cqsy_collection/cqsy_python_practice/tools/ignore_files/newXmls/'
path_new = 'G:/cqsy_collection/cqsy_python_practice/tools/ignore_files/newXmls/7-15-01-'

for filename in os.listdir(path):
    shutil.move(path + filename, path_new + filename)