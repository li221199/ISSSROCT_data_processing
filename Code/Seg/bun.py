#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('1-2/adapt2.png', 0)
#print(img[0].shape)
j=0
k=2031
total=0
for i in range(500):
    while img[j][i]<150 and img[k][i]<150:
        if img[j][i]<150:
            j+=1
        if img[k][i]<150:
            k-=1
    total+=k-j
    j = 0
    k = 2031
total/=500
print(total)