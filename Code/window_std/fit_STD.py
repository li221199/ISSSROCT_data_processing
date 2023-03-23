#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from scipy.optimize import curve_fit

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
data1_1=np.array(data_pd1_1).T
data1_2=np.array(data_pd1_2).T
data1_3=np.array(data_pd1_3).T
data1_4=np.array(data_pd1_4).T
data1_5=np.array(data_pd1_5).T

#归一化
max=np.nanmax([data1_1,data1_2,data1_3,data1_4,data1_5])
min=np.nanmin([data1_1,data1_2,data1_3,data1_4,data1_5])
#data1_1=255*(data1_1-min)/(max-min)
#data1_2=255*(data1_2-min)/(max-min)
#data1_3=255*(data1_3-min)/(max-min)
#data1_4=255*(data1_4-min)/(max-min)
#data1_5=255*(data1_5-min)/(max-min)
#print(data1_1.shape)       #500*2032

#====================================================================================
#window=np.zeros(10)
std=np.zeros((50,2022))
data=data1_1        ##############################


data_mean=np.zeros((50,2032))
for i in range(50):
    data_mean[i]=np.mean(data[i*10:i*10+10,:],axis=0)
#print(data_mean.shape)     ##50*2032

for i in range(2022):
    std[:,i]=np.std(data_mean[:,i:i+10])
print(std)

x1_1=range(2022)
y1_1=std[0,:]
##plt.subplot(1, 3, 1)
plt.plot(x1_1,y1_1,color='r')
##plt.title('Original')       #, plt.xticks([]), plt.yticks([])
plt.show()
#pd.DataFrame(std).to_csv('std1_5.csv')      ################################

######插值


######plotfit
x_plf=x1_1
y_plf=y1_1
p = np.poly1d(np.polyfit(x_plf, y_plf, 20))
print(np.polyfit(x_plf, y_plf, 20))
plt.plot(x1_1, y1_1, 'o', x_plf, y_plf, '-')
plt.show()

