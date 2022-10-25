# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 12:01:45 2022

@author: bernardogoltz
"""

from PIL import Image
from pylab import *


path = 'C:/Users/angel/OneDrive/Documentos/computer-vision/Computer-Vision/images/maltes.jpg'
maltese = Image.open(path)


out = maltese.resize((128,128))
out.rotate(45)
out.show()

im = array(Image.open('C:/Users/angel/OneDrive/Documentos/computer-vision/Computer-Vision/images/maltes.jpg'))
figure()
title("Megan??")
gray()
imshow(im)

x = [200,200,400,400]
y = [200,500,200,500]
plot(x,'r*')