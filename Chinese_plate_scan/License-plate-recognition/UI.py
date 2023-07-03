# -*- coding:utf-8 -*-
# author: DuanshengLiu
import cv2
import numpy as np
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from tensorflow import keras
from core import locate_and_correct
from Unet import unet_predict
from CNN import cnn_predict


class Window:
    def __init__(self, win, ww, wh):
        self.win = win
        self.ww = ww
        self.wh = wh
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, 200, 50))  # 界面启动时的初始位置
        self.win.title("车牌定位，矫正和识别软件---by DuanshengLiu")
        self.img_src_path = None

        self.label_src = Label(self.win, text='原图:', font=('微软雅黑', 13)).place(x=0, y=0)
        self.label_lic1 = Label(self.win, text='车牌区域1:', font=('微软雅黑', 13)).place(x=615, y=0)
        self.label_pred1 = Label(self.win, text='识别结果1:', font=('微软雅黑', 13)).place(x=615, y=85)
        self.label_lic2 = Label(self.win, text='车牌区域2:', font=('微软雅黑', 13)).place(x=615, y=180)
        self.label_pred2 = Label(self.win, text='识别结果2:', font=('微软雅黑', 13)).place(x=615, y=265)
        self.label_lic3 = Label(self.win, text='车牌区域3:', font=('微软雅黑', 13)).place(x=615, y=360)
        self.label_pred3 = Label(self.win, text='识别结果3:', font=('微软雅黑', 13)).place(x=615, y=445)

        self.can_src = Canvas(self.win, width=512, height=512, bg='white', relief='solid', borderwidth=1)  # 原图画布
        self.can_src.place(x=50, y=0)
        self.can_lic1 = Canvas(self.win, width=245, height=85, bg='white', relief='solid', borderwidth=1)  # 车牌区域1画布
        self.can_lic1.place(x=710, y=0)
        self.can_pred1 = Canvas(self.win, width=245, height=65, bg='white', relief='solid', borderwidth=1)  # 车牌识别1画布
        self.can_pred1.place(x=710, y=90)
        self.can_lic2 = Canvas(self.win, width=245, height=85, bg='white', relief='solid', borderwidth=1)  # 车牌区域2画布
        self.can_lic2.place(x=710, y=175)
        self.can_pred2 = Canvas(self.win, width=245, height=65, bg='white', relief='solid', borderwidth=1)  # 车牌识别2画布
        self.can_pred2.place(x=710, y=265)
        self.can_lic3 = Canvas(self.win, width=245, height=85, bg='white', relief='solid', borderwidth=1)  # 车牌区域3画布
        self.can_lic3.place(x=710, y=350)
        self.can_pred3 = Canvas(self.win, width=245, height=65, bg='white', relief='solid', borderwidth=1)  # 车牌识别3画布
        self.can_pred3.place(x=710, y=440)

        self.button1 = Button(self.win, text='选择文件', width=10, height=1, command=self.load_show_img)  # 选择文件按钮
        self.button1.place(x=680, y=wh - 30)
        self.button2 = Button(self.win, text='识别车牌', width=10, height=1, command=self.display)  # 识别车牌按钮
        self.button2.place(x=780, y=wh - 30)
        self.button3 = Button(self.win, text='清空所有', width=10, height=1, command=self.clear)  # 清空所有按钮
        self.button3.place(x=880, y=wh - 30)
        self.unet = keras.models.load_model('unet.h5')
        self.cnn = keras.models.load_model('cnn.h5')
        print('正在启动中,请稍等...')
        cnn_predict(self.cnn, [np.zeros((80, 240, 3))])
        print("已启动,开始识别吧！")


    def load_show_img(self):
        self.clear()
        sv = StringVar()
        sv.set(askopenfilename())
        self.img_src_path = Entry(self.win, state='readonly', text=sv).get()  # 获取到所打开的图片
        img_open = Image.open(self.img_src_path)
        if img_open.size[0] * img_open.size[1] > 240 * 80:
            img_open = img_open.resize((512, 512), Image.ANTIALIAS)
        self.img_Tk = ImageTk.PhotoImage(img_open)
        self.can_src.create_image(258, 258, image=self.img_Tk, anchor='center')

    def display(self):
        if self.img_src_path == None:  # 还没选择图片就进行预测
            self.can_pred1.create_text(32, 15, text='请选择图片', anchor='nw', font=('黑体', 28))
        else:
            img_src = cv2.imdecode(np.fromfile(self.img_src_path, dtype=np.uint8), -1)  # 从中文路径读取时用
            h, w = img_src.shape[0], img_src.shape[1]
            if h * w <= 240 * 80 and 2 <= w / h <= 5:  # 满足该条件说明可能整个图片就是一张车牌,无需定位,直接识别即可
                lic = cv2.resize(img_src, dsize=(240, 80), interpolation=cv2.INTER_AREA)[:, :, :3]  # 直接resize为(240,80)
                img_src_copy, Lic_img = img_src, [lic]
            else:  # 否则就需通过unet对img_src原图预测,得到img_mask,实现车牌定位,然后进行识别
                img_src, img_mask = unet_predict(self.unet, self.img_src_path)
                img_src_copy, Lic_img = locate_and_correct(img_src, img_mask)  # 利用core.py中的locate_and_correct函数进行车牌定位和矫正

            Lic_pred = cnn_predict(self.cnn, Lic_img)  # 利用cnn进行车牌的识别预测,Lic_pred中存的是元祖(车牌图片,识别结果)
            if Lic_pred:
                img = Image.fromarray(img_src_copy[:, :, ::-1])  # img_src_copy[:, :, ::-1]将BGR转为RGB
                self.img_Tk = ImageTk.PhotoImage(img)
                self.can_src.delete('all')  # 显示前,先清空画板
                self.can_src.create_image(258, 258, image=self.img_Tk,
                                          anchor='center')  # img_src_copy上绘制出了定位的车牌轮廓,将其显示在画板上
                for i, lic_pred in enumerate(Lic_pred):
                    if i == 0:
                        self.lic_Tk1 = ImageTk.PhotoImage(Image.fromarray(lic_pred[0][:, :, ::-1]))
                        self.can_lic1.create_image(5, 5, image=self.lic_Tk1, anchor='nw')
                        self.can_pred1.create_text(35, 15, text=lic_pred[1], anchor='nw', font=('黑体', 28))
                    elif i == 1:
                        self.lic_Tk2 = ImageTk.PhotoImage(Image.fromarray(lic_pred[0][:, :, ::-1]))
                        self.can_lic2.create_image(5, 5, image=self.lic_Tk2, anchor='nw')
                        self.can_pred2.create_text(40, 15, text=lic_pred[1], anchor='nw', font=('黑体', 28))
                    elif i == 2:
                        self.lic_Tk3 = ImageTk.PhotoImage(Image.fromarray(lic_pred[0][:, :, ::-1]))
                        self.can_lic3.create_image(5, 5, image=self.lic_Tk3, anchor='nw')
                        self.can_pred3.create_text(40, 15, text=lic_pred[1], anchor='nw', font=('黑体', 28))

            else:  # Lic_pred为空说明未能识别
                self.can_pred1.create_text(47, 15, text='未能识别', anchor='nw', font=('黑体', 27))

    def clear(self):
        self.can_src.delete('all')
        self.can_lic1.delete('all')
        self.can_lic2.delete('all')
        self.can_lic3.delete('all')
        self.can_pred1.delete('all')
        self.can_pred2.delete('all')
        self.can_pred3.delete('all')
        self.img_src_path = None

    def closeEvent():  # 关闭前清除session(),防止'NoneType' object is not callable
        keras.backend.clear_session()
        sys.exit()


if __name__ == '__main__':
    win = Tk()
    ww = 1000  # 窗口宽设定1000
    wh = 600  # 窗口高设定600
    Window(win, ww, wh)
    win.protocol("WM_DELETE_WINDOW", Window.closeEvent)
    win.mainloop()
