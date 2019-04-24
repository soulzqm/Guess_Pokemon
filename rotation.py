# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 01:27:10 2019

@author: qimin
input:

angle: in degree, 0<angle<360
path: the folder address where contains both raw256x256 and shadow256x256 folders
pokemon_no: 1-809
#r,s: raw or shadow, raw = r, shadow = s

output:
correct_name : full name of the assign pokemon_no
wrong_names: three random full names of the similar pokemon in the list
img_s_rotation: rotated shadow png image (512x512)
img_r_rotation: rotated colored png image (512x512)    
"""
import random
import math
import cv2 as cv
import os
import numpy as np 
from PIL import Image

def rotate(path,pokemon_no,angle):
    
    
    #convert 1 to '001'    
    if pokemon_no < 10:
        no = '00' + str(pokemon_no)
    elif pokemon_no < 100:
        no = '0' + str(pokemon_no)
    else:
        no =  str(pokemon_no)
    
    
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path,i)) and no in i:
            name = i.replace('.png','')
    correct_name = name
    # read and get other three random similiar pokemon name from the txt list
    ptxt = open(path+'pokemonlist.txt','r')
    #get all similar pokemon no from the txt list

    for line in ptxt:
        if line[1:len(str(pokemon_no))+1] == str(pokemon_no):
            
            plist = line[:]
            
    plist = plist.replace(']','').split(',')
    
    similars = [int(i) for i in plist[1:-1]] 
    #randomly choose three and convert to full names        
    wrong_no =  random.sample(similars,3)
    
    wrong_names = []
    for n2 in wrong_no[:]:
        if n2 < 10:
            no2 = '00' + str(n2)
        elif n2 < 100:
            no2 = '0' + str(n2)
        else:
            no2 =  str(n2)
        
        
        for j in os.listdir(path):
            if os.path.isfile(os.path.join(path,j)) and no2 in j:
                wname = j.replace('.png','')
                wrong_names.append(wname)
        
    #direct to the folder saving raw and shadow images
    path_s = path + 'Shadow(256x256)/'
    path_r = path + 'Raw(256x256)/'
    
    img_r = cv.imread((path_r+name+'_raw.png'))
    img_s= cv.imread((path_s+name+'_s.png'))
    
    #start rotation
    num_rows, num_cols = img_r.shape[:2]
    
    translation_matrix = np.float32([ [1,0,int(0.5*num_cols)], [0,1,int(0.5*num_rows)] ])
    
    rotation_matrix = cv.getRotationMatrix2D((num_cols, num_rows), angle, 1)
    
    img_r_translation = cv.warpAffine(img_r, translation_matrix, (2*2*num_cols, 2*num_rows),borderValue=(255,255,255))
    img_s_translation = cv.warpAffine(img_s, translation_matrix, (2*2*num_cols, 2*num_rows),borderValue=(255,255,255))
    img_r_rotation = cv.warpAffine(img_r_translation, rotation_matrix, (2*num_cols, 2*num_rows),borderValue=(255,255,255))
    img_s_rotation = cv.warpAffine(img_s_translation, rotation_matrix, (2*num_cols, 2*num_rows),borderValue=(255,255,255))
    
    #cv.imshow('Rotation1', img_r_rotation)
    #cv.imshow('Rotation2', img_s_rotation)
    
    cv.waitKey()
    
    return correct_name, wrong_names, img_s_rotation, img_r_rotation

#for test
if __name__ == "__main__":
    path = "C:/Users/qimin/Desktop/pokemon_png/"
    no = 39
    angle = 180
    [correct_name, wrong_names, rotated_s, rotated_r] = rotate(path,no,angle)