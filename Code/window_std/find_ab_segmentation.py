#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import pandas as pd

#===============================生成ab点文件====================================
#path="D:/Code/Python_Code/Seg/k_means_result/"###kmeans
path="D:/Code/Python_Code/Seg/SOM_result/"
image1=cv2.imread(path+"result1.png")
image2=cv2.imread(path+"result2.png")
image3=cv2.imread(path+"result3.png")
image4=cv2.imread(path+"result4.png")
image5=cv2.imread(path+"result5.png")
#print(image1.shape)
image1_gray = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY).T
image2_gray = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY).T
image3_gray = cv2.cvtColor(image3,cv2.COLOR_BGR2GRAY).T
image4_gray = cv2.cvtColor(image4,cv2.COLOR_BGR2GRAY).T
image5_gray = cv2.cvtColor(image5,cv2.COLOR_BGR2GRAY).T
#print(image1_gray.shape)
#print(image1_gray[0].shape)
#print(image1.shape)
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
    position[i]=ab_position(image1_gray,image2_gray,image3_gray,image4_gray,image5_gray,i)
print(position.shape)
position_mean=np.zeros((50,10))
for i in range(50):
    position_mean[i]=np.mean(position[i*10:(i+1)*10],axis=0)
print(position_mean.shape)
#pd.DataFrame(position_mean).to_csv('kmeans_ab_point_pos.csv')###kmeans
pd.DataFrame(position_mean).to_csv('SOM_ab_point_pos.csv')
#===============================生成ab点文件====================================



#===============================生成ab和厚度箱线图====================================
#draw_box.py
#===============================生成ab和厚度箱线图====================================