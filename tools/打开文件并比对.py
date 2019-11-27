
Path = 'F:/数据集版本管理/Mix_base_test_40656/voc.names'

f = open(Path, 'r')                   #以读方式打开文件
classnames_list = list()
for line in f.readlines():                          #依次读取每行
    line = line.strip()                             #去掉每行头尾空白
    if not len(line) or line.startswith('#'):       #判断是否是空行或注释行
        continue                                    #是的话，跳过不处理
    classnames_list.append(line)                             #保存
