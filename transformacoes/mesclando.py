# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:29:17 2022

@author: bernardogoltz
"""
import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np 


path_superman = 'C:/Users/angel/OneDrive/Documentos/computer-vision/Computer-Vision/resources/images/Imagens/Superman.png'
path_batman = 'C:/Users/angel/OneDrive/Documentos/computer-vision/Computer-Vision/resources/images/Imagens/batman.png'

batman = cv.imread(path_batman,0)
superman = cv.imread(path_superman,0)

merged = cv.addWeighted(batman , 0.5 , superman , 0.4, gamma = 1)

plt.imshow(merged)
