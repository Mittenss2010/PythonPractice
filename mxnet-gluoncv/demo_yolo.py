"""03. Predict with pre-trained YOLO models
==========================================

This article shows how to play with pre-trained YOLO models with only a few
lines of code.

First let's import some necessary libraries:
"""

from gluoncv import model_zoo, data, utils
from matplotlib import pyplot as plt

######################################################################
# 1.加载与训练模型
# -------------------------
# 获取使用 Darknet53 作为基础模型，在Pascal VOC 数据集上与训练的 YOLOv3 模型. 
# pretrained=True 时：从model zoo 自动下载模型
# 更多与训练模型，参见`../../model_zoo/index`.
net = model_zoo.get_model('yolo3_darknet53_voc', pretrained=True)

######################################################################
# 图像预处理
# --------------------
## 下载图像，并使用预先设置的数据变换，进行预处理
# 1. 这里缩放到短边为 512。You can feed an arbitrarily sized image.
# 2. YOLO的一个约束时输入的宽高要被32整除。
# 3. 若想同时加载多个图像，给函数 load_test 输入图像文件名列表，such as ``[im_fname1, im_fname2,...]`` 
# func:【gluoncv.data.transforms.presets.yolo.load_test】
#
# 函数返回2值：
# 1.NDArray with shape `(batch_size, RGB_channels, height, width)`
#   可直接作为模型的输入。
# 2.可用于绘制的 numpy images。

#   Since we only loaded a single image, the first dimension of `x` is 1.

# 输入url，返回文件名
# im_fname = utils.download('https://raw.githubusercontent.com/zhreshold/' +
#                           'mxnet-ssd/master/data/demo/dog.jpg',
#                           path='dog.jpg')
# print(im_fname)
x, img = data.transforms.presets.yolo.load_test('112.jpg', short=512)

print('Shape of pre-processed image:', x.shape)

######################################################################
# 推理和显示
# ---------------------
# 前向函数返回所有预测到的bboxes，及相应的IDs，scores
# Their shapes 分别是
# `(batch_size, num_bboxes, 1)`, 
# `(batch_size, num_bboxes, 1)`, 
# `(batch_size, num_bboxes, 4)`, respectively.
#
# 显示结果的函数
# func:`gluoncv.utils.viz.plot_bbox`
#  We slice the results for the first image and feed them into `plot_bbox`:

class_IDs, scores, bounding_boxs = net(x)
print(len(class_IDs[0]))
print(len(scores[0]))
print(len(bounding_boxs[0]))
for i in range(len(class_IDs[0])):
    print(scores[0][i])
    print(class_IDs[0][i])

ax = utils.viz.plot_bbox(img, 
                         bounding_boxs[0], 
                         scores[0],
                         class_IDs[0], 
                         class_names=net.classes)
plt.show()
