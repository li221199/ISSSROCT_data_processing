#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
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
thick1_1 = thickness1[50:100]-thickness1[0:50]
thick1_2 = thickness1[100:150]-thickness1[0:50]
thick1_3 = thickness1[150:200]-thickness1[0:50]
thick1_4 = thickness1[200:250]-thickness1[0:50]
# print(thick1_1.shape)
thick2_1 = thickness2[50:100]-thickness2[0:50]
thick2_2 = thickness2[100:150]-thickness2[0:50]
thick2_3 = thickness2[150:200]-thickness2[0:50]
thick2_4 = thickness2[200:250]-thickness2[0:50]
# print(thick1_1.shape)
thick3_1 = thickness3[50:100]-thickness3[0:50]
thick3_2 = thickness3[100:150]-thickness3[0:50]
thick3_3 = thickness3[150:200]-thickness3[0:50]
thick3_4 = thickness3[200:250]-thickness3[0:50]
# print(thick1_1.shape)
thick4_1 = thickness4[50:100]-thickness4[0:50]
thick4_2 = thickness4[100:150]-thickness4[0:50]
thick4_3 = thickness4[150:200]-thickness4[0:50]
thick4_4 = thickness4[200:250]-thickness4[0:50]

thick_sens1=[np.mean(thick1_1),np.mean(thick1_2),np.mean(thick1_3),np.mean(thick1_4)]
thick_sens2=[np.mean(thick2_1),np.mean(thick2_2),np.mean(thick2_3),np.mean(thick2_4)]
thick_sens3=[np.mean(thick3_1),np.mean(thick3_2),np.mean(thick3_3),np.mean(thick3_4)]
thick_sens4=[np.mean(thick4_1),np.mean(thick4_2),np.mean(thick4_3),np.mean(thick4_4)]

x=range(4)
lables = ['5µm', '15µm', '30µm', '45µm']
fig, ax = plt.subplots()

ax.set_xticklabels(['5µm', '15µm', '30µm', '45µm'])

ax.set_xticks([i for i in range(0,5,1)])
ax.plot(x,thick_sens1,marker='v',label="1")
ax.plot(x,thick_sens2,marker='o',label="2")
ax.plot(x,thick_sens3,marker='P',label="3")
ax.plot(x,thick_sens4,marker='d',label="4")
ax.legend(['Statsitics','Clustering','PSO','Neural Network'])     # 设置折线名称
#ax.scatter(x, [snr1_1,snr1_2,snr1_3,snr1_4,snr1_5], c='red')
plt.show()