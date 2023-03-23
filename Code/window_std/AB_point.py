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
#window=np.zeros(16)
window_mean=np.zeros((50,2016))
std_window=np.zeros((50,2016))
pow_std_window=np.zeros((50,2013))
std=np.zeros((50,2022))
data=data1_1        #######################


data_mean=np.zeros((50,2032))
for i in range(50):
    data_mean[i]=np.mean(data[i*10:i*10+10,:],axis=0)
#print(data_mean.shape)     ##50*2032

for i in range(2016):
    window_mean[:,i]=np.mean(data_mean[:,i:i+16])
    std_window[:,i]=np.std(data_mean[:,i:i+16])
print(window_mean.shape)
print(std_window.shape)

#x1_1=range(2016)
#y1_1=std_window[0,:]
##plt.subplot(1, 3, 1)
#plt.plot(x1_1,y1_1,color='r')
##plt.title('Original')       #, plt.xticks([]), plt.yticks([])
#plt.show()
#pd.DataFrame(window_mean).to_csv('AB_point1_1.csv')      #########################################

#========================================对std求导
#data_pd=pd.DataFrame(std_window)
#print(data_pd.shape)       #50*2016(range范围)


#==================================二次求std
for i in range(2013):
    pow_std_window[:,i]=np.std(std_window[:,i:i+3])

#x1_1=range(2013)
#y1_1=pow_std_window[0,:]
##plt.subplot(1, 3, 1)
#plt.plot(x1_1,y1_1,color='r')
##plt.title('Original')       #, plt.xticks([]), plt.yticks([])
#plt.show()







#====================================================================================
#window=np.zeros(10)
std=np.zeros((50,2022))
data=data1_1        #######################


data_mean=np.zeros((50,2032))
for i in range(50):
    data_mean[i]=np.mean(data[i*10:i*10+10,:],axis=0)
#print(data_mean.shape)     ##50*2032
x1_1=range(2032)
y1_1=data_mean[0,:]
##plt.subplot(1, 3, 1)
plt.plot(x1_1,y1_1,color='r')
##plt.title('Original')       #, plt.xticks([]), plt.yticks([])
plt.show()
##=========================================std=========================================
for i in range(2022):
    std[:,i]=np.std(data_mean[:,i:i+10])
print(std)

x1_1_std=range(2022)
y1_1_std=std[0,:]
##plt.subplot(1, 3, 1)
#plt.plot(x1_1,y1_1,color='r')
##plt.title('Original')       #, plt.xticks([]), plt.yticks([])
#plt.show()
#pd.DataFrame(std).to_csv('std1_5.csv')      #########################################


#==================================去除极值=======================================
std_mean=np.zeros((50,2022))
for i in range(2022):
    tmp=data_mean[:,i:i+10]
    for j in range(50):
        tmp_delet=tmp[j]
        tmp_max=np.max(tmp_delet)
        tmp_min=np.min(tmp_delet)
        #if np.where(tmp[j]==tmp_max)
        tmp_delet=np.delete(tmp_delet,np.where(tmp_delet==tmp_max))
        tmp_delet=np.delete(tmp_delet,np.where(tmp_delet==tmp_min))
        std_mean[j,i]=np.mean(tmp_delet)
        #print(tmp_delet.shape)
    #tmp_max=np.max(tmp)
    #tmp_min=np.min(tmp)
    #tmp=np.delete(tmp,np.where(tmp==tmp_max))
    #tmp = np.delete(tmp, np.where(tmp == tmp_min))
    #std_mean[:,i]=np.mean(tmp)
#print(std_mean)
x1_1=range(2022)
y1_1=std_mean[0,:]
##plt.subplot(1, 3, 1)
plt.plot(x1_1,y1_1,color='r')
plt.plot(x1_1_std,y1_1_std,color='b')
##plt.title('Original')       #, plt.xticks([]), plt.yticks([])
#plt.show()
#================================找max及其周边区域==================================================
max_std=np.max(y1_1_std)
position=np.where(y1_1_std==max_std)[0]
print(type(position[0]))
plt.plot(x1_1_std[np.where(y1_1_std==max_std)[0][0]],max_std,marker='o', color='coral')
plt.show()
print(x1_1_std[np.where(y1_1_std==max_std)[0][0]],max_std)






