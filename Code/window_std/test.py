###此文件用户反转灰度图片和改变颜色

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import cv2
from math import log, exp
#path1='D:/Code/Python_Code/Seg/org/'
path1='D:/Code/Python_Code/Seg/SOM_result/'
org1=cv2.imread(path1+'ttt2_test1.bmp', cv2.IMREAD_GRAYSCALE)
org2=cv2.imread(path1+'ttt2_test2.bmp', cv2.IMREAD_GRAYSCALE)
org3=cv2.imread(path1+'ttt2_test3.bmp', cv2.IMREAD_GRAYSCALE)
org4=cv2.imread(path1+'ttt2_test4.bmp', cv2.IMREAD_GRAYSCALE)
org5=cv2.imread(path1+'ttt2_test5.bmp', cv2.IMREAD_GRAYSCALE)
#def change(org):
#    for i in range(2032):
#        for j in range(500):
#            if org[i,j]==0:
#                org[i,j]=100
#            if org[i,j]==255:
#                org[i,j]=0
#    for i in range(2032):
#        for j in range(500):
#            if org[i,j]==100:
#                org[i,j]=255
#    return org
def change2(org):
    for i in range(2032):
        for j in range(500):
            if org[i,j]>100:
                org[i,j]=0
            if org[i,j]>30:
                org[i,j]=255
    return org
org1=change2(org1)
org2=change2(org2)
org3=change2(org3)
org4=change2(org4)
org5=change2(org5)
cv2.imwrite(path1+'result1.png',org1)
cv2.imwrite(path1+'result2.png',org2)
cv2.imwrite(path1+'result3.png',org3)
cv2.imwrite(path1+'result4.png',org4)
cv2.imwrite(path1+'result5.png',org5)