#本文件用于k-means聚类进行图像分割，先进行数据读取，读取五类厚度数据之后进行聚类分割处理，输出待处理五类厚度图像和分割后结果
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image


def seg_kmeans_gray(img):
    # 读取图片
    #img = cv2.imread('name', cv2.IMREAD_GRAYSCALE)

    # 展平
    img_flat = img.reshape((img.shape[0] * img.shape[1], 1))
    img_flat = np.float32(img_flat)

    # 迭代参数
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER, 20, 0.5)
    flags = cv2.KMEANS_RANDOM_CENTERS

    # 进行聚类
    compactness, labels, centers = cv2.kmeans(img_flat, 2, None, criteria, 10, flags)

    # 显示结果
    img_output = labels.reshape((img.shape[0], img.shape[1]))
    plt.subplot(121), plt.imshow(img, 'gray'), plt.title('input')
    plt.subplot(122), plt.imshow(img_output, 'gray'), plt.title('kmeans')
    plt.show()
    return img_output


if __name__ == '__main__':
    # 读取数据
    data_csv1_1 = 'D:/Code/Project/OCT_data_seg/1213/4s/1-1/csv.csv'
    data_csv1_2 = 'D:/Code/Project/OCT_data_seg/1213/4s/1-2/csv.csv'
    data_csv1_3 = 'D:/Code/Project/OCT_data_seg/1213/4s/1-3/csv.csv'
    data_csv1_4 = 'D:/Code/Project/OCT_data_seg/1213/4s/1-4/csv.csv'
    data_csv1_5 = 'D:/Code/Project/OCT_data_seg/1213/4s/1-5/csv.csv'
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


    img1 = cv2.imread('k_means_result/outfile1.png', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('k_means_result/outfile2.png', cv2.IMREAD_GRAYSCALE)
    img3 = cv2.imread('k_means_result/outfile3.png', cv2.IMREAD_GRAYSCALE)
    img4 = cv2.imread('k_means_result/outfile4.png', cv2.IMREAD_GRAYSCALE)
    img5 = cv2.imread('k_means_result/outfile5.png', cv2.IMREAD_GRAYSCALE)

    img1=seg_kmeans_gray(img1)*100
    img2 = seg_kmeans_gray(img2) * 100
    img3 = seg_kmeans_gray(img3) * 100
    img4 = seg_kmeans_gray(img4) * 100
    img5 = seg_kmeans_gray(img5) * 100

    #print("aaa")
    pic1 = Image.fromarray(img1)
    #pic1 = pic1.convert('L')  # 这样才能转为灰度图，如果是彩色图则改L为‘RGB’
    pic1.save('k_means_result/result1.png')
    pic2 = Image.fromarray(img2)
    #pic2 = pic2.convert('L')  # 这样才能转为灰度图，如果是彩色图则改L为‘RGB’
    pic2.save('k_means_result/result2.png')
    pic3 = Image.fromarray(img3)
    #pic3 = pic3.convert('L')  # 这样才能转为灰度图，如果是彩色图则改L为‘RGB’
    pic3.save('k_means_result/result3.png')
    pic4 = Image.fromarray(img4)
    #pic4 = pic4.convert('L')  # 这样才能转为灰度图，如果是彩色图则改L为‘RGB’
    pic4.save('k_means_result/result4.png')
    pic5 = Image.fromarray(img5)
    #pic5 = pic5.convert('L')  # 这样才能转为灰度图，如果是彩色图则改L为‘RGB’
    pic5.save('k_means_result/result5.png')