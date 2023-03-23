#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import pandas as pd

path='D:/Code/Python_Code/window_std/tmp/'
csv1=pd.read_csv(path+'kmeans_ab_point_box.csv',header=None)
csv2=pd.read_csv(path+'PSO_ab_point_box.csv',header=None)
csv3=pd.read_csv(path+'SOM_ab_point_box.csv',header=None)
print(csv1.shape)

data1=np.array(csv1)
data2=np.array(csv2)
data3=np.array(csv3)

data1_a=np.zeros(5)
data1_b=np.zeros(5)
data1_th=np.zeros(5)

data2_a=np.zeros(5)
data2_b=np.zeros(5)
data2_th=np.zeros(5)

data3_a=np.zeros(5)
data3_b=np.zeros(5)
data3_th=np.zeros(5)

for i in range(5):
    data1_a[i]=np.std(data1[i*50:(i+1)*50,0])
    data1_b[i]=np.std(data1[i*50:(i+1)*50,1])
    #thi1=csv1[i*50:(i+1)*50,1]-csv1[i*50:(i+1)*50,0]
    data1_th[i]=data1_a[i]+data1_b[i]

    data2_a[i] = np.std(data2[i * 50:(i + 1) * 50, 0])
    data2_b[i] = np.std(data2[i * 50:(i + 1) * 50, 1])
    data2_th[i] = data2_a[i] + data2_b[i]

    data3_a[i] = np.std(data3[i * 50:(i + 1) * 50, 0])
    data3_b[i] = np.std(data3[i * 50:(i + 1) * 50, 1])
    data3_th[i] = data3_a[i] + data3_b[i]


print(data1_a)
print(data2_a)
print(data3_a)
print("==================")
print(data1_b)
print(data2_b)
print(data3_b)
print("======================")
print(data1_th)
print(data2_th)
print(data3_th)
