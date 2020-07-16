# 1、redis连接

# redis提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，
# Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py。
# redis连接实例是线程安全的，可以直接将redis连接实例设置为一个全局变量，直接使用。
# 如果需要另一个Redis实例（or Redis数据库）时，就需要重新创建redis连接实例来获取一个新的连接。
# 同理，python的redis没有实现select命令。

# 安装redis
# pip install redis

# 连接redis，加上decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型。


# import redis   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

# r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
# r.set('name', 'junxi')                                                # key是"foo" value是"bar" 将键值对存入redis缓存
# print(r['name'])
# print(r.get('name'))  # 取出键name对应的值
# print(type(r.get('name')))



# python将图片转base64存入redis，再读取出来,并存储！***************************************************************************
# import redis
# import base64
 
# #图片转文字
 
# with open("../Track_keyPoint/ignore_video/001.jpg","rb") as f:    # 打开01.png图片
#     # b64encode是编码，b64decode是解码
#     base64_data = base64.b64encode(f.read())    #读取图片转换的二进制文件，并给赋值
#     # base64.b64decode(base64data)
#     print(base64_data)
#     r = redis.Redis(host='127.0.0.1', port=6379)
#     r.set("jpg_test", base64_data)
 
#     var = r.get("jpg_test")
#     print(var)
#     data = base64.b64decode(var)  # 把二进制文件解码，并复制给data
#     with open("../Track_keyPoint/ignore_video/001_out.jpg", "wb") as f:  # 写入生成一个jd.png
#         f.write(data)

# python将图片转base64存入redis，再读取出来,做检测！***************************************************************************

import redis
import base64

with open("../Track_keyPoint/ignore_video/001.jpg","rb") as f:    # 打开01.png图片
    # b64encode是编码，b64decode是解码
    base64_data = base64.b64encode(f.read())    #读取图片转换的二进制文件，并给赋值
    # base64.b64decode(base64data)
    print(base64_data)
    r = redis.Redis(host='127.0.0.1', port=6379)
    r.set("jpg_test", base64_data)
 
    var = r.get("jpg_test")