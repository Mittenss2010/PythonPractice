
import re
import urllib.request
 
url = 'http://pd.zhijinwang.com/'

# https://jingyan.baidu.com/article/020278118741e91bcd9ce566.html
# GB2312
# iso8859-1
data=urllib.request.urlopen(url).read().decode(encoding='GB2312')    #读取并解码，默认应该是utf-8?
print(data)

# 


# rule=r'src="(.+?\.jpg)" pic_ext'
# compiled_rule=re.compile(rule)
# list1=re.findall(compiled_rule,data)
# x=1
# path='d://python//grab//photo'#构建本地保存路径
# for element in list1:
#     pathnew=path+'//'+str(x)+'.jpg'
#     urllib.request.urlretrieve(element,pathnew)
