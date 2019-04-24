# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 23:36:02 2019
This Code processes the wiki pokemon PNG images so that it converts the pixels
with high RGB values into low values and leave the background with high RGB values
this is for the binarization of the images and thresholding them to make greyscale
images to compare their shape in OpenCV modulus
@author: qimin
"""

import os
import numpy as np 
from PIL import Image



def get_filled(pokemon_img,path):
#-------this fucntion makes the pokemon's image into shadow configuration-----#     
    img = Image.open((path+pokemon_img))
    #uniformize and save the image as size 256*256
    
    newname1 = pokemon_img.replace(".png","_filled.png")
    
#change the pixels to of the pokemon to be black, while keeping background 
#transparent (a=0) as the orignial image 
    WIDTH, HEIGHT = img.size
    for x in range (0, WIDTH):
        for y in range (0,HEIGHT):
            r, g, b,a = img.getpixel((x,y))
            if a < 10:
                r=255
                g=255
                b=255
            elif r >120 or g > 120 or b > 120:
                r = 10
                g = 10
                b = 10
            img.putpixel((x,y),(r,g,b,a))
    
    
    img.save((path+"Filled/"+newname1))

if __name__ == "__main__":
    path = "The path where you extract Guess_Pokemon"
    for file in os.listdir(path):
        get_filled(file,path)
