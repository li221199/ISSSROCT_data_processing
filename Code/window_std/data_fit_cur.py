#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

#读取数据
data_csv1_1='D:/Code/Project/OCT_data_seg/1213/4s/1-1/csv.csv'
data_csv1_2='D:/Code/Project/OCT_data_seg/1213/4s/1-2/csv.csv'
data_csv1_3='D:/Code/Project/OCT_data_seg/1213/4s/1-3/csv.csv'
data_csv1_4='D:/Code/Project/OCT_data_seg/1213/4s/1-4/csv.csv'
data_csv1_5='D:/Code/Project/OCT_data_seg/1213/4s/1-5/csv.csv'
data_pd1_1=pd.read_csv(data_csv1_1,header=None)
data_pd1_2=pd.read_csv(data_csv1_2,header=None)
data_pd1_3=pd.read_csv(data_csv1_3,header=None)
data_pd1_4=pd.read_csv(data_csv1_4,header=None)
data_pd1_5=pd.read_csv(data_csv1_5,header=None)

#print(data_pd)
data1_1=np.array(data_pd1_1)
data1_2=np.array(data_pd1_2)
data1_3=np.array(data_pd1_3)
data1_4=np.array(data_pd1_4)
data1_5=np.array(data_pd1_5)

#归一化
max=np.nanmax([data1_1,data1_2,data1_3,data1_4,data1_5])
min=np.nanmin([data1_1,data1_2,data1_3,data1_4,data1_5])
#data1_1=255*(data1_1-min)/(max-min)
#data1_2=255*(data1_2-min)/(max-min)
#data1_3=255*(data1_3-min)/(max-min)
#data1_4=255*(data1_4-min)/(max-min)
#data1_5=255*(data1_5-min)/(max-min)
#print(data1_1.shape)       #2032*500

window=np.zeros(10)
sample1_1=np.zeros(2022)

x1_1=range(2032)
y1_1=data1_1[:,0]
#plt.subplot(1, 3, 1)
plt.plot(x1_1,y1_1,color='r')
#plt.title('Original')       #, plt.xticks([]), plt.yticks([])

for i in range(2022):
    window

plt.show()