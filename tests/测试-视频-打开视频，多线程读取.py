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