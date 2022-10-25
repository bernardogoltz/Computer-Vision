# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:32:42 2022

@author: bernardogoltz
"""
#importing PIL Image module (the most common module of the Library)
from PIL import Image

path = 'C:/Users/angel/OneDrive/Documentos/computer-vision/Computer-Vision/images/xing.jpeg'

#importing image
thiago = Image.open(path)


# basic convertions and rotations:
thiago = thiago.convert('L')
thiago = thiago.rotate(180)
thiago.thumbnail((200,100))

#crop method 
box = (10,10,10,10)
#(left,upper,right,lower)
region = thiago.crop(box)
region 
thiago.show()

out = thiago.resize(100,100)



