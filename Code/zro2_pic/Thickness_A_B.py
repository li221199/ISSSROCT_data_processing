#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
# 本文件用于提取氧化锆厚度的ab点信息，绘制相对厚度分布，ab点分布
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import cv2
from math import log, exp

# ================================一.提取ab点信息=================================
df4 = pd.read_csv('D:/Code/Python_Code/window_std/SOM_ab_point_box.csv')
df3 = pd.read_csv('D:/Code/Python_Code/window_std/PSO_ab_point_box.csv')
df2 = pd.read_csv('D:/Code/Python_Code/window_std/kmeans_ab_point_box.csv')
df1 = pd.read_csv('D:/Code/Python_Code/window_std/ab_point_box_test.csv')
# print(df1.shape,df2.shape,df3.shape,df4.shape)
data_ab1 = np.array(df1)
data_ab1 = data_ab1[:, 1:3]
# print(data_ab1.shape)
data_ab2 = np.array(df2)
data_ab2 = data_ab2[:, 1:3]
data_ab3 = np.array(df3)
data_ab3 = data_ab3[:, 1:3]
data_ab4 = np.array(df4)
data_ab4 = data_ab4[:, 1:3]
# ================================一.提取ab点信息=================================


# ================================二.绝对厚度信息=================================
thickness1 = data_ab1[:, 1] - data_ab1[:, 0]
thickness2 = data_ab2[:, 1] - data_ab2[:, 0]
thickness3 = data_ab3[:, 1] - data_ab3[:, 0]
thickness4 = data_ab4[:, 1] - data_ab4[:, 0]
# ======四种方法对应的5-45的四个相对厚度
thick1_1 = thickness1[0:50]
thick1_2 = thickness1[50:100]
thick1_3 = thickness1[100:150]
thick1_4 = thickness1[150:200]
thick1_5 = thickness1[200:250]
# print(thick1_1.shape)
thick2_1 = thickness2[0:50]
thick2_2 = thickness2[50:100]
thick2_3 = thickness2[100:150]
thick2_4 = thickness2[150:200]
thick2_5 = thickness2[200:250]
# print(thick1_1.shape)
thick3_1 = thickness3[0:50]
thick3_2 = thickness3[50:100]
thick3_3 = thickness3[100:150]
thick3_4 = thickness3[150:200]
thick3_5 = thickness3[200:250]
# print(thick1_1.shape)
thick4_1 = thickness4[0:50]
thick4_2 = thickness4[50:100]
thick4_3 = thickness4[100:150]
thick4_4 = thickness4[150:200]
thick4_5 = thickness4[200:250]
# print(thick1_1.shape)
# print(thick1_2,thick2_2,thick3_2,thick4_2)
# ======matplot绘制箱线图
# zero=np.zeros(50)
# lables = ['0µm', '5µm', '15µm', '30µm','45µm']
# plt.boxplot([thick1_2,thick1_1,thick1_3,thick1_4,thick1_5], labels=lables) #注意单词labels和lables
# plt.show()
# ================================二.相对厚度信息并绘图=================================


# ================================三.绘制ab点，和相对厚度一起=================================
# ======算法一
a1_1 = data_ab1[0:50, 0]
b1_1 = data_ab1[0:50, 1]
a1_2 = data_ab1[50:100, 0]
b1_2 = data_ab1[50:100, 1]
a1_3 = data_ab1[100:150, 0]
b1_3 = data_ab1[100:150, 1]
a1_4 = data_ab1[150:200, 0]
b1_4 = data_ab1[150:200, 1]
a1_5 = data_ab1[200:250, 0]
b1_5 = data_ab1[200:250, 1]
# ======算法二
a2_1 = data_ab2[0:50, 0]
b2_1 = data_ab2[0:50, 1]
a2_2 = data_ab2[50:100, 0]
b2_2 = data_ab2[50:100, 1]
a2_3 = data_ab2[100:150, 0]
b2_3 = data_ab2[100:150, 1]
a2_4 = data_ab2[150:200, 0]
b2_4 = data_ab2[150:200, 1]
a2_5 = data_ab2[200:250, 0]
b2_5 = data_ab2[200:250, 1]
# ======算法三
a3_1 = data_ab1[0:50, 0]
b3_1 = data_ab1[0:50, 1]
a3_2 = data_ab1[50:100, 0]
b3_2 = data_ab1[50:100, 1]
a3_3 = data_ab1[100:150, 0]
b3_3 = data_ab1[100:150, 1]
a3_4 = data_ab1[150:200, 0]
b3_4 = data_ab1[150:200, 1]
a3_5 = data_ab1[200:250, 0]
b3_5 = data_ab1[200:250, 1]
# ======算法四
a1_1 = data_ab1[0:50, 0]
b1_1 = data_ab1[0:50, 1]
a1_2 = data_ab1[50:100, 0]
b1_2 = data_ab1[50:100, 1]
a1_3 = data_ab1[100:150, 0]
b1_3 = data_ab1[100:150, 1]
a1_4 = data_ab1[150:200, 0]
b1_4 = data_ab1[150:200, 1]
a1_5 = data_ab1[200:250, 0]
b1_5 = data_ab1[200:250, 1]

