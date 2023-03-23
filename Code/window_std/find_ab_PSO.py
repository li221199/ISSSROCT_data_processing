#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import pandas as pd
from PIL import Image

data_csv1_1 = 'D:/Code/Python_Code/Seg/PSO_result/SA_Segmented1.csv'
data_csv1_2 = 'D:/Code/Python_Code/Seg/PSO_result/SA_Segmented2.csv'
data_csv1_3 = 'D:/Code/Python_Code/Seg/PSO_result/SA_Segmented3.csv'
data_csv1_4 = 'D:/Code/Python_Code/Seg/PSO_result/SA_Segmented4.csv'
data_csv1_5 = 'D:/Code/Python_Code/Seg/PSO_result/SA_Segmented5.csv'
data_pd1_1 = pd.read_csv(data_csv1_1, header=None)
data_pd1_2 = pd.read_csv(data_csv1_2, header=None)
data_pd1_3 = pd.read_csv(data_csv1_3, header=None)
data_pd1_4 = pd.read_csv(data_csv1_4, header=None)
data_pd1_5 = pd.read_csv(data_csv1_5, header=None)

#print(data_pd1_1.shape)

data1 = np.array(data_pd1_1)
data2 = np.array(data_pd1_2)
data3 = np.array(data_pd1_3)
data4 = np.array(data_pd1_4)
data5 = np.array(data_pd1_5)


def trans_one_to_255(data):
    data[data == 2] = 255
    data[data == 1] = 0
    return data
def trans_one_to_255_2(data):
    data[data == 2] = 0
    data[data == 1] = 255
    return data

#========================================转为图片=================================================
data1 = trans_one_to_255(data1).astype(float)
data2 = trans_one_to_255(data2).astype(float)
data3 = trans_one_to_255(data3).astype(float)
data4 = trans_one_to_255_2(data4).astype(float)
data5 = trans_one_to_255_2(data5).astype(float)

#im1 = Image.fromarray(data1)
#im2 = Image.fromarray(data2)
#im3 = Image.fromarray(data3)
#im4 = Image.fromarray(data4)
#im5 = Image.fromarray(data5)
#im1 = im1.convert('L')  # 这样才能转为灰度图，如果是彩色图则改L为‘RGB’
#im2 = im2.convert('L')
#im3 = im3.convert('L')
#im4 = im4.convert('L')
#im5 = im5.convert('L')

#im1.save('D:/Code/Python_Code/Seg/PSO_result/1.png')
#im2.save('D:/Code/Python_Code/Seg/PSO_result/2.png')
#im3.save('D:/Code/Python_Code/Seg/PSO_result/3.png')
#im4.save('D:/Code/Python_Code/Seg/PSO_result/4.png')
#im5.save('D:/Code/Python_Code/Seg/PSO_result/5.png')
#========================================转为图片=================================================

#=======================================find a b==================================================
print(data1.shape)
data1 = data1.T
data2 = data2.T
data3 = data3.T
data4 = data4.T
data5 = data5.T
def find_ab(img,num):
    a_position=0
    b_position=2031
    while(img[num,a_position]>150):
        a_position+=1
    while(img[num,b_position]>150):
        b_position-=1
    return a_position,b_position
def ab_position(image1_gray,image2_gray,image3_gray,image4_gray,image5_gray,num):
    a1_1,b1_1=find_ab(image1_gray,num)
    a1_2,b1_2=find_ab(image2_gray,num)
    a1_3,b1_3=find_ab(image3_gray,num)
    a1_4,b1_4=find_ab(image4_gray,num)
    a1_5,b1_5=find_ab(image5_gray,num)
    return a1_1,b1_1,a1_2,b1_2,a1_3,b1_3,a1_4,b1_4,a1_5,b1_5
position=np.zeros((500,10))
for i in range(500):
    position[i]=ab_position(data1,data2,data3,data4,data5,i)
print(position.shape)
position_mean=np.zeros((50,10))
for i in range(50):
    position_mean[i]=np.mean(position[i*10:(i+1)*10],axis=0)
print(position_mean.shape)
pd.DataFrame(position_mean).to_csv('PSO_ab_point_pos.csv')###kmeans
#=======================================find a b==================================================