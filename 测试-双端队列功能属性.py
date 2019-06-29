# queue模块有三种队列及构造函数
# Python queue模块的FIFO队列先进先出。 
# queue.Queue(maxsize)

# LIFO类似于堆，即先进后出。 
# queue.LifoQueue(maxsize)

# 还有一种是优先级队列级别越低越先出来。 
# queue.PriorityQueue(maxsize)

# queue模块中的常用方法
# queue.qsize() 返回队列的大小
# queue.empty() 如果队列为空，返回True,反之False
# queue.full() 如果队列满了，返回True,反之False
# queue.full 与 maxsize 大小对应
# queue.get([block[, timeout]])获取队列，立即取出一个元素， timeout超时时间
# queue.put(item[, timeout]]) 写入队列，立即放入一个元素， timeout超时时间
# queue.get_nowait() 相当于queue.get(False)
# queue.put_nowait(item) 相当于queue.put(item, False)
# queue.join() 阻塞调用线程，直到队列中的所有任务被处理掉, 实际上意味着等到队列为空，再执行别的操作
# queue.task_done() 在完成一项工作之后，queue.task_done()函数向任务已经完成的队列发送一个信号


# ******************************************************************************
# 队列测试
# from collections import deque

# for i in range(20):
#     trackstack[i] = deque([], 20)

# trackstack[0].appendleft(('label, bbox, score'))
# ******************************************************************************

# import collections 
# import queue
# d=collections.deque('abcdefg')

# print('Deque:',d)
# print('Length:',len(d))
# print('Left end:',d[0])
# print('Right end:',d[-1])
 
# d.remove('c')
# print('remove(c):',d)

# d = queue.Queue(maxsize=20)

# print('Deque:',d)
# print('Length:',d.qsize())
# print('Length:',d.full())

# for i in range(30):
#     if not d.full():
#         print(d.put(str(i)))
#     else:
#         print('full')
#         print(d.get())
#         print(d.put(str(i)))

# print('Length:',d.qsize())


# ******************************************************************************
# from  collections import deque

# L1_track_deque = deque(maxlen=20)

# print(len(L1_track_deque))
# # print(L1_track_deque.__len__())

# # 循环添加，自动挤出队列
# for item in range(30):
#     L1_track_deque.appendleft(item)

# print(L1_track_deque.pop())
# print(len(L1_track_deque))


# ******************************************************************************
# 测试，通过循环iterator对象，并对其列表化，赋值到四个变量
# xmin, ymin, xmax, ymax = [int(x) for x in bbox]

# bbox = [1,2,3,4]
# a,b,c,d = [i for i in bbox]
# print(a,b,c,d)

# 字典测试


# ClassType = {"ye_qi_da_qian":"动态",
#              "ye_qi_da_qian_open":"动态",
#              "ye_qi_da_qian_close":"动态",
#              "roi_zhuan_pan":"静态"
#             }

# print("ye_qi_da_qian" in ClassType)


ClassType = {"ye_qi_da_qian":"动态",
             "ye_qi_da_qian_open":"动态",
             "ye_qi_da_qian_close":"动态",
             "roi_zhuan_pan":"静态"
            }

print(ClassType)

for item in ClassType:
    print(item)                   # 返回键
    print(ClassType[item])        # 访问值


# ******************************************************************************
# 测试 enumerate

# seq = ['one', 'two', 'three']
# for i, element in enumerate(seq):
#     print(i, element)


# ******************************************************************************
# 测试 zip

# >>> a = [1,2,3]
# >>> b = [4,5,6]
# >>> c = [4,5,6,7,8]
# >>> zipped = zip(a,b)     # 打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]

# >>> zip(a,c)              # 元素个数与最短的列表一致
# [(1, 4), (2, 5), (3, 6)]

# >>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# [(1, 2, 3), (4, 5, 6)]

# ******************************************************************************

