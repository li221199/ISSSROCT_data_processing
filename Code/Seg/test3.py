#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
#用于组装图片，拼接

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#读取数据
data1_1=cv2.imread('k_means_result/outfile1.png', cv2.IMREAD_GRAYSCALE)
data1_2=cv2.imread('k_means_result/outfile2.png', cv2.IMREAD_GRAYSCALE)
data1_3=cv2.imread('k_means_result/outfile3.png', cv2.IMREAD_GRAYSCALE)
data1_4=cv2.imread('k_means_result/outfile4.png', cv2.IMREAD_GRAYSCALE)
data1_5=cv2.imread('k_means_result/outfile5.png', cv2.IMREAD_GRAYSCALE)

data=np.hstack([data1_1,data1_2,data1_3,data1_4,data1_5])

cv2.imwrite('222.png',data)