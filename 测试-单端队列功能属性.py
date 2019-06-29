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
