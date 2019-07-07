"""Bounding box visualization functions."""
from __future__ import absolute_import, division


import random
import cv2

import mxnet as mx
import numpy as np
import matplotlib.pyplot as plt


def plot_bbox(img, bboxes, scores=None, labels=None, thresh=0.5,
              class_names=None, colors=None,
              reverse_rgb=False, absolute_coordinates=True):
    """Visualize bounding boxes.

    Parameters
    ----------
    img : numpy.ndarray or mxnet.nd.NDArray
        Image with shape `H, W, 3`.
    bboxes : numpy.ndarray or mxnet.nd.NDArray
        Bounding boxes with shape `N, 4`. Where `N` is the number of boxes.
    scores : numpy.ndarray or mxnet.nd.NDArray, optional
        Confidence scores of the provided `bboxes` with shape `N`.
    labels : numpy.ndarray or mxnet.nd.NDArray, optional
        Class labels of the provided `bboxes` with shape `N`.
    thresh : float, optional, default 0.5
        Display threshold if `scores` is provided. Scores with less than `thresh`
        will be ignored in display, this is visually more elegant if you have
        a large number of bounding boxes with very small scores.
    class_names : list of str, optional
        Description of parameter `class_names`.
    colors : dict, optional
        You can provide desired colors as {0: (255, 0, 0), 1:(0, 255, 0), ...}, otherwise
        random colors will be substituted.
    reverse_rgb : bool, optional
        Reverse RGB<->BGR orders if `True`.
    absolute_coordinates : bool
        If `True`, absolute coordinates will be considered, otherwise coordinates
        are interpreted as in range(0, 1).

    Returns
    -------
    Mat img

    """
    from matplotlib import pyplot as plt

    # 异常处理1：labels不为空，但是框数量与标签数不匹配
    # 异常处理2：scores不为空，但是框数量与评分数量不匹配
    if labels is not None and not len(bboxes) == len(labels):
        raise ValueError('The length of labels and bboxes mismatch, {} vs {}'
                         .format(len(labels), len(bboxes)))
    if scores is not None and not len(bboxes) == len(scores):
        raise ValueError('The length of scores and bboxes mismatch, {} vs {}'
                         .format(len(scores), len(bboxes)))

    if len(bboxes) < 1:
        return img

    if isinstance(bboxes, mx.nd.NDArray):
        bboxes = bboxes.asnumpy()
    if isinstance(labels, mx.nd.NDArray):
        labels = labels.asnumpy()
    if isinstance(scores, mx.nd.NDArray):
        scores = scores.asnumpy()

    if not absolute_coordinates:
        # convert to absolute coordinates using image shape
        height = img.shape[0]
        width = img.shape[1]
        bboxes[:, (0, 2)] *= width
        bboxes[:, (1, 3)] *= height

    # use random colors if None is provided
    if colors is None:
        colors = dict()
    
    for i, bbox in enumerate(bboxes):
        # 屏蔽评分小于阈值的目标
        # 标签<0??? 不存在的标签？？or背景
        if scores is not None and scores.flat[i] < thresh:
            continue
        if labels is not None and labels.flat[i] < 0:
            continue

        # 类别id？每个类别一种颜色
        cls_id = int(labels.flat[i]) if labels is not None else -1
        
        # 选择画框的色彩
        if cls_id not in colors:
            if class_names is not None:
                colors[cls_id] = plt.get_cmap('hsv')(cls_id / len(class_names))
            else:
                colors[cls_id] = (random.random(), random.random(), random.random())
        # 初始化Rectangle 坐标
        xmin, ymin, xmax, ymax = [int(x) for x in bbox]
        cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(255,0,0), 2)
        
        # 绘制类别名称或概率评分
        # if class_names is not None and cls_id < len(class_names):
        #     class_name = class_names[cls_id]
        # else:
        #     class_name = str(cls_id) if cls_id >= 0 else ''
        # score = '{:.3f}'.format(scores.flat[i]) if scores is not None else ''
        # if class_name or score:
        #     ax.text(xmin, ymin - 2,                                   
        #             '{:s}'.format(class_name),
        #             bbox=dict(facecolor=colors[cls_id], alpha=0.5),
        #             fontsize=8, 
        #             color='white')
        #             #             ax.text(xmin, ymin - 2,
        #             # '{:s} {:s}'.format(class_name, score),
        #             # bbox=dict(facecolor=colors[cls_id], alpha=0.5),
        #             # fontsize=12, 
        #             # color='white')
        #     print('{:s} {:s}'.format(class_name, score))
    return img




