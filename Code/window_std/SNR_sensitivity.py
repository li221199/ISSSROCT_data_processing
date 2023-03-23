#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import cv2
from math import log, exp

#=============================================SNR===============================================
#read image
path1='D:/Code/Python_Code/Seg/org/'
org1=cv2.imread(path1+'org1.png', cv2.IMREAD_GRAYSCALE).astype(float)
org2=cv2.imread(path1+'org2.png', cv2.IMREAD_GRAYSCALE).astype(float)
org3=cv2.imread(path1+'org3.png', cv2.IMREAD_GRAYSCALE).astype(float)
org4=cv2.imread(path1+'org4.png', cv2.IMREAD_GRAYSCALE).astype(float)
org5=cv2.imread(path1+'org5.png', cv2.IMREAD_GRAYSCALE).astype(float)
path2='D:/Code/Python_Code/Seg/PSO_result/'
imag1=cv2.imread(path2+'1.png', cv2.IMREAD_GRAYSCALE).astype(float)
imag2=cv2.imread(path2+'2.png', cv2.IMREAD_GRAYSCALE).astype(float)
imag3=cv2.imread(path2+'3.png', cv2.IMREAD_GRAYSCALE).astype(float)
imag4=cv2.imread(path2+'4.png', cv2.IMREAD_GRAYSCALE).astype(float)
imag5=cv2.imread(path2+'5.png', cv2.IMREAD_GRAYSCALE).astype(float)
def snr(org,image):
    tmp1 = 0
    tmp2 = 0
    for i in range(2032):
        for j in range(500):
            tmp1+=org[i,j]*org[i,j]
            tmp2+=(org[i,j]-image[i,j])*(org[i,j]-image[i,j])
            #print(tmp1,tmp2)
    SNR=10*log(tmp1/tmp2)
    return SNR
SNR1=snr(org1,imag1)
SNR2=snr(org2,imag2)
SNR3=snr(org3,imag3)
SNR4=snr(org4,imag4)
SNR5=snr(org5,imag5)
print(SNR1,SNR2,SNR3,SNR4,SNR5)
#=============================================SNR===============================================


#=============================================sensitivity===============================================

#=============================================sensitivity===============================================