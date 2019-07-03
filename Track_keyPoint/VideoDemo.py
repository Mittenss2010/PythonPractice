
from __future__ import division
import argparse, time, logging, os, math, tqdm, cv2

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
from gluoncv.utils.viz import cv_plot_image, cv_plot_keypoints

ctx = mx.gpu(0)
detector_name = "ssd_512_mobilenet1.0_coco"
detector = get_model(detector_name, pretrained=True, ctx=ctx)

detector.reset_class(classes=['person'], reuse_weights={'person':'person'})

estimator = get_model('simple_pose_resnet18_v1b', pretrained='ccd24037', ctx=ctx)

cap = cv2.VideoCapture(0)
time.sleep(1)  ### letting the camera autofocus

axes = None
num_frames = 1000

for i in range(num_frames):
    ret, frame = cap.read()

    frame = mx.nd.array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).astype('uint8')

    x, frame = gcv.data.transforms.presets.yolo.transform_test(frame, short=512, max_size=350)

    x = x.as_in_context(ctx)
    class_IDs, scores, bounding_boxs = detector(x)
    pose_input, upscale_bbox = detector_to_simple_pose(frame, class_IDs, scores, bounding_boxs,
                                                        output_shape=(128, 96), ctx=ctx)
    if len(upscale_bbox) > 0:
        predicted_heatmap = estimator(pose_input)
        pred_coords, confidence = heatmap_to_coord(predicted_heatmap, upscale_bbox)

        img = cv_plot_keypoints(frame, pred_coords, confidence, class_IDs, bounding_boxs, scores,
                                box_thresh=0.5, keypoint_thresh=0.2)
    cv_plot_image(img)
    cv2.waitKey(1)


cap.release()

# # 常规库
# import sys
# import os 
# import numpy as np
# import cv2
# import time

# sys.path.append('./src/')                       # 添加模块导入路径



# # 识别相关自定义库
# # import behavior_recognize
# from scene import Scene
# from info_class import FrameInfo

# # faster Rcnn 加速
# os.environ['MXNET_CUDNN_AUTOTUNE_DEFAULT'] = '0'

# # Mxnet 相关库
# import mxnet as mx
# import gluoncv as gcv
# from gluoncv.data.transforms import presets
# from gluoncv.data import VOCDetection
# import mq_utils


# # 初始化模型相关变量
# print('Loading Model and construct Network...')
# ctx = mx.gpu(0)
# VOCDetection.CLASSES = ('roi_zhuan_pan','ye_qi_da_qian_open','ye_qi_da_qian_close')
# class_names = VOCDetection.CLASSES
# thresh = 0.5
# net = gcv.model_zoo.get_model('ssd_512_resnet50_v1_voc', pretrained=False, pretrained_base=False)
# net.load_parameters('./ignore_params/ssd_512_resnet50_v1_voc_best.params')
# net.set_nms(0.25, 100)
# net.collect_params().reset_ctx(ctx = ctx)

# # 推理输入尺寸
# height = 720
# width = 1280

# short = 720
# max_size = 1280

# # 缩放操作会出现Bugs，首先使用opencv缩放，再输入检测
# # short = 360
# # max_size = 640

# # 构造视频相关参数
# print('Construct videoWriter Layout...')

# # 打开视频，获取视频参数
# video_path = './ignore_video/002.mp4'
# cap = cv2.VideoCapture(video_path)                # 文件名及格式
# return_value, frame = cap.read()                  # 视频读取

# video_out_path = './ignore_video/output.avi'
# fourcc = cv2.VideoWriter_fourcc(*'XVID')            
# videowriter = cv2.VideoWriter(video_out_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (frame.shape[1], frame.shape[0]))

# # Scene 构建全局类
# scene_01 = Scene()
# scene_01.register_rule()    #注册规则

# frameCount = 0
# while(frameCount<5000):
#     ret , frame = cap.read()
#     frameCount+=1

#     time_start = time.time()

#     #加载图像数据，返回Tensor
#     x, img = presets.ssd.transform_test(mx.nd.array(frame), short=short, max_size=max_size)
#     print("变换耗时：" + "{:.2f}".format((time.time() - time_start)*1000) + "ms")

#     x = x.as_in_context(ctx)
#     # 网络返回三个值，分别给标签，评分，框位置赋值
#     ids, scores, bboxes = [item[0].asnumpy() for item in net(x)]

#     # 界面绘制
#     # img = mq_utils.mq_viz.plot_bbox_track(img, scene_01.get_stableObj_toPaint())            # 获取稳定框，绘制矩形框

#     img, ret_list, minIndex = mq_utils.mq_viz.plot_bbox(img, bboxes, scores, ids, 
#                                                         thresh=0.5, 
#                                                         class_names=class_names)

#     # cv2.putText(result, text=info, org=(50, 70), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
#     #            fontScale=1, color=(255, 0, 0), thickness=2)
#     cv2.imshow("img", img)
    
#     # 文件输出
#     if cv2.waitKey(30) & 0xFF == ord('q'):  #按q键退出
#         break

# cap.release()
# videowriter.release()
# cv2.destroyAllWindows()
# print('Total FrameCount:' + str(frameCount))