# ======算法一统计算法的图片
fig, (ax1,ax2,ax3) = plt.subplots(3, 1, figsize=(6,4), sharex = True)
#ax1 = plt.subplot(311)
lables = ['0µm', '5µm', '15µm', '30µm', '45µm']
ax1.boxplot([thick1_2, thick1_1, thick1_3, thick1_4, thick1_5], labels=lables)  # 注意单词labels和lables
#min1 = np.min(a1_1)
# min2 = np.min(a1_2)
# min3 = np.min(a1_3)
# min4 = np.min(a1_4)
# min5 = np.min(a1_5)
#a_min=np.min(a1_2)
#b_min=np.min(b1_2)
a1_mean=np.mean(a1_1)
b1_mean=np.mean(b1_1)
a2_mean=np.mean(a1_2)
b2_mean=np.mean(b1_2)
a3_mean=np.mean(a1_3)
b3_mean=np.mean(b1_3)
a4_mean=np.mean(a1_4)
b4_mean=np.mean(b1_4)
a5_mean=np.mean(a1_5)
b5_mean=np.mean(b1_5)
#ax2 = plt.subplot(312)
#ax2.violinplot([a1_2 - a2_mean, a1_1 - a1_mean, a1_3 - a3_mean, a1_4 - a4_mean, a1_5 - a5_mean], showmeans=True, showmedians=True)
ax2.violinplot([a1_1 - a1_mean, a1_2 - a2_mean, a1_3 - a3_mean, a1_4 - a4_mean, a1_5 - a5_mean], showmeans=True, showmedians=True)
#ax3 = plt.subplot(313)
#ax3.violinplot([b1_2 - b2_mean, b1_1 - b1_mean, b1_3 - b3_mean, b1_4 - b4_mean, b1_5 - b5_mean], showmeans=True, showmedians=True)
ax3.violinplot([b1_1 - b1_mean, b1_2 - b2_mean, b1_3 - b3_mean, b1_4 - b4_mean, b1_5 - b5_mean], showmeans=True, showmedians=True)
plt.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=0.15,hspace=0)
plt.show()
# ================================三.绘制ab点，和相对厚度一起=================================
a1_1 = np.expand_dims(a1_1, 0)
b1_1 = np.expand_dims(b1_1, 0)
a1_2 = np.expand_dims(a1_2, 0)
b1_2 = np.expand_dims(b1_2, 0)
a1_3 = np.expand_dims(a1_3, 0)
b1_3 = np.expand_dims(b1_3, 0)
a1_4 = np.expand_dims(a1_4, 0)
b1_4 = np.expand_dims(b1_4, 0)
a1_5 = np.expand_dims(a1_5, 0)
b1_5 = np.expand_dims(b1_5, 0)
#position=np.concatenate([a1_2,b1_2,a1_1,b1_1,a1_3,b1_3,a1_4,b1_4,a1_5,b1_5])
#pd.DataFrame(position).to_csv('thick1.csv')
#position=np.concatenate([a1_1,b1_1,a1_2,b1_2,a1_3,b1_3,a1_4,b1_4,a1_5,b1_5])
#pd.DataFrame(position).to_csv('thick4.csv')