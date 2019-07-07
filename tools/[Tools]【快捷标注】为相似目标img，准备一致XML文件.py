import os
import shutil
count = 0

folderName = "02"

# 修改为图片路径
picPath = "./" + folderName + "/"

# 修改为原始xml 路径
pathXML_Original = "./temp.xml"

# 修改为：图片路径 + temp.xml
pathDest = picPath + "/temp.xml"

for item in os.listdir(picPath):
    print(item) 
    shutil.copy(pathXML_Original,pathDest)
    shutil.move(pathDest,picPath + item[:-3] + 'xml')
    # break
