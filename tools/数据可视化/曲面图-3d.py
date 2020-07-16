# 以下两个函数的区别：

# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow') #绘面
# 1
# 和

# ax.scatter(x[1000:4000],y[1000:4000],z[1000:4000],c='r') #绘点
# 1
# 1、绘制3D曲面图
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:17:13 2015

@author: Eddy_zheng
"""

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()
