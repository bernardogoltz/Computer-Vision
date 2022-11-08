# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:49:01 2022

@author: bernardogoltz
"""

import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np 

img = cv.imread('C:/Users/angel/OneDrive/Documentos/computer-vision/Computer-Vision/resources/images/Imagens/einstein.jpg',0)

img_equalizada = cv.equalizeHist(img)

print("\n{} Linhas\n{} Colunas".format(img_equalizada.shape[0] , img_equalizada.shape[1]))

linhas , colunas = img_equalizada.shape

mat = cv.getRotationMatrix2D((linhas/2,colunas/2),45,1)

img_rotacionada = cv.warpAffine(img_equalizada,mat,(colunas,linhas))

fig, ax = plt.subplots(1,2)
ax[0].imshow(img_equalizada,cmap = plt.cm.gray)
ax[0].set_title("Imagem normal")
ax[1].imshow(img_rotacionada,cmap = plt.cm.gray)
ax[1].set_title("Imagem rotacionada")


# translação 

#   matriz de translação (ou deslocamento)
matrix = np.float32([[1,0,100],[0,1,100]])
img_translacionada = cv.warpAffine(img_equalizada,matrix,(colunas,linhas))
plt.imshow(img_translacionada)

