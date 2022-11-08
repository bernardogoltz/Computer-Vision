# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:18:50 2022

@author: bernardogoltz
"""

import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

path = 'C:/Users/angel/OneDrive/Documentos/computer-vision/Computer-Vision/resources/images/Imagens/Superman.png'
path_batman = 'C:/Users/angel/OneDrive/Documentos/computer-vision/Computer-Vision/resources/images/Imagens/batman.png'

img = cv.imread(path,0)
img_2 = cv.imread(path_batman,0)

img_somada = cv.add(img,img_2)
img_subtraida = cv.subtract(img,img_2)

fig, ax = plt.subplots(1,2)
ax[0].imshow(img,cmap = plt.cm.gray)
ax[1].imshow(img_2,cmap = plt.cm.gray)

fig, ax = plt.subplots(1,2)
ax[0].imshow(img_somada,cmap = plt.cm.gray)
ax[1].imshow(img_subtraida,cmap = plt.cm.gray)

