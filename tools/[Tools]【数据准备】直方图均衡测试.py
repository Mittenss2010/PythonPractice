import cv2
import numpy as np

# 读入图片
image = cv2.imread("7.jpg",0) # 363 236
eq = cv2.equalizeHist(image)

cv2.imshow("image", image) # 显示原始图片
cv2.imshow("Histogram Equalization", np.hstack([eq]))
# cv2.imwrite('.6-1.jpg',np.hstack([eq]))
cv2.waitKey(0)


# import plotly as py
# import plotly.graph_objs as go
# import numpy as np

# pyplt = py.offline.plot
# s1 = np.random.RandomState(1)
# x = s1.randn(1000)
# data = [go.Histogram(x=x,
#                        histnorm = 'probability')] 
# # y = x 水平直方图，histnorm='probability' y轴显示概率，没有则显示数目
# pyplt(data, filename='1.html')


# import numpy as np
# import matplotlib.mlab as mlab
# import matplotlib.pyplot as plt
# import pandas
# # Load dataset
# url ="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# names = ['sepal-length', 'sepal-width','petal-length', 'petal-width', 'class']
# dataset = pandas.read_csv(url, names=names)
# print(dataset.head(10))
# # descriptions
# print(dataset.describe())
# x = dataset.iloc[:,0] #提取第一列的sepal-length变量
# mu =np.mean(x) #计算均值
# sigma =np.std(x)
# mu,sigma

# num_bins = 30 #直方图柱子的数量

# n, bins, patches = plt.hist(x, num_bins,normed=1, facecolor='blue', alpha=0.5)
# #直方图函数，x为x轴的值，normed=1表示为概率密度，即和为一，绿色方块，色深参数0.5.返回n个概率，直方块左边线的x值，及各个方块对象
# y = mlab.normpdf(bins, mu, sigma)               #拟合一条最佳正态分布曲线y 
# plt.plot(bins, y, 'r--')                        #绘制y的曲线
# plt.xlabel('sepal-length')                      #绘制x轴
# plt.ylabel('Probability')                                   #绘制y轴
# plt.title(r'Histogram : $\mu=5.8433$,$\sigma=0.8253$')      #中文标题 u'xxx' 

# plt.subplots_adjust(left=0.15)#左边距 
# plt.show() 


