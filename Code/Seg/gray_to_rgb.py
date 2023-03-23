#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
import cv2
import cv2
import matplotlib.pyplot as plt
import numpy as np
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

# print(data_pd)
data1_1 = np.array(data_pd1_1)
data1_2 = np.array(data_pd1_2)
data1_3 = np.array(data_pd1_3)
data1_4 = np.array(data_pd1_4)
data1_5 = np.array(data_pd1_5)

# 归一化
max = np.nanmax([data1_1, data1_2, data1_3, data1_4, data1_5])
min = np.nanmin([data1_1, data1_2, data1_3, data1_4, data1_5])
data1_1 = 255 * (data1_1 - min) / (max - min)
data1_2 = 255 * (data1_2 - min) / (max - min)
data1_3 = 255 * (data1_3 - min) / (max - min)
data1_4 = 255 * (data1_4 - min) / (max - min)
data1_5 = 255 * (data1_5 - min) / (max - min)
# print(data1_1)

im4 = Image.fromarray(data1_1)
im5 = Image.fromarray(data1_2)
im2 = Image.fromarray(data1_3)
im3 = Image.fromarray(data1_4)
im1 = Image.fromarray(data1_5)
im1 = im1.convert('L')  # 这样才能转为灰度图，如果是彩色图则改L为‘RGB’
im2 = im2.convert('L')
im3 = im3.convert('L')
im4 = im4.convert('L')
im5 = im5.convert('L')

im1.save('k_means_result/outfile1.png')
im2.save('k_means_result/outfile2.png')
im3.save('k_means_result/outfile3.png')
im4.save('k_means_result/outfile4.png')
im5.save('k_means_result/outfile5.png')
