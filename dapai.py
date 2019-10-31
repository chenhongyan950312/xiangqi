#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:57:25 2019

@author: chy
"""
import tkinter as tk
from PIL import Image, ImageTk

win = tk.Tk() #第一步，建立窗口
win.title('发牌程序') #第二步，给窗口起名字
win.geometry('800x600') #第三步，设定窗口的大小（长x宽）
cv = tk.Canvas(win, bg='green', width=800, height=600) # 第四步，在界面上组织图形,该画布上放置各种元素

cv.pack() #第五步，放置图形，常用的是pack和place两种方法
win.mainloop() #第六步，主窗口循环显示

img = Image.open(r'/home/chy/456.jpg') #读取扑克牌
imgs = ImageTk.PhotoImage(img)
#photo = ImageTk.PhotoImage(image)
cv.create_image((200, 80), image=imgs)

#button=Button(win,image=imgs,text="waring",command=win.quit)   
#button.image=imgs
#button.pack()       
#win.mainloop()




