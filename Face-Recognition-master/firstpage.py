#import module from tkinter for UI
from tkinter import Tk, Label, Button

from _tkinter import *

import os

#creating instance of TK
root=Tk()

root.configure(background="#80D8FF")

#root.geometry("600x600")

def function1():
    
    os.system("python training.py")
    
def function2():
    
    os.system("python face_recognition.py")

def function3():

    os.system("python face_datasets.py")

def function4():

    os.system("python showdata.py")

#stting title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#creating a text label
Label(root, text="Smart Attendance",font=("helvatica",40),fg="white",bg="#00BFA5",height=2).grid(row=0,rowspan=2,columnspan=2,padx=5,pady=5)

#creating a button
Button(root,text="Train DATABASE",font=("times new roman",30),bg="#3F51B5",fg='white',command=function1).grid(row=3,columnspan=2,padx=5,pady=5)

#creating second button
Button(root,text="Take Attendance",font=("times new roman",30),bg="#3F51B5",fg='white',command=function2).grid(row=4,columnspan=2,padx=5,pady=5)

#creating third button
Button(root,text="New Entry",font=('times new roman',30),bg="#3F51B5",fg="white",command=function3).grid(row=5,columnspan=2,padx=5,pady=5)

#creating fourth button
Button(root,text="View Attendance",font=('times new roman',30),bg="#3F51B5",fg="white",command=function4).grid(row=6,columnspan=2,padx=5,pady=5)

root.mainloop()
