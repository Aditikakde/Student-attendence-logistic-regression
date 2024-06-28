

from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
#from pymsgbox import *


root=tk.Tk()

root.title("Student Attendance Using Web Cam")

#, relwidth=1, relheight=1)

w = tk.Label(root, text="Student Attendance Using Web Cam",width=40,background="skyblue",height=2,font=("Times new roman",19,"bold"))
w.place(x=0,y=15)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="skyblue")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login1.py"])


def Register():
    from subprocess import call
    call(["python","registration.py"])







bg = Image.open(r"h4.jpg")
bg.resize((7300,900))
print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=300,y=93)

wlcm=tk.Label(root,text="......Welcome to Student Attendance Using Web Cam ......",width=85,height=2,background="skyblue",foreground="black",font=("Times new roman",22,"bold"))
wlcm.place(x=0,y=700)




Disease2=tk.Button(root,text="Login",command=Login,width=9,height=2,bd=0,background="skyblue",foreground="black",font=("times new roman",14,"bold"))
Disease2.place(x=1300,y=18)


Disease3=tk.Button(root,text="Register",command=Register,width=9,height=2,bd=0,background="skyblue",foreground="black",font=("times new roman",14,"bold"))
Disease3.place(x=1400,y=18)



root.mainloop()
