#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def seg_kmeans_gray():
    # 读取图片
    img = cv2.imread('k_means_result/4.png', cv2.IMREAD_GRAYSCALE)
    img=np.where(img>125,0,255)
    cv2.imwrite('0302.png',img)


if __name__ == '__main__':
    seg_kmeans_gray()