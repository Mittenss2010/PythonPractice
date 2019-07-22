import os
import shutil

folderName = "2019年7月18日-02"      # 图片所在，文件夹名称
pathXML_Original = "./950.xml"       # 画好框的xml 名称，例：123.xml，525.xml

picPath = "./" + folderName + "/" 
pathDest = picPath + "/temp.xml"     

for item in os.listdir(picPath):
    shutil.copy(pathXML_Original,pathDest)
    shutil.move(pathDest,picPath + item[:-3] + 'xml')


    
