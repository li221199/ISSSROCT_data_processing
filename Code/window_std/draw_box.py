#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns


# 读取ab点位置
#df = pd.read_csv('SOM_ab_point_box.csv')
df = pd.read_csv('PSO_ab_point_box.csv')
#df = pd.read_csv('kmeans_ab_point_box.csv')
#df = pd.read_csv('ab_point_box_test.csv')
np_data=np.array(df)
np_data=np_data[:,1:3]
print(np_data)

#print(ab1_1)
#==============================绘制五种厚度的箱线图=========================================
#print(df1_1)
sns.boxplot(x=df["CLASS"],y=df["B"]-df["A"])
plt.suptitle('Box plot of five types of thickness') #在plt.show()前加这一行
plt.xlabel('Thickness category', fontsize=13)
plt.ylabel('Thickness', fontsize=13)
plt.show()


#==============================绘制五种厚度a点的箱线图=========================================
sns.boxplot(x=df["CLASS"],y=df["A"])
plt.suptitle('Box plot of five types of A points') #在plt.show()前加这一行
plt.xlabel('Thickness category', fontsize=15)
plt.ylabel('A position', fontsize=15)
plt.show()

#==============================绘制五种厚度b点的箱线图=========================================
sns.boxplot(x=df["CLASS"],y=df["B"])
plt.suptitle('Box plot of five types of B points') #在plt.show()前加这一行
plt.xlabel('Thickness category', fontsize=15)
plt.ylabel('B position', fontsize=15)
plt.show()


#==============================绘制五种厚度每种厚度的50组a点数据=======================================
#53412
x=range(50)
#np_data_a1=np_data[0:50,0]
#np_data_a2=np_data[50:100,0]
#np_data_a3=np_data[100:150,0]
#np_data_a4=np_data[150:200,0]
#np_data_a5=np_data[200:250,0]
np_data_a1=np_data[0:50,0]
np_data_a2=np_data[50:100,0]
np_data_a3=np_data[100:150,0]
np_data_a4=np_data[150:200,0]
np_data_a5=np_data[200:250,0]
plt.plot(x,np_data_a1,label='a1')
plt.plot(x,np_data_a2,label='a2')
plt.plot(x,np_data_a3,label='a3')
plt.plot(x,np_data_a4,label='a4')
plt.plot(x,np_data_a5,label='a5')
plt.show()


#==============================绘制五种厚度每种厚度的50组b点数据=======================================
np_data_b1=np_data[0:50,1]
np_data_b2=np_data[50:100,1]
np_data_b3=np_data[100:150,1]
np_data_b4=np_data[150:200,1]
np_data_b5=np_data[200:250,1]
plt.plot(x,np_data_b1,label='b1')
plt.plot(x,np_data_b2,label='b2')
plt.plot(x,np_data_b3,label='b3')
plt.plot(x,np_data_b4,label='b4')
plt.plot(x,np_data_b5,label='b5')
plt.show()