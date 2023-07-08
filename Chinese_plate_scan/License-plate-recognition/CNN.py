# -*- coding:utf-8 -*-
# author: DuanshengLiu
from tensorflow.keras import layers, losses, models
import numpy as np
import cv2
import os


def cnn_train():
    char_dict = {"京": 0, "沪": 1, "津": 2, "渝": 3, "冀": 4, "晋": 5, "蒙": 6, "辽": 7, "吉": 8, "黑": 9, "苏": 10,
                 "浙": 11, "皖": 12, "闽": 13, "赣": 14, "鲁": 15, "豫": 16, "鄂": 17, "湘": 18, "粤": 19, "桂": 20,
                 "琼": 21, "川": 22, "贵": 23, "云": 24, "藏": 25, "陕": 26, "甘": 27, "青": 28, "宁": 29, "新": 30,
                 "0": 31, "1": 32, "2": 33, "3": 34, "4": 35, "5": 36, "6": 37, "7": 38, "8": 39, "9": 40,
                 "A": 41, "B": 42, "C": 43, "D": 44, "E": 45, "F": 46, "G": 47, "H": 48, "J": 49, "K": 50,
                 "L": 51, "M": 52, "N": 53, "P": 54, "Q": 55, "R": 56, "S": 57, "T": 58, "U": 59, "V": 60,
                 "W": 61, "X": 62, "Y": 63, "Z": 64}

    # 读取数据集
    path = 'home/cnn_datasets/'  # 车牌号数据集路径(车牌图片宽240，高80)
    pic_name = sorted(os.listdir(path))
    n = len(pic_name)
    X_train, y_train = [], []
    for i in range(n):
        print("正在读取第%d张图片" % i)
        img = cv2.imdecode(np.fromfile(path + pic_name[i], dtype=np.uint8), -1)  # cv2.imshow无法读取中文路径图片，改用此方式
        label = [char_dict[name] for name in pic_name[i][0:7]]  # 图片名前7位为车牌标签
        X_train.append(img)
        y_train.append(label)
    X_train = np.array(X_train)
    y_train = [np.array(y_train)[:, i] for i in range(7)]  # y_train是长度为7的列表，其中每个都是shape为(n,)的ndarray，分别对应n张图片的第一个字符，第二个字符....第七个字符

    # cnn模型
    Input = layers.Input((80, 240, 3))  # 车牌图片shape(80,240,3)
    x = Input
    x = layers.Conv2D(filters=16, kernel_size=(3, 3), strides=1, padding='same', activation='relu')(x)
    x = layers.MaxPool2D(pool_size=(2, 2), padding='same', strides=2)(x)
    for i in range(3):
        x = layers.Conv2D(filters=32 * 2 ** i, kernel_size=(3, 3), padding='valid', activation='relu')(x)
        x = layers.Conv2D(filters=32 * 2 ** i, kernel_size=(3, 3), padding='valid', activation='relu')(x)
        x = layers.MaxPool2D(pool_size=(2, 2), padding='same', strides=2)(x)
        x = layers.Dropout(0.5)(x)
    x = layers.Flatten()(x)
    x = layers.Dropout(0.3)(x)
    Output = [layers.Dense(65, activation='softmax', name='c%d' % (i + 1))(x) for i in range(7)]  # 7个输出分别对应车牌7个字符，每个输出都为65个类别类概率
    model = models.Model(inputs=Input, outputs=Output)
    model.summary()
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',  # y_train未进行one-hot编码，所以loss选择sparse_categorical_crossentropy
                  metrics=['accuracy'])

    # 模型训练
    print("开始训练cnn")
    model.fit(X_train, y_train, epochs=35)  # 总loss为7个loss的和
    model.save('cnn.h5')
    print('cnn.h5保存成功!!!')


def cnn_predict(cnn, Lic_img):
    characters = ["京", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "皖", "闽", "赣", "鲁", "豫",
                  "鄂", "湘", "粤", "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新", "0", "1", "2",
                  "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M",
                  "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    Lic_pred = []
    for lic in Lic_img:
        lic_pred = cnn.predict(lic.reshape(1, 80, 240, 3))  # 预测形状应为(1,80,240,3)
        lic_pred = np.array(lic_pred).reshape(7, 65)  # 列表转为ndarray，形状为(7,65)
        if len(lic_pred[lic_pred >= 0.8]) >= 4:  # 统计其中预测概率值大于80%以上的个数，大于等于4个以上认为识别率高，识别成功
            chars = ''
            for arg in np.argmax(lic_pred, axis=1):  # 取每行中概率值最大的arg,将其转为字符
                chars += characters[arg]
            chars = chars[0:2] + '·' + chars[2:]
            Lic_pred.append((lic, chars))  # 将车牌和识别结果一并存入Lic_pred
    return Lic_pred