def plot_keypoints(img, coords, confidence, class_ids, bboxes, scores,
                   box_thresh=0.5, keypoint_thresh=0.2, **kwargs):
    """Visualize keypoints.

    Parameters
    ----------
    img : numpy.ndarray or mxnet.nd.NDArray
        Image with shape `H, W, 3`.
    coords : numpy.ndarray or mxnet.nd.NDArray
        Array with shape `Batch, N_Joints, 2`.
    confidence : numpy.ndarray or mxnet.nd.NDArray
        Array with shape `Batch, N_Joints, 1`.
    class_ids : numpy.ndarray or mxnet.nd.NDArray
        Class IDs.
    bboxes : numpy.ndarray or mxnet.nd.NDArray
        Bounding boxes with shape `N, 4`. Where `N` is the number of boxes.
    scores : numpy.ndarray or mxnet.nd.NDArray, optional
        Confidence scores of the provided `bboxes` with shape `N`.
    box_thresh : float, optional, default 0.5
        Display threshold if `scores` is provided. Scores with less than `box_thresh`
        will be ignored in display.
    keypoint_thresh : float, optional, default 0.2
        Keypoints with confidence less than `keypoint_thresh` will be ignored in display.
  
    Returns
    -------
    Mat img

    """
    if isinstance(coords, mx.nd.NDArray):
        coords = coords.asnumpy()
    if isinstance(class_ids, mx.nd.NDArray):
        class_ids = class_ids.asnumpy()
    if isinstance(bboxes, mx.nd.NDArray):
        bboxes = bboxes.asnumpy()
    if isinstance(scores, mx.nd.NDArray):
        scores = scores.asnumpy()
    if isinstance(confidence, mx.nd.NDArray):
        confidence = confidence.asnumpy()

    joint_visible = confidence[:, :, 0] > keypoint_thresh

    joint_pairs = [[0, 1], [1, 3], [0, 2], [2, 4],
                   [5, 6], [5, 7], [7, 9], [6, 8], [8, 10],
                   [5, 11], [6, 12], [11, 12],
                   [11, 13], [12, 14], [13, 15], [14, 16]]

    person_ind = class_ids[0] == 0

    colors = {0: (255, 0, 0), 1:(0, 255, 0)}
    img = plot_bbox(img, 
                   bboxes[0][person_ind[:, 0]],
                   scores[0][person_ind[:, 0]],
                   thresh=box_thresh, 
                   colors=colors,
                   **kwargs)

    
    # 画框
    # 构造 colormap_index
    colormap_index = np.linspace(0, 1, len(joint_pairs))

    for i in range(coords.shape[0]):     # 遍历人类目标个数，坐标组 
        pts = coords[i]                  # 获取点集合
        # print("***********************************************************")
        # print("pts.count = " + str(len(pts)))
        # print("pts.shape = " + str(pts.shape))
        # print("colormap_index = " + str(colormap_index))
        # print("joint_pairs = " + str(joint_pairs))
        # print("***********************************************************")

        cyc_count = 0
        for cm_ind, jp in zip(colormap_index, joint_pairs):
            cyc_count+=1
            # print("第几个点:" + str(cyc_count))
            # print("cm_ind :" + str(cm_ind))
            # print("jp :" + str(jp))
            if joint_visible[i, jp[0]] and joint_visible[i, jp[1]]:
                # 画线
                # 起点：(x,y) = (pts[jp, 0][0], pts[jp, 1][0])
                # 终点：(x,y) = (pts[jp, 0][1], pts[jp, 1][y])
                color = (random.random()*255, random.random()*255, random.random()*255)
                cv2.line(img,(pts[jp, 0][0], pts[jp, 1][0]),(pts[jp, 0][1], pts[jp, 1][1]),color,2)
                # print("两点位置:" + str(pts[jp, 0]) + str(pts[jp, 1]))
                # print("第几个点:" + str(cyc_count))

                # 传入x元组，传入y元组，绘制直线
                # ax.plot(pts[jp, 0], pts[jp, 1],linewidth=3.0, alpha=0.7, color=plt.cm.cool(cm_ind))
                # print("plot_data_input:" + str(pts[jp, 0]) + str(pts[jp, 1]))

                # 画点
                # (x,y)——对儿
                if cyc_count == 7 or cyc_count == 9:
                    cv2.circle(img,(pts[jp, 0][1],pts[jp, 1][1]),5,(255,255,0),-1)#圆，-1为向内填充
                if cyc_count == 15 or cyc_count == 16:
                    cv2.circle(img,(pts[jp, 0][1],pts[jp, 1][1]),5,(0,255,255),-1)#圆，-1为向内填充

                # cv2.circle(img,(pts[jp, 0][0],pts[jp, 1][0]),2,(0,255,255),-1) #圆，-1为向内填充
                # cv2.circle(img,(pts[jp, 0][1],pts[jp, 1][1]),2,(0,255,255),-1) #圆，-1为向内填充

                # 传入x元组，传入y元组，绘制点
                # ax.scatter(pts[jp, 0], pts[jp, 1], s=20)
                # print("scatter_data_input:" + str(pts[jp, 0]) + str(pts[jp, 1]))
    return img
