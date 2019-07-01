
# 测试python，最大count
# 测试多模型，显卡预测
# 测试

import sys
max = sys.maxsize

output_num_str = str(max)

# 给字符串每个元素间插入符号
# join用法测试
# 描述
# Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

# 语法
# join()方法语法：

# str.join(sequence)
# 参数
# sequence -- 要连接的元素序列。 
# 返回值
# 返回通过指定字符连接序列中元素后生成的新字符串。

#print(print('\''.join(list(output_num_str))))

output_num_list = list(output_num_str)
#print(output_num_list)

for i in range(len(output_num_list)):
    if i%3 == 0:
        output_num_list.insert(len(output_num_list) - i, '\'')
print(output_num_list)

print(max)
print(max*max)


# i=0
# while True:
#     i+=1
#     if i%1000000 == 0:
#         print(i)


#   python string与list互转 
# 因为python的read和write方法的操作对象都是string。
# 而操作二进制的时候会把string转换成list进行解析，解析后重新写入文件的时候，还得转换成string。


import string
str = 'abcde'
list = list(str)
list
str

str_convert = ''.join(list)
str_convert
