###
#本文件用于OCT原始数据的去噪
###
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import pandas as pd
from scipy import stats

data_csv1_1 = 'D:/ProgramData/新建文件夹/待处理/FPGA_IFFT_data_270.csv'
data_csv1_2 = 'D:/ProgramData/新建文件夹/待处理/FPGA_IFFT_data_270_0.csv'
data_csv1_3 = 'D:/ProgramData/新建文件夹/待处理/FPGA_IFFT_data_1000.csv'
data_csv1_4 = 'D:/ProgramData/新建文件夹/待处理/FPGA_IFFT_data_1000_0.csv'
data_csv1_5 = 'D:/ProgramData/新建文件夹/待处理/FPGA_IFFT_data_2048.csv'
data_csv1_6 = 'D:/ProgramData/新建文件夹/待处理/FPGA_IFFT_data_2048_0.csv'
data_pd1_1 = pd.read_csv(data_csv1_1, header=None)
data_pd1_2 = pd.read_csv(data_csv1_2, header=None)
data_pd1_3 = pd.read_csv(data_csv1_3, header=None)
data_pd1_4 = pd.read_csv(data_csv1_4, header=None)
data_pd1_5 = pd.read_csv(data_csv1_5, header=None)
data_pd1_6 = pd.read_csv(data_csv1_6, header=None)
data1 = np.array(data_pd1_1).T.astype(int)
data2 = np.array(data_pd1_2).T.astype(int)
data3 = np.array(data_pd1_3).T.astype(int)
data4 = np.array(data_pd1_4).T.astype(int)
data5 = np.array(data_pd1_5).T.astype(int)
data6 = np.array(data_pd1_6).T.astype(int)


# print(len(data1[0]))
def remove_un(data):
    max=stats.mode(data)[0][0]
    return max
for i in range(2048):
    max=remove_un(data1[i])
    list1=np.where(data1[i]>max+10)
    if list1:
        data1=np.delete(data1,list1,axis=1)
    list2 = np.where(data1[i] < max - 10)
    if list2:
        data1=np.delete(data1,list2,axis=1)
print(data1.shape)

for i in range(2048):
    max=remove_un(data2[i])
    list1=np.where(data2[i]>max+10)
    if list1:
        data2=np.delete(data2,list1,axis=1)
    list2 = np.where(data2[i] < max - 10)
    if list2:
        data2=np.delete(data2,list2,axis=1)
print(data2.shape)

for i in range(2048):
    max=remove_un(data3[i])
    list1=np.where(data3[i]>max+10)
    if list1:
        data3=np.delete(data3,list1,axis=1)
    list2 = np.where(data3[i] < max - 10)
    if list2:
        data3=np.delete(data3,list2,axis=1)
print(data3.shape)

for i in range(2048):
    max=remove_un(data4[i])
    list1=np.where(data4[i]>max+10)
    if list1:
        data4=np.delete(data4,list1,axis=1)
    list2 = np.where(data4[i] < max - 10)
    if list2:
        data4=np.delete(data4,list2,axis=1)
print(data4.shape)

for i in range(2048):
    max=remove_un(data5[i])
    list1=np.where(data5[i]>max+10)
    if list1:
        data5=np.delete(data5,list1,axis=1)
    list2 = np.where(data5[i] < max - 10)
    if list2:
        data5=np.delete(data5,list2,axis=1)
print(data5.shape)

for i in range(2048):
    max=remove_un(data6[i])
    list1=np.where(data6[i]>max+10)
    if list1:
        data6=np.delete(data6,list1,axis=1)
    list2 = np.where(data6[i] < max - 10)
    if list2:
        data6=np.delete(data6,list2,axis=1)
print(data6.shape)

data1=data1.T
data2=data2.T
data3=data3.T
data4=data4.T
data5=data5.T
data6=data6.T
pd.DataFrame(data1).to_csv('171.csv')###kmeans
pd.DataFrame(data2).to_csv('172.csv')###kmeans
pd.DataFrame(data3).to_csv('173.csv')###kmeans
pd.DataFrame(data4).to_csv('174.csv')###kmeans
pd.DataFrame(data5).to_csv('175.csv')###kmeans
pd.DataFrame(data6).to_csv('176.csv')###kmeans
