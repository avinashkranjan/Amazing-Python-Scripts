# -*- coding:utf-8 -*-
# author: DuanshengLiu
from Unet import unet_train
from CNN import cnn_train

unet_train()#训练后得到unet.h5,用于车牌定位
cnn_train()#训练后得到cnn.h5，用于车牌识别
