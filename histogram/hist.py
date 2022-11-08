# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 12:16:09 2022

@author: bernardogoltz
"""

import cv2 as cv 
import matplotlib.pyplot as plt

def grey_hist(image):
    plt.hist(img.ravel(),256,[0,256]) 
    

img = cv.imread('C:/Users/angel/OneDrive/Documentos/computer-vision/Computer-Vision/resources/images/Imagens/Cinza.jpg')

grey_hist(img)



