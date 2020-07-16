# import multiprocessing
# import random


# def func(num):

#     # 内部数组赋值
#     # print(len(num))
#     index = random.randint(0,4)
#     print(index)
#     num[index] = 9999   #子进程改变数组，主进程跟着改变


# if  __name__=="__main__":

#     #主进程与子进程共享这个数组
#     num = multiprocessing.Array("i",[1,2,3,4,5])   
#     print(num[:])
#     process_list = []
    
#     for i in range(4):
#         #print(i)
#         # 数组作为：args 参数传入
#         process_list.append(multiprocessing.Process(target=func,args=(num,)))
        
#         process_list[i].start()
#         process_list[i].join()
#     print(num[:])


# ******************************************************************************


import multiprocessing
import time


class camera():

    def __init__(self):
        pass
    
    def funname(self):
        pass

  
def func(mydict, mylist):  

    cam = camera()
    cam1 = camera()

    mydict["index1"] = cam   #子进程改变dict,主进程跟着改变  
    mydict["index2"] = cam1 

    mylist.append(11)        #子进程改变List,主进程跟着改变  
    mylist.append(22)  
    mylist.append(33)  
  
if __name__=="__main__":  
    with multiprocessing.Manager() as MG:   #重命名  
        mydict=MG.dict()              # 主进程与子进程共享这个字典  
        mylist=MG.list(range(5))      # 主进程与子进程共享这个List  
  
        p=multiprocessing.Process(target=func,args=(mydict, mylist))  
        p.start()  
        p.join()  
  
        print(mylist)  
        print(mydict)  