# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:03:39 2022

@author: bernardogoltz
"""

import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

img = cv.imread('C:/Users/angel/OneDrive/Documentos/computer-vision/Computer-Vision/resources/images/Imagens/einstein.jpg',0)

img_resize = cv.resize(img,None,fx = 0.8,fy = 0.8,interpolation = cv.INTER_CUBIC)

cv.imshow("Imagem original",img)
cv.imshow("Imagem modificada",img_resize)

cv.waitKey(0)
cv.destroyAllWindows()