#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

#本文件用于读取OCT原始数据和二维图像数据并展示

#读取数据
#data_csv1_1='D:/Code/Project/OCT_data_seg/1213/4s/1-1/csv.csv'
#data_csv1_2='D:/Code/Project/OCT_data_seg/1213/4s/1-2/csv.csv'
#data_csv1_3='D:/Code/Project/OCT_data_seg/1213/4s/1-3/csv.csv'
#data_csv1_4='D:/Code/Project/OCT_data_seg/1213/4s/1-4/csv.csv'
#data_csv1_5='D:/Code/Project/OCT_data_seg/1213/4s/1-5/csv.csv'
data_raw1_1='D:/Code/Project/OCT_data_seg/1213/4s/1-1/raw.csv'
data_raw1_2='D:/Code/Project/OCT_data_seg/1213/4s/1-2/raw.csv'
data_raw1_3='D:/Code/Project/OCT_data_seg/1213/4s/1-3/raw.csv'
data_raw1_4='D:/Code/Project/OCT_data_seg/1213/4s/1-4/raw.csv'
data_raw1_5='D:/Code/Project/OCT_data_seg/1213/4s/1-5/raw.csv'
data_pd1_1=pd.read_csv(data_raw1_1,header=None)
data_pd1_2=pd.read_csv(data_raw1_2,header=None)
data_pd1_3=pd.read_csv(data_raw1_3,header=None)
data_pd1_4=pd.read_csv(data_raw1_4,header=None)
data_pd1_5=pd.read_csv(data_raw1_5,header=None)

#print(data_pd)
data1_1=np.array(data_pd1_1).T
data1_2=np.array(data_pd1_2).T
data1_3=np.array(data_pd1_3).T
data1_4=np.array(data_pd1_4).T
data1_5=np.array(data_pd1_5).T

print(data1_1.shape)
print(data1_1[0].shape)

x=range(8992)

#fig = plt.figure()     #和fig.tight_layout()使用调整子图行间距
#53412
axes1=plt.subplot(511)
axes1.plot(x, data1_5[7])
axes1.set_ylabel('intensity')
#axes1.set_xlabel('the length of raw data')
axes1.set_title('0μm')

axes2=plt.subplot(512)
axes2.plot(x, data1_3[7])
axes2.set_ylabel('intensity')
#axes2.set_xlabel('the length of raw data')
axes2.set_title('5μm')

axes3=plt.subplot(513)
axes3.plot(x, data1_4[7])
axes3.set_ylabel('intensity')
#axes3.set_xlabel('the length of raw data')
axes3.set_title('15μm')

axes4=plt.subplot(514)
axes4.plot(x, data1_1[7])
axes4.set_ylabel('intensity')
#axes4.set_xlabel('the length of raw data')
axes4.set_title('30μm')

axes5=plt.subplot(515)
axes5.plot(x, data1_2[7])
axes5.set_ylabel('intensity')
axes5.set_xlabel('the length of raw data')
axes5.set_title('45μm')

#fig.tight_layout()
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.6)

plt.show()

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
data1_1=np.array(data_pd1_1).T
data1_2=np.array(data_pd1_2).T
data1_3=np.array(data_pd1_3).T
data1_4=np.array(data_pd1_4).T
data1_5=np.array(data_pd1_5).T

print(data1_1.shape)
print(data1_1[0].shape)

x=range(2032)

#fig = plt.figure()     #和fig.tight_layout()使用调整子图行间距

axes1=plt.subplot(511)
axes1.plot(x, data1_5[7])
axes1.set_ylabel('intensity')
#axes1.set_xlabel('the length of raw data')
axes1.set_title('0μm')

axes2=plt.subplot(512)
axes2.plot(x, data1_3[7])
axes2.set_ylabel('intensity')
#axes2.set_xlabel('the length of raw data')
axes2.set_title('5μm')

axes3=plt.subplot(513)
axes3.plot(x, data1_4[7])
axes3.set_ylabel('intensity')
#axes3.set_xlabel('the length of raw data')
axes3.set_title('15μm')

axes4=plt.subplot(514)
axes4.plot(x, data1_1[7])
axes4.set_ylabel('intensity')
#axes4.set_xlabel('the length of raw data')
axes4.set_title('30μm')

axes5=plt.subplot(515)
axes5.plot(x, data1_2[7])
axes5.set_ylabel('intensity')
axes5.set_xlabel('the length of raw data')
axes5.set_title('45μm')

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.6)

plt.show()