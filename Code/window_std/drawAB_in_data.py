#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns


def redata(data_info):
# 平均化原始数据
    data = data_info
    data_mean = np.zeros((50, 2032))
    for i in range(50):
        data_mean[i] = np.mean(data[i * 10:i * 10 + 10, :], axis=0)
    return data_mean

def mean_std(data_mean):
# ==================================去除极值平均处理后的std=======================================
    std_mean = np.zeros((50, 2022))
    for i in range(2022):
        tmp = data_mean[:, i:i + 10]
        for j in range(50):
            tmp_delet = tmp[j]
            tmp_max = np.max(tmp_delet)
            tmp_min = np.min(tmp_delet)
            # if np.where(tmp[j]==tmp_max)
            tmp_delet = np.delete(tmp_delet, np.where(tmp_delet == tmp_max))
            tmp_delet = np.delete(tmp_delet, np.where(tmp_delet == tmp_min))
            std_mean[j, i] = np.mean(tmp_delet)
    return std_mean

# 读取ab点位置
df = pd.read_csv('ab_point_pos.csv')
# print(df)
data_ab = np.array(df)
data_ab = data_ab[:, 1:11]

# 读取原始数据
data_csv1_1 = 'D:/Code/Project/OCT_data_seg/1213/4s/1-1/csv.csv'
data_csv1_2 = 'D:/Code/Project/OCT_data_seg/1213/4s/1-2/csv.csv'
data_csv1_3 = 'D:/Code/Project/OCT_data_seg/1213/4s/1-3/csv.csv'
data_csv1_4 = 'D:/Code/Project/OCT_data_seg/1213/4s/1-4/csv.csv'
data_csv1_5 = 'D:/Code/Project/OCT_data_seg/1213/4s/1-5/csv.csv'
data_pd1_1 = pd.read_csv(data_csv1_1, header=None)
data_pd1_2 = pd.read_csv(data_csv1_2, header=None)
data_pd1_3 = pd.read_csv(data_csv1_3, header=None)
data_pd1_4 = pd.read_csv(data_csv1_4, header=None)
data_pd1_5 = pd.read_csv(data_csv1_5, header=None)

# print(data_pd)
data1_1 = np.array(data_pd1_1).T
data1_2 = np.array(data_pd1_2).T
data1_3 = np.array(data_pd1_3).T
data1_4 = np.array(data_pd1_4).T
data1_5 = np.array(data_pd1_5).T
# print(data1_1.shape)
data1_1=redata(data1_1)
data1_2=redata(data1_2)
data1_3=redata(data1_3)
data1_4=redata(data1_4)
data1_5=redata(data1_5)
#print(data1_1)
#=============================ab点数据信息及std数据信息==============================================
std1_1=mean_std(data1_1)
std1_2=mean_std(data1_2)
std1_3=mean_std(data1_3)
std1_4=mean_std(data1_4)
std1_5=mean_std(data1_5)
ab1_1=data_ab[:,0:2]
ab1_2=data_ab[:,2:4]
ab1_3=data_ab[:,4:6]
ab1_4=data_ab[:,6:8]
ab1_5=data_ab[:,8:10]
#print(ab1_1)

#================================绘制std_mean和ab点位置的图======================================
def std_mean_and_ab_pos(ab,rand,std_data,x):
    rand_a = int(ab[rand, 0])
    rand_b = int(ab[rand, 1])
    plt.plot(x, std_data[rand], color='b')
    plt.plot(rand_a, std_data[rand,rand_a], marker='o', color='coral')
    plt.plot(rand_b, std_data[rand,rand_b], marker='o', color='coral')
    plt.show()
def std_mean_and_ab_pos_col(axes,ab,rand,std_data,x):
    rand_a = int(ab[rand, 0])
    rand_b = int(ab[rand, 1])
    axes.plot(x, std_data[rand], color='b')
    axes.plot(rand_a, std_data[rand,rand_a], marker='o', color='coral')
    axes.plot(rand_b, std_data[rand,rand_b], marker='o', color='coral')
    axes.set_ylabel('intensity')
x=range(2022)
rand=random.randint(0,50)
print("the rand is: ",rand)
#一个是分开画图，一个是图像画在一起
#std_mean_and_ab_pos(ab1_1,rand,std1_1,x)
#std_mean_and_ab_pos(ab1_2,rand,std1_2,x)
#std_mean_and_ab_pos(ab1_3,rand,std1_3,x)
#std_mean_and_ab_pos(ab1_4,rand,std1_4,x)
#std_mean_and_ab_pos(ab1_5,rand,std1_5,x)
#厚度顺序53412
axes1=plt.subplot(511)
std_mean_and_ab_pos_col(axes1,ab1_5,rand,std1_5,x)
axes1.set_title('0μm')
axes2=plt.subplot(512)
std_mean_and_ab_pos_col(axes2,ab1_3,rand,std1_3,x)
axes2.set_title('5μm')
axes3=plt.subplot(513)
std_mean_and_ab_pos_col(axes3,ab1_4,rand,std1_4,x)
axes3.set_title('15μm')
axes4=plt.subplot(514)
std_mean_and_ab_pos_col(axes4,ab1_1,rand,std1_1,x)
axes4.set_title('30μm')
axes5=plt.subplot(515)
std_mean_and_ab_pos_col(axes5,ab1_2,rand,std1_2,x)
axes5.set_title('45μm')
axes5.set_xlabel('the length of 2D OCT')
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.6)
plt.show()



#========================绘制五种厚度值在50组平均数据中的方差变化=========================
thickness1_1=ab1_1[1]-ab1_1[0]
thickness1_2=ab1_2[1]-ab1_2[0]
thickness1_3=ab1_3[1]-ab1_3[0]
thickness1_4=ab1_4[1]-ab1_4[0]
thickness1_5=ab1_5[1]-ab1_5[0]
thi_std1_1=np.std(thickness1_1)
thi_std1_2=np.std(thickness1_2)
thi_std1_3=np.std(thickness1_3)
thi_std1_4=np.std(thickness1_4)
thi_std1_5=np.std(thickness1_5)
x=range(5)
y=[thi_std1_5,thi_std1_3,thi_std1_4,thi_std1_2,thi_std1_1]
#y=np.concatenate((thi_std1_1,thi_std1_2,thi_std1_3,thi_std1_4,thi_std1_5))
plt.plot(x,y)
plt.show()




