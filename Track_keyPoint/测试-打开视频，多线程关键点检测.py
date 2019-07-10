


from __future__ import division                        # 2.7中默认的整数除法是地板除，而导入了__future__之后，就是精确除了

import argparse, time, logging, os, math, tqdm, cv2    # 导入外围模块

import cv2
import threading

import numpy as np
import mxnet as mx
from mxnet import gluon, nd, image
from mxnet.gluon.data.vision import transforms

import matplotlib.pyplot as plt

import gluoncv as gcv
from gluoncv import data
from gluoncv.data import mscoco
from gluoncv.model_zoo import get_model
from gluoncv.data.transforms.pose import detector_to_simple_pose, heatmap_to_coord
from mq_utils.mq_viz import plot_keypoints
# from gluoncv.utils.viz import cv_plot_image, cv_plot_keypoints

ctx = mx.gpu(0)

def captureAndShow(ipString):
    cap = cv2.VideoCapture(ipString)
    print(ipString)
    while(cap.isOpened()):
        ret, frame_org = cap.read()
        if ret==True:
            img = cv2.resize(frame_org, (640,480))
            frame = mx.nd.array(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)).astype('uint8')
            x, frame = gcv.data.transforms.presets.yolo.transform_test(frame, short=512, max_size=350)
            # x, frame = gcv.data.transforms.presets.yolo.transform_test(frame, short=720, max_size=1280)

            x = x.as_in_context(ctx)
            class_IDs, scores, bounding_boxs = detector(x)
            pose_input, upscale_bbox = detector_to_simple_pose(frame, class_IDs, scores, bounding_boxs,
                                                                output_shape=(128, 96), ctx=ctx)
            if len(upscale_bbox) > 0:
                predicted_heatmap = estimator(pose_input)
                pred_coords, confidence = heatmap_to_coord(predicted_heatmap, upscale_bbox)

                img = plot_keypoints(frame, pred_coords, confidence, class_IDs, bounding_boxs, scores,
                                        box_thresh=0.5, keypoint_thresh=0.2)
                # cv_plot_image(img)
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

    # 初始化模型相关变量
    detector_name = "ssd_512_mobilenet1.0_coco"
    detector = get_model(detector_name, pretrained=True, ctx=ctx)
    detector.reset_class(classes=['person'], reuse_weights={'person':'person'})
    estimator = get_model('simple_pose_resnet18_v1b', pretrained='ccd24037', ctx=ctx)

    print("模型初始化完毕")
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