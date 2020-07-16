import os
import shutil

folderName = "add1"              # 图片所在，文件夹名称
pathXML_Original = "G:/@@@@Now_DataPro/0323_labels/063.xml"       # 画好框的xml 名称，例：123.xml，525.xml

picPath = "G:/@@@@Now_DataPro/0323_labels/" + folderName + "/" 
pathDest = picPath + "/temp.xml"     

for item in os.listdir(picPath):
    shutil.copy(pathXML_Original, pathDest)
    shutil.move(pathDest, picPath + item[:-3] + 'xml')