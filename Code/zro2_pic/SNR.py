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

def SNR(thick):
    mean_thick=np.mean(thick)
    std_thick=np.std(thick)
    snr=mean_thick/std_thick
    return snr

snr1_1=SNR(thick1_1)
snr1_2=SNR(thick1_2)
snr1_3=SNR(thick1_3)
snr1_4=SNR(thick1_4)
snr1_5=SNR(thick1_5)

snr2_1=SNR(thick2_1)
snr2_2=SNR(thick2_2)
snr2_3=SNR(thick2_3)
snr2_4=SNR(thick2_4)
snr2_5=SNR(thick2_5)

snr3_1=SNR(thick3_1)
snr3_2=SNR(thick3_2)
snr3_3=SNR(thick3_3)
snr3_4=SNR(thick3_4)
snr3_5=SNR(thick3_5)

snr4_1=SNR(thick4_1)
snr4_2=SNR(thick4_2)
snr4_3=SNR(thick4_3)
snr4_4=SNR(thick4_4)
snr4_5=SNR(thick4_5)

x=range(5)
lables = ['0µm', '5µm', '15µm', '30µm', '45µm']

#ticks = plt.set_xticks([1,2,3,4,5]) # 设置刻度
#labels = plt.set_xticklabels(['one','two','three','four'],rotation = 30,fontsize = 'small') # 设置刻度标签

fig, ax = plt.subplots()
#ax.bar(x, y, label = "Proportion", color = "#468499")
#ax.set_title("% respondents accepting violence against women, by gender")
#ax.set_xlabel("Gender")
#ax.set_ylabel("Proportion %")
#ax.legend()
ax.set_xticklabels(['0µm', '5µm', '15µm', '30µm', '45µm'])
#ax1.set_xticklabels([str(i)+':00' for i in range(0,25,2)], rotation=0, fontsize='x-large')#fontproperties=myfont
#设置横轴 特定x值时显示刻度
ax.set_xticks([i for i in range(0,5,1)])
ax.plot(x,[snr1_1,snr1_2,snr1_3,snr1_4,snr1_5],marker='v',label="1")
ax.plot(x,[snr2_1,snr2_2,snr2_3,snr2_4,snr2_5],marker='o',label="2")
ax.plot(x,[snr3_1,snr3_2,snr3_3,snr3_4,snr3_5],marker='P',label="3")
ax.plot(x,[snr4_1,snr4_2,snr4_3,snr4_4,snr4_5],marker='d',label="4")
ax.legend(['Statsitics','Clustering','PSO','Neural Network'])     # 设置折线名称
#ax.scatter(x, [snr1_1,snr1_2,snr1_3,snr1_4,snr1_5], c='red')
plt.show()