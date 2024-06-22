#auth_plugin='mysql_native_password'


import time
from tkinter import *
from tkinter import messagebox
from salenpepe import *
from wokonfire import *
from masalhouse import *
from tkinter.messagebox import showinfo

from PIL import ImageTk


root=Tk()   
root.title("Urban Chowk Main Menu")

root.geometry("1200x676")
img1= PhotoImage(file="C:\\Nistha\\Ctag Python\\Urban Chowk\\mainbg.png", master= root) 
img_label1= Label(root,image=img1)
img_label1.place(x=0, y=0)




l1=Label(root,text="URBAN CHOWK",font=("impact",85)).pack(pady=40)
b1=Button(root,text="Sale and Pepe",bg="White",fg="Green",font=("Arial Bold",30),command=salenpepe).pack(pady=20)
b2=Button(root,text="Wok on Fire",bg="Black",fg="Yellow",font=("Arial Bold",30),command=wokonfire).pack(pady=20)
b3=Button(root,text="Masala House",bg="Yellow",fg="Red",font=("Arial Bold",30),command=masalahouse).pack(pady=20)

#e1=Entry(root).pack()      #for input
root.mainloop()
