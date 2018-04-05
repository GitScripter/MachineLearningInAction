# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
from sklearn import svm
import numpy as np
from sklearn import model_selection
import matplotlib.pyplot as plt

#定义一个函数，将不同类别标签与数字相对应
def iris_type(s):
    class_label={b'Iris-setosa':0,b'Iris-versicolor':1,b'Iris-virginica':2}
    return class_label[s]

#导入数据
filepath='IRIS_dataset.txt'
data=np.loadtxt(filepath,dtype=float,delimiter=',',converters={4:iris_type})
#以上4个参数中分别表示：
#dtype=float 数据类型
#delimiter=',' 数据以什么分割符号分割数据
#converters={4:iris_type} 对某一列数据（第四列）进行某种类型的转换

# print(data)

#将原始数据集划分成训练集和测试集
X ,y=np.split(data,(4,),axis=1) #np.split 按照列（axis=1）进行分割，从第四列开始往后的作为y 数据，之前的作为X 数据
x=X[:,0:2] #在 X中取前两列作为特征（为了后面的可视化）
x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,random_state=1,test_size=0.3)
# 用train_test_split将数据分为训练集和测试集，测试集占总数据的30%（test_size=0.3),random_state是随机数种子（随机数种子：其实就是该组随机数的编号，在需要重复试验的时候，保证得到一组一样的随机数。比如你每次都填1，其他参数一样的情况下你得到的随机数组是一样的。但填0或不填，每次都会不一样。
# 随机数的产生取决于种子，随机数和种子之间的关系遵从以下两个规则：种子不同，产生不同的随机数；种子相同，即使实例不同也产生相同的随机数。）

#搭建模型




