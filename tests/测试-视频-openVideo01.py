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


if __name__ == '__main__':

    ipString = 'rtsp://admin:qwe,asd.@192.168.1.64:554/ch1/main/av_stream'
    captureAndShow(ipString)

