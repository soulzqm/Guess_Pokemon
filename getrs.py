"""
This code is a part of Guess_Pokemon Project 
It converts 809 pokemon's wiki png images into 256*256 sized colored & shadow
forms
It preprocess and store the images used in the Guess_Pokemon game

output:

img1:pokemon resized colored images
    
img2: pokemon resized shawdow images

The 256x256 colorful images are store in 'Raw(256x256)' folder with the name 
format: No.+Name+_raw+.png

The 256x256 shadow images are store in 'Shadow(256x256)' folder with the name 
format: No.+Name+_s+.png

@author: qimin
"""


import os
import numpy as np 
from PIL import Image



def get_shadow(pokemon_img,path):
#-------this fucntion makes the pokemon's image into shadow configuration-----#     
    img1 = Image.open((path+pokemon_img))
    #uniformize and save the image as size 256*256
    img1 = img1.resize((256,256),Image.BILINEAR)
    img2 = img1.copy()
    
#change the pixels to of the pokemon to be black, while keeping background 
#transparent (a=0) as the orignial image 
    WIDTH, HEIGHT = 256,256
    for x in range (0, WIDTH):
        for y in range (0,HEIGHT):
            r, g, b,a = img1.getpixel((x,y))
            if a == 0:
                r=255
                g=255
                b=255
                img1.putpixel((x,y),(r,g,b,a))
            else:
                r=0
                g=0
                b=0
            img2.putpixel((x,y),(r,g,b,a))
    
    #save the processed image 
    newname1 = pokemon_img.replace(".png","_raw.png")
    newname2 = pokemon_img.replace(".png","_s.png")
    img1.save((path+"Raw(256x256)/"+newname1))
    img2.save((path+"Shadow(256x256)/"+newname2))

if __name__ == "__main__":
    path = "your path/Guess_Pokemon/"
    for file in os.listdir(path):
        get_shadow(file,path)