import os
import shutil
count = 0
folderName = "01"

# 修改为图片路径
picPath = "./" + folderName + "/"
# 修改为原始xml 路径
pathXML_Original = "./7575.xml"
# 修改为：图片路径 + temp.xml
pathDest = picPath + "/temp.xml"

for item in os.listdir(picPath):
    print(item) 
    shutil.copy(pathXML_Original,pathDest)              # 复制
    shutil.move(pathDest,picPath + item[:-3] + 'xml')   # 改名
    # break
