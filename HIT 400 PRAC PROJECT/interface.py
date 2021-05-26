import cv2
import tkinter as tk
import tkinter.messagebox
from tkinter import *
import os

root = Tk()
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (width, height))
#root.geometry('500x570')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
root.title('Driver Cam')
frame.config(background='orange')
label = Label(frame, text="Driver Cam", bg='orange', font=('Arial 35 bold'))
label.pack(side=TOP)
filename = PhotoImage(file="C:/Users/pcRUX/Desktop/part 4.2/HIT 400/HIT 400 PRAC PROJECT/HIT-400-PROJ/HIT 400 PRAC PROJECT/rUX PROD.png")
background_label = Label(frame, image=filename)
background_label.pack(side=TOP)


def hel():
    help(cv2)

def Contri():
    tkinter.messagebox.showinfo("Contributor","\nPanashe Rukarwa\nH170219A\nComputer Science Student\nHIT400 FINAL YEAR PROJECT\n")
    
def anotherWin():
    tkinter.messagebox.showinfo("About","\nDriver Drowsiness Detection System using Deep Learning\nAll rights reserved\n")

def callAdminAuthentication():
    root.destroy()
    os.system('python login.py')

def callDrowsinessDetection():
    os.system('python detectface.py')


menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Manual Override", menu=subm1)
subm1.add_command(label="Admin Authentication", command=callAdminAuthentication)

subm1 = Menu(menu)
menu.add_cascade(label="Tools", menu=subm1)
subm1.add_command(label="OpenCV Docs", command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About", menu=subm2)
subm2.add_command(label="Driver Cam", command=anotherWin)
subm2.add_command(label="Contributors", command=Contri)

def exit():
    exit()

but1=Button(frame, padx=5, pady=5, width=39,bg='grey', fg='black', relief=GROOVE, command=callDrowsinessDetection, text='Launch Cam',font=('helvetica 16 bold'))
but1.place(x=400,y=84)   

root.mainloop()    