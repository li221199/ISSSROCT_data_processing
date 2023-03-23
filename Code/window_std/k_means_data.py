#!/usr/bin/env python3 
# -*- coding:utf-8 -*-

#本代码用于kmeans方法得到的图像进行ab点提取、厚度计算、std等数据分析、箱线图绘制

import numpy as np
import cv2
import pandas as pd

img1 = cv2.imread('D:/Code/Python_Code/Seg/k_means_result/1.png', cv2.IMREAD_GRAYSCALE).T
img2 = cv2.imread('D:/Code/Python_Code/Seg/k_means_result/2.png', cv2.IMREAD_GRAYSCALE).T
img3 = cv2.imread('D:/Code/Python_Code/Seg/k_means_result/3.png', cv2.IMREAD_GRAYSCALE).T
img4 = cv2.imread('D:/Code/Python_Code/Seg/k_means_result/4.png', cv2.IMREAD_GRAYSCALE).T
img5 = cv2.imread('D:/Code/Python_Code/Seg/k_means_result/5.png', cv2.IMREAD_GRAYSCALE).T

img1_avg=np.zeros((50,2032))
img2_avg=np.zeros((50,2032))
img3_avg=np.zeros((50,2032))
img4_avg=np.zeros((50,2032))
img5_avg=np.zeros((50,2032))

#十个为一组进行平均
for i in range(50):
    img1_avg[i]=np.mean(img1[i*10:(i+1)*10,:],axis=0)
    img2_avg[i] = np.mean(img2[i * 10:(i + 1) * 10, :], axis=0)
    img3_avg[i] = np.mean(img3[i * 10:(i + 1) * 10, :], axis=0)
    img4_avg[i] = np.mean(img4[i * 10:(i + 1) * 10, :], axis=0)
    img5_avg[i] = np.mean(img5[i * 10:(i + 1) * 10, :], axis=0)
#print(img1_avg)

#寻找五十组的ab点位置并保存
def find_ab(img_avg):
    a_position=0
    b_position=2031
    for i in range(2032):
        if img_avg[a_position]>200:
            a_position+=1
        if img_avg[b_position]>200:
            b_position-=1
    return a_position,b_position
def ab_position(img1_avg,img2_avg,img3_avg,img4_avg,img5_avg,num):
    a1_1,b1_1=find_ab(img1_avg[num])
    a1_2,b1_2=find_ab(img2_avg[num])
    a1_3,b1_3=find_ab(img3_avg[num])
    a1_4,b1_4=find_ab(img4_avg[num])
    a1_5,b1_5=find_ab(img5_avg[num])
    return a1_1,b1_1,a1_2,b1_2,a1_3,b1_3,a1_4,b1_4,a1_5,b1_5
position=np.zeros((50,10))
for i in range(50):
    position[i]=ab_position(img1_avg,img2_avg,img3_avg,img4_avg,img5_avg,i)
#print(position)
#pd.DataFrame(position).to_csv('kmeans_ab_point_pos.csv')    #50组ab点存为csv文件

#######