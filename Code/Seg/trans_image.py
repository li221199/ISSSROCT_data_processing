#!/usr/bin/env python3 
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from PIL import Image
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
data1_1=255*(data1_1-min)/(max-min)
data1_2=255*(data1_2-min)/(max-min)
data1_3=255*(data1_3-min)/(max-min)
data1_4=255*(data1_4-min)/(max-min)
data1_5=255*(data1_5-min)/(max-min)
#print(data1_1)

im = Image.fromarray(data1_1)
im = im.convert('L')  # 这样才能转为灰度图，如果是彩色图则改L为‘RGB’
im.save('outfile1.png')

#========================自适应阈值——大津阈值法==============================================
img = cv2.imread('outfile1.png', 0)
# 固定阈值法
ret1, th1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
# Otsu阈值法
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 先进行高斯滤波，再使用Otsu阈值法
blur = cv2.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original', 'Histogram', 'Global(v=100)',
          'Original', 'Histogram', "Otsu's",
          'Gaussian filtered Image', 'Histogram', "Otsu's"]

for i in range(3):
    # 绘制原图
    plt.subplot(3, 3, i * 3 + 1)
    plt.imshow(images[i * 3], 'gray')
    plt.title(titles[i * 3], fontsize=8)
    plt.xticks([]), plt.yticks([])

    # 绘制直方图plt.hist, ravel函数将数组降成一维
    plt.subplot(3, 3, i * 3 + 2)
    plt.hist(images[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1], fontsize=8)
    plt.xticks([]), plt.yticks([])

    # 绘制阈值图
    plt.subplot(3, 3, i * 3 + 3)
    plt.imshow(images[i * 3 + 2], 'gray')
    plt.title(titles[i * 3 + 2], fontsize=8)
    plt.xticks([]), plt.yticks([])

    cv2.imwrite('adapt'+str(i)+'.png',images[i * 3 + 2])

plt.show()


#========================sobel算子法==============================================
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

cv2.imwrite('sobelx'+'.png',sobelx)
cv2.imwrite('sobely'+'.png',sobely)

plt.show()


#=========================生长法====================================================
