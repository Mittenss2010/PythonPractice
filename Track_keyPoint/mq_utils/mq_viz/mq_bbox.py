"""Bounding box visualization functions."""
from __future__ import absolute_import, division

import random
import mxnet as mx
import cv2
#from .image import plot_image



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

    Returns Img

    """
    from matplotlib import pyplot as plt

    # 异常处理1：【labels不为空】and 【框数量与评分数量不匹配】
    # 异常处理2：【scores不为空】and 【框数量与评分数量不匹配】
    if labels is not None and not len(bboxes) == len(labels):
        raise ValueError('The length of labels and bboxes mismatch, {} vs {}'
                         .format(len(labels), len(bboxes)))
    if scores is not None and not len(bboxes) == len(scores):
        raise ValueError('The length of scores and bboxes mismatch, {} vs {}'
                         .format(len(scores), len(bboxes)))

    #ax = plot_image(img, ax=ax, reverse_rgb=reverse_rgb)        在底层绘制图像？？
    
    if len(bboxes) < 1:
        return img

    if isinstance(bboxes, mx.nd.NDArray):
        bboxes = bboxes.asnumpy()
    if isinstance(labels, mx.nd.NDArray):
        labels = labels.asnumpy()
    if isinstance(scores, mx.nd.NDArray):
        scores = scores.asnumpy()

    if not absolute_coordinates:
        # 使用图像shape 转换到绝对坐标系
        height = img.shape[0]
        width = img.shape[1]
        bboxes[:, (0, 2)] *= width
        bboxes[:, (1, 3)] *= height

    # 若未colors == None，使用随机colors
    if colors is None:
        colors = dict()
    
    resultList = list()
    scoreList = list()

    minIndex = None
    
    print(bboxes)
    print('*********************************************************************')

    for i, bbox in enumerate(bboxes):
        print(bbox)

        # 屏蔽评分小于阈值的目标
        # 标签<0??? 不存在的标签？？or背景
        if scores is not None and scores.flat[i] < thresh:
            continue
        if labels is not None and labels.flat[i] < 0:
            continue

        cls_id = int(labels.flat[i]) if labels is not None else -1
        
        # 选择画框的色彩
        if cls_id not in colors:
            if class_names is not None:
                colors[cls_id] = plt.get_cmap('hsv')(cls_id / len(class_names))
            else:
                colors[cls_id] = (random.random(), random.random(), random.random())
        # 初始化Rectangle 坐标
        xmin, ymin, xmax, ymax = [int(x) for x in bbox]
        print(xmin, ymin, xmax, ymax)
        height = img.shape[0]
        width = img.shape[1]
        #绘制矩形框
        cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(255,0,0), 2)

        # 绘制类别名称或概率评分
        if class_names is not None and cls_id < len(class_names):
            class_name = class_names[cls_id]
        else:
            class_name = str(cls_id) if cls_id >= 0 else ''
        score = '{:.3f}'.format(scores.flat[i]) if scores is not None else ''
		
        if class_name or score:
            # ax.text(xmin, ymin - 2,                                   
                    # '{:s}'.format(class_name,score),
                    # bbox=dict(facecolor=colors[cls_id], alpha=0.5),
                    # fontsize=8, 
                    # color='white')

            print('{:s} {:s}'.format(class_name, score))
            font = cv2.FONT_HERSHEY_SIMPLEX  # 定义字体
            img	= cv2.putText(img, '{:s}'.format(class_name), (xmin, ymin), font, 0.6, (255, 255, 0), 2)
            img	= cv2.putText(img, ' {:s}'.format(score), (xmin, ymin-15), font, 0.6, (0, 0, 255), 2)
                         # 图像，        文字内容，          坐标 ，         字体， 大小， 颜色，   字体厚度
            
            # 结果列表 输出信息，加入色彩信息
            resultList.append('类别: {:s}    评分: {:s}  '.format(class_name, score))
            scoreList.append(score)

        minIndex = scoreList.index(min(scoreList))

    return img , resultList, minIndex

def plot_bbox_track(img, tracking_objs_to_paint):
    '''
        功能：

        参数：img, 
              tracking_objs_to_paint: list 元素为((classnames, current_bbox, pridect_bbox))
        返回：img
    '''
    for tracking_obj in tracking_objs_to_paint:

        cur_bbox_index = 1
        pre_bbox_index = 2

        xmin, ymin, xmax, ymax = [int(x) for x in tracking_obj[cur_bbox_index]]
        cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,255,0), 1)

        font = cv2.FONT_HERSHEY_SIMPLEX  # 定义字体
        img	= cv2.putText(img, '{:s}'.format(tracking_obj[0]), (xmin, ymin), font, 0.6, (0, 255, 0), 1)

        xmin, ymin, xmax, ymax = [int(x) for x in tracking_obj[pre_bbox_index]]
        cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(255,0,0), 2)

        # print(tracking_obj)

    return img