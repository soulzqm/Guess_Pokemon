# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 10:48:24 2019

@author: qimin
"""

from PIL import ImageTk, Image
import tkinter as tk
import random
from rotation import *
#Please make sure the path is the folder where you extract the Guess_Pokemon.zip to !
path = "C:/Users/qimin/Desktop/Guess_Pokemon/"

#design the GUI interface

# setup the main panel
m=tk.Tk() 
m.title('Guess Pokemon Ver 1.0.0 by soulzqm')
m.geometry("800x800") 
m.resizable(0, 0) #Don't allow resizing in the x or y direction

#Put the background for the starting page

canvas = tk.Canvas(m,width = 600,height = 600, bg = 'white')
bg1_org=Image.open('background.jpg')
bg1 = ImageTk.PhotoImage(bg1_org)

canvas.create_image(0,0,anchor=tk.NW,image = bg1)

canvas.pack(fill="both", expand=True ) 


#This fucntion check if you click the correct pokemon name or not
#If it is correct, return 'green', otherwise 'red'
def check(button,correct_name):
    
    if button.cget('text') == correct_name :
        color = "green"
    else:
        color= "red"
    
    return color 
    

#This function calls rotation() with randomlized pokemon no and rotation angle
#It returns the four multiple choice names and the shadow/colored image for 
#The correct pokemon
def generate_question(path = ''):
    no = random.randrange(1, 810)  #
    angle = random.randrange(1, 360)
    [correct_name, wrong_names, rotated_s, rotated_r] = rotate(path,no,angle)
    
    return correct_name, wrong_names, rotated_s, rotated_r

#To get info for all weiges in the current window
def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list



def NEXT (button,correct_name):
    
    #Put the coloered image as the answer
    Q.create_image( 400, 400, image = rotated_r)
    Q.image = rotated_r
    
    #check if the chosen button is the answer, if yes, then it becomes green
    #otherwise, it becomes red and shows the right button as green
    color = check(button,correct_name)

    if color == 'green':
        for i in [button1,button2,button3,button4]:
            if i == button:
                i.config(state='disabled', disabledforeground='green')
            else:    
                i.config(state='disabled')
    else:
        for i in [button1,button2,button3,button4]:
            if i == button:
                i.config(state='disabled', disabledforeground='red')
            elif i.cget('text') == correct_name:
                i.config(state='disabled', disabledforeground='green')
            else:    
                i.config(state='disabled')
        
        
   
    Next = tk.Button(
            frame, bd=5, height=2, width=15, 
            font=11,text="Next one", fg="black",
            command = START
            )
    Next.pack(side = tk.BOTTOM, expand=True)


def START():
    global frame, button1, button2 ,button3, button4, Q,rotated_r
    widget_list = all_children(m)
    for item in widget_list:
        item.pack_forget()
    
    frame = tk.Frame(m, height = 800,width = 800, bg ='white')
    frame.pack( fill="both", expand=True)
    
    [correct_name, wrong_names, rotated_s, rotated_r] = generate_question(path)
   
    #Here,we need to convert images from openCV format to PIL forma
    rotated_s = Image.fromarray(rotated_s)
    rotated_s = ImageTk.PhotoImage(rotated_s)
    
    rotated_r = cv.cvtColor(rotated_r, cv.COLOR_BGR2RGB)
    rotated_r = Image.fromarray(rotated_r) 
    rotated_r = ImageTk.PhotoImage(rotated_r)
    
    names = random.sample([correct_name] + wrong_names,4)
   
    #Put the shadow image as the question
    Q = tk.Canvas(frame, width = 600, height = 600, bg = 'white') 
    Q.create_image(400,400, anchor = tk.CENTER, image = rotated_s)
    Q.image = rotated_s
    Q.pack( side =tk.TOP,fill ='both',expand=False)
   
    #Generate the four choices for pokemon's name
    
    button1 = tk.Button(
            frame, bd=5, height=2, width=15, 
            font=11,text= names[0], fg="black",
             state = 'normal'
            )
    
    button1.pack( side = tk.LEFT, expand=False)
    
    button2 = tk.Button(
            frame, bd=5, height=2, width=15, 
            font=11,text=names[1], fg="black",
             state = 'normal'
            )
    button2.pack( side = tk.LEFT, expand=False)
    
    button3 = tk.Button(
            frame, bd=5, height=2, width=15, 
            font=11,text=names[2], fg="black",
             state = 'normal'
            )
    button3.pack( side = tk.LEFT, expand=False)
    
    button4 = tk.Button(
            frame, bd=5, height=2, width=15, 
            font=11,text=names[3], fg="black",
            state = 'normal'
            )
    button4.pack(side = tk.LEFT, expand=False)
    
    button1.config(command=lambda:NEXT(button1,correct_name))
    button2.config(command=lambda:NEXT(button2,correct_name))
    button3.config(command=lambda:NEXT(button3,correct_name))
    button4.config(command=lambda:NEXT(button4,correct_name))


start = tk.Button(
        m, text='START',
        bd=5, height=5, width=15, 
        font=11,command=START
                  )
start.place(x=0, y=0, relwidth=1, relheight=1)
start.pack()



m.mainloop()