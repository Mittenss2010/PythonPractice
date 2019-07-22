from __future__ import division                        # 2.7中默认的整数除法是地板除，而导入了__future__之后，就是精确除了
import argparse, time, logging, os, math, tqdm, cv2    # 导入外围模块

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
from mq_utils.mq_viz import plot_bbox
# from gluoncv.utils.viz import cv_plot_image, cv_plot_keypoints


# 初始化模型相关变量
ctx = mx.gpu(0)
detector_name = "ssd_512_mobilenet1.0_coco"
detector = get_model(detector_name, pretrained=True, ctx=ctx)
detector.reset_class(classes=['person'], reuse_weights={'person':'person'})
#estimator = get_model('simple_pose_resnet18_v1b', pretrained='ccd24037', ctx=ctx)


# 构造视频相关参数
video_path = './ignore_video/images/'
axes = None
num_frames = 1000
for filename in os.listdir(video_path):
    
    cv2.imread()
    frame = mx.nd.array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).astype('uint8')

    x, frame = gcv.data.transforms.presets.yolo.transform_test(frame, short=512, max_size=350)
    # x, frame = gcv.data.transforms.presets.yolo.transform_test(frame, short=720, max_size=1280)
    x = x.as_in_context(ctx)
    class_IDs, scores, bounding_boxs = detector(x)

    # print(bounding_boxs)
    # print(scores)
    # print(class_IDs)

    person_ind = class_IDs[0] == 0

    colors = {0: (255, 0, 0), 1:(0, 255, 0)}
    img,ret_list, minIndex = plot_bbox(frame, 
                                        bounding_boxs[0][person_ind[:, 0]],
                                        scores[0][person_ind[:, 0]],
                                        thresh=0.5)


    # img, ret_list, minIndex = plot_bbox(frame, bounding_boxs, scores, class_IDs, 
    #                                                     thresh=0.5, 
    #                                                     class_names=['person'])

    cv2.imshow("img", img)
    cv2.waitKey(0)

cap.release()