# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 20:02:37 2022

@author: DELL
"""
#dataset and dataloaders

#构建自己的dataset，需要继承官方的dataset
#需要构建三个函数 __getitem__ __len__ __init__ 
# __init__ (self,磁盘路径，目录,transform, target_transform) transform可以在这里也可以自己写一个
#transform对图像预处理的函数，target_transform对label预处理的函数
# __len__ (self) return len(self.img.label)
# __getitem__ (self,idx) 
# 训练一个样本
# 结合模板进行仿写


#dataloder 通常传入dataset
from torch.utils.data import DataLoader
# Iterate through the DataLoder
# __init__ 常用的一些参数
# dataset 自定义的dataset； batch_size 默认为1； shuffle=true 打乱数据集合；
# sampler batch_sampler 以某种顺序从dataset取元素，自定义的采样方法，使用之后shuffle可以不用使用，即batch_size相关的不必再设置
# num_workers 设置进程的，=0为一个进程，collate_fn 对shuffle后的mini_batch再处理pad成同样的长度返回batch

