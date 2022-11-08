# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:28:46 2022

@author: bernardogoltz
"""
import cv2 as cv 
import matplotlib.pyplot as plt 

img = cv.imread('C:/Users/angel/OneDrive/Documentos/computer-vision/Computer-Vision/resources/images/Imagens/einstein.jpg',0)

img_equalizada = cv.equalizeHist(img)

# imagem equalizada vs normal
fig, ax = plt.subplots(1,2)

ax[0].imshow(img,cmap = plt.cm.gray)
ax[0].set_title("Padrão")

ax[1].imshow(img_equalizada,cmap = plt.cm.gray)
ax[1].set_title("Equalizada")


# histograma equalizado vs normal
fig, ax = plt.subplots(1,2)

ax[0].hist(img.ravel(),256,[0,256])
ax[0].set_title("Padrão")

ax[1].hist(img_equalizada.ravel(),256,[0,256])
ax[1].set_title("Equalizada")