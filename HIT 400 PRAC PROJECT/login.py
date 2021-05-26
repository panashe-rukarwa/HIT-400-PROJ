from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter import messagebox

import pymysql
import cv2
import os

userID = "urEmailDomain"
home = "urHomeWindow"

def login():
    global userID 
    try:
        connection = pymysql.connect(host='localhost', user='root',db='login')
    except:
        print("You are not connected to server(localhost)!")
    else:
        print("Connected Successfully")
        print("Enter Email and Password")
        Email = User.get()
        Password = Pass.get()
        cur = connection.cursor()
        query = "SELECT email,password FROM users"
        cur.execute(query)
        
        def isValidEmail(user_email):
            if len(user_email) > 7:
                if re.match("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", user_email) !=None:
                    return True
                return False
            else:
                messagebox.showinfo('Information', 'This is not a valid email address')
                return False
        
        def validateAllFields():
            if v_pwd.get() == "":
                messagebox.showinfo('Information', 'Please enter password to proceed')
            elif v_emailAdd.get() != "":
                status = isValidEmail(v_emailAdd.get())
                if(status): 
                    messagebox.showinfo('Information', 'Admin authenticated! Welcome')
            else:
                messagebox.showinfo('Information', 'Admin authenticated! Welcome')
        
        for (email,pas) in cur:
            validateAllFields()
            if Email==email and Password==pas:
                login = True
                break
            else:
                login = False
        userID = (Email.split('@')[0])
        if login==True:
            print("Logged in successfully as", userID)
            newWindow()
        elif login==False:
            print("Email or password is wrong")
        cur.close()
        connection.close()
        
def newWindow():
    global userID,home
    #Close LOGIN window
    root.withdraw()
    #Open new window
    home = Toplevel(root)
    home.title('Manual Override Window')
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    #setting tkinter window size
    home.geometry("%dx%d" % (width, height))
    home.config(background='orange')
    frame = Frame(root, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH, expand=1)
    #frame.config(background='orange')
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
    
    def callHome():
        root.destroy()
        os.system('python interface.py')
    
    menu = Menu(root)
    root.config(menu=menu)
    
    subm1 = Menu(menu)
    menu.add_cascade(label="Home", menu=subm1)
    subm1.add_command(label="Back to Home", command=callHome)
    
    subm1 = Menu(menu)
    menu.add_cascade(label="Tools", menu=subm1)
    subm1.add_command(label="OpenCV Docs", command=hel)
    
    subm2 = Menu(menu)
    menu.add_cascade(label="About", menu=subm2)
    subm2.add_command(label="Driver Cam", command=anotherWin)
    subm2.add_command(label="Contributors", command=Contri)
    
    def exit():
        if tkinter.messagebox.askokcancel("Quit", "You want to quit now? *sniff*"):
            root.destroy()
    
    but1=Button(frame, padx=5, pady=5, width=39,bg='grey', fg='black', relief=GROOVE, command=exit, text='Disable Cam',font=('helvetica 16 bold'))
    but1.place(x=400,y=84)   
    
    something = Label(home, text="You are currently logged in\n {}", fg='blue', bg='orange')
    something.place(x=120, y=20)

    logout = Button(home, text='Logout', image=lo, fg='white', bg='red', activebackground='orange', width=100, height=20, command=logOut, compound=LEFT)
    logout.place(x=400, y=20)
    home.mainloop()
    
def logOut():
    global home
    home.withdraw()
    root.deiconify()
    print("Logged out successfully...")
    
root = Tk()
root.config(bg='orange')
root.title('Admin Authentication')
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (width, height))
root.resizable(0, 0)
image = PhotoImage(file='C:/Users/pcRUX/Desktop/part 4.2/HIT 400/HIT 400 PRAC PROJECT/HIT-400-PROJ/HIT 400 PRAC PROJECT/Output file.png')
root.wm_iconbitmap("C:/Users/pcRUX/Desktop/part 4.2/HIT 400/HIT 400 PRAC PROJECT/HIT-400-PROJ/HIT 400 PRAC PROJECT/lockoverlay.ico")

li = PhotoImage(file='C:/Users/pcRUX/Desktop/part 4.2/HIT 400/HIT 400 PRAC PROJECT/HIT-400-PROJ/HIT 400 PRAC PROJECT/checked.png')
lo = PhotoImage(file='C:/Users/pcRUX/Desktop/part 4.2/HIT 400/HIT 400 PRAC PROJECT/HIT-400-PROJ/HIT 400 PRAC PROJECT/checked.png')


def hel():
        help(cv2)
    
def Contri():
    tkinter.messagebox.showinfo("Contributor","\nPanashe Rukarwa\nH170219A\nComputer Science Student\nHIT400 FINAL YEAR PROJECT\n")
    
def anotherWin():
    tkinter.messagebox.showinfo("About","\nDriver Drowsiness Detection System using Deep Learning\nAll rights reserved\n")

def callHome():
    root.destroy()
    os.system('python interface.py')

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Home", menu=subm1)
subm1.add_command(label="Back to Home", command=callHome)

subm1 = Menu(menu)
menu.add_cascade(label="Tools", menu=subm1)
subm1.add_command(label="OpenCV Docs", command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About", menu=subm2)
subm2.add_command(label="Driver Cam", command=anotherWin)
subm2.add_command(label="Contributors", command=Contri)

def exit():
    if tkinter.messagebox.askokcancel("Quit", "You want to quit now? *sniff*"):
        root.destroy()

v_emailAdd = StringVar()
v_pwd = StringVar()

def clearAllFields():
    v_pwd.set("")
    v_emailAdd.set("")

bgLabel = Label(root, image=image)
bgLabel.pack(side=TOP)
nameTag = Label(root, text="Created by PANASHE RUKARWA", font=('arial', 10, 'bold'), fg='black').place(x=580, y=365)

site = Label(root, text='Admin Authentication', font=('arial', 15, 'bold', 'underline'), fg='black')
site.place(x=580, y=120)
#USERNAME
username = Label(root, text="Username: ", font=('arial', 10, 'bold'), fg='black').place(x=500, y=180)
User = Entry(root, textvariable=v_emailAdd, width=30, font=('calibri', 12), highlightbackground='orange', highlightthickness=1)
User.place(x=580, y=180)
#PASSWORD
password = Label(root, text="Password: ", font=('arial', 10, 'bold'), fg='black').place(x=500, y=230)
Pass = Entry(root, textvariable=v_pwd, width=30, font=('calibri', 12), highlightbackground='orange', show='*', highlightthickness=1)
Pass.place(x=580, y=230)

submit = Button(root, text='Authenticate', image=li, fg='white', bg='green', activebackground='blue', width=100, height=20, command=login, compound=LEFT)
submit.place(x=630, y=280)
btn_clear = Button(root, text='Clear', image=li, command=clearAllFields, bg="green", fg="white", activebackground='blue', width=100, height=20, compound=LEFT, font=("bold", 10)).place(x=630, y=330)

#close loop
root.mainloop()
            
              