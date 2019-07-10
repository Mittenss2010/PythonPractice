# import numpy as np
# import cv2
# import redis
# import base64
# import threading

# # start = time.time()

# # t1 = threading.Thread(target=decrement, args=[50000000])
# # t2 = threading.Thread(target=decrement, args=[50000000])

# # t1.start() # 启动线程，执行任务


# cap = cv2.VideoCapture('rtsp://admin:qwe,asd.@192.168.1.64:554/ch1/main/av_stream')
# cap1 = cv2.VideoCapture('rtsp://admin:qwe,asd.@192.168.1.65:554/ch1/main/av_stream')
# cap2 = cv2.VideoCapture('rtsp://admin:qwe,asd.@192.168.1.66:554/ch1/main/av_stream')

# cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
# cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()

#     if ret==True:
#         # frame
#         # obj_redis = redis.Redis(host='127.0.0.1', port=6379)
#         # frameNum = str(int(cap.get(cv2.CAP_PROP_POS_FRAMES)))
#         # obj_redis.set(frameNum, bytearray(frame))
#         # var = obj_redis.get(frameNum)
#         # image = np.fromstring(var, np.uint8)


#         img = cv2.resize(frame, (640,480))
#         # img1 = cv2.resize(frame1, (640,480))
#         # img2 = cv2.resize(frame2, (640,480))

#         cv2.imshow('frame',img)
#         #cv2.imshow('frame1',img1)
#         #cv2.imshow('frame2',img2)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break

# cap.release()
# cv2.destroyAllWindows()




import numpy as np
import cv2
import threading


def captureAndShow(ipString):
    cap = cv2.VideoCapture(ipString)
    print(ipString)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            img = cv2.resize(frame, (640,480))
            cv2.imshow(ipString[32:34], img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

class CaptureThread(threading.Thread):
    def __init__(self, ipString):
        # 注意：一定要显式的调用父类的初始化函数。
        super(CaptureThread, self).__init__(name=ipString)

    def run(self):
        captureAndShow(self.name)
        print("%s正在运行中......" % self.name)

if __name__ == '__main__':

    ipString = 'rtsp://admin:qwe,asd.@192.168.1.64:554/ch1/main/av_stream'
    ipString1 = 'rtsp://admin:qwe,asd.@192.168.1.65:554/ch1/main/av_stream'
    ipString2 = 'rtsp://admin:qwe,asd.@192.168.1.66:554/ch1/main/av_stream'

    CaptureThread(ipString).start()
    CaptureThread(ipString1).start()
    CaptureThread(ipString2).start()



# import threading

# class MyThread(threading.Thread):
#     def __init__(self, thread_name):
#         # 注意：一定要显式的调用父类的初始化函数。
#         super(MyThread, self).__init__(name=thread_name)

#     def run(self):


#         print("%s正在运行中......" % self.name)

# if __name__ == '__main__':

#     for i in range(10):

#         MyThread("thread-" + str(i)).start()