# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 21:32:29 2022

@author: DELL
"""
import torch
import numpy as np
#创建张量
a=[1,2,3.]
b=torch.tensor(a)

c=np.random.normal((2,3))
c1=torch.tensor(c)

c=torch.ones_like(b)
c=torch.zeros_like(b)
c=torch.rand_like(b)
print(c)

#属性
b.dtype
b.shape
b.size

#cat对两个张量进行连接
a=torch.rand([2,2,])
b=torch.rand([3,3,])
#d=torch.cat([a,b],dim=1) #列续上，di=0为行连接

#张量的运算
#chunk函数，将张量分割成特定数目的张量，如果不能被整除，最后一个张量为余数
b1,b2=torch.chunk(b, chunks=2) #也可以设置dim的值
#gather 沿着某个维度取一些变量 （input，dim,index)
# out[i][j][k]=input[index][i][j][k]  dim=0
# out[i][j][k]=input[i][index][i][j][k]  dim=1
# out[i][j][k]=input[i][j][index][i][j][k]  dim=2

#reshape 维度改变，但是实际上的顺序并没有改变
#scatter_(dim,index,src) 函数
torch.full((2,4),1)#.scatter_(0,index,src) #从dim分析，将index的是src数据换掉full里面相对应数据，和gather类似
#split chunk只进行均分，split可以任意分配每组的数量
a=torch.rand((2,4))
torch.split(a,[1,1]) #分成两份分别是1，3数量

#squeeze 函数 把数量为1维度的移除掉
torch.reshape(a, [2,1,4])
aa=torch.zeros(2,1,3,1,2)
#torch.squeeze(a,dim=3)

#stack 函数 从不同的dim拼接,维度有扩充
torch.stack([a,b],dim=1)

#take(input,index) 函数将input的index位置取出
#tile(input, dim)  函数在dim维度进行复制


