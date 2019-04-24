# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:18:03 2019
This script reads all the raw pokemon PNG images and find the relative similarity 
of their shapes based on the method of Humoments & Euclidean distance and 
contour match
  
pokemon_list1 and pokemon_list2 are both lists of 809 lists of every 3 most similar 
pokemon name to one specific pokemon detected by the two different methods.

Output: the txt file where lists 809 pokemon no with their corresponding similar 
no detected by both methods 

@author: qimin
"""
import os
import math
import cv2 as cv
import numpy as np

#first get the Hu monments for all pokemons

Path = 'Your Path /Guess_Pokemon/Filled/'
hu_pokemon = []
imgs = []
for file in os.listdir(Path):
    if os.path.isfile((Path+file)) == True:
        print (file)
        img = cv.imread((Path+file),cv.IMREAD_GRAYSCALE)

        #Binarize the image using thresholding
        _,img = cv.threshold(img, 128, 255, cv.THRESH_BINARY)
        imgs.append(img)

        # Calculate Moments
        moments = cv.moments(img)
        
        # Calculate Hu Moments
        huMoments = cv.HuMoments(moments)
     
        # Log scale hu moments
        for i in range (0,7):
            huMoments[i] = -1*math.copysign(1,huMoments[i]) *math.log10(abs(huMoments[i]))
        
        huMoments = np.array(huMoments).tolist()
        hu_pokemon.append([ i [0] for i in huMoments])
        
#find the Euclidean distance between the Hu Moments of every pair of pokemon 
def Ed(Hu1,Hu2):
    ed12 = 0
    
    for i in range(0,2): #we can change the order of Humoments it includes
        ed12 = ed12 + (Hu2[i] - Hu1[i]) **2
    
    ed12 = ed12 ** 0.5
    return ed12


# choose the top 3 nearest distance for each pokemon
# record the No. of them into a list
# eg. for 001, the list will be [1,## ,## , ###]
pokemon_list1 = []
for no in range(len(hu_pokemon)):
    pokemon_list1.append ([])
    ed =[]
    for h in range(len(hu_pokemon)):
        ed.append(Ed(hu_pokemon[no],hu_pokemon[h]))
    for i in range(0,4):
        pokemon_list1[no].append (ed.index(sorted(ed)[i])+1)
    

#------------------------------------------------------------------------------       
#Find the most similar pokemon sets by using opencv built-in contour function
pokemon_list2 = []

for no2 in range(809):
   pokemon_list2.append ([])
   ed2 =[]
   for h2 in range(809):
       ed2.append(cv.matchShapes(imgs[no2],imgs[h2],cv.CONTOURS_MATCH_I3,0))
   for i in range(0,4):
       pokemon_list2[no2].append (ed2.index(sorted(ed2)[i])+1)

#comebine pokemon_list 1 & 2
pokemonlist = []
for dex in range(809):
    combin = pokemon_list1[dex][:] + pokemon_list2[dex][1:] 
    sorted(set(combin), key=combin.index) #because set() can change the order
    pokemonlist.append(combin) 
        
    

#save the total lists into txt file for further use
txt = open('your path /Guess_Pokemon/pokemonlist.txt','w')

for line in pokemonlist:
    txt.write(str(line)+'\r\n')

txt.close()