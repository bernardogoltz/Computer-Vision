# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 12:37:34 2022

@author: bernardogoltz
"""

import cv2 as cv 
import matplotlib.pyplot as plt

path = 'C:/Users/angel/OneDrive/Documentos/computer-vision/Computer-Vision/resources/images/Imagens/colorida.jpg'
img = cv.imread(path)

azul, verde, vermelho = cv.split(img)

figure = plt.figure(figsize = (20,15))


axis_1 = figure.add_subplot(131)
axis_1.hist(azul.ravel(),256,[0,256])
plt.title("Histograma do canal azul")

axis_2 = figure.add_subplot(132)
axis_2.hist(verde.ravel(),256,[0,256])
plt.title("Histograma do canal verde")

axis_3 = figure.add_subplot(133)
axis_3.hist(vermelho.ravel(),256,[0,256])
plt.title("Histograma do canal vermelho")



plt.show()
