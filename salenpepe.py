import tkinter
from tkinter import *
from tkinter import messagebox
import random as r
import mysql.connector as m
from tkinter.messagebox import showinfo

def View_bill():
    global Order_id,pizza1,pizza2,lasagna,tiramisu,orderid,order_val,total_val
    pizza1=q1.get()
    pizza2=q2.get()
    lasagna=q3.get()
    tiramisu=q4.get()
    if pizza1=="":
        pizza1=0
    if pizza2=="":
        pizza2=0
    if lasagna=="":
        lasagna=0
    if tiramisu=="":
        tiramisu=0
#Random order id
    orderid=r.randint(100000,999999)
    Ord_id=Label(root,text="Order ID: ",bg="#013220",fg="#DEE1AC",font=("Lucida Console",20)).grid(row=9,column=1,pady=10)
    Order_id=Label(root,text=orderid,bg="#013220",fg="#DEE1AC",font=("Lucida Console",20)).grid(row=9,column=2,pady=10)

#Billing
    order_val=(int(pizza1)*179)+(int(pizza2)*169)+(int(lasagna)*229)+(int(tiramisu)*209)
    gst=0.18*order_val
    total_val=order_val+gst
    tot=Label(root,text="Total bill\nIncluding taxes",bg="#013220",fg="#DEE1AC",font=("Lucida Console",20))
    tot.grid(row=10,column=1,pady=10)
    total_val=Label(root,text=order_val,bg="#013220",fg="#DEE1AC",font=("Lucida Console",16))
    total_val.grid(row=10,column=2,pady=10)

def Place_order():
    pas="nistha"
    db="urbanchowk"
    con=m.connect(host="localhost",user="root",passwd=pas,database=db,auth_plugin='mysql_native_password')
    cur=con.cursor()
    t='salenpepe'
    qry="insert into masalahouse values('"+str(orderid)+"','"+(cust_name.get())+"','"+(contact.get())+"','"+str(q1.get())+"','"+str(q2.get())+"','"+str(q3.get())+"','"+str(q4.get())+"','"+str(order_val)+"','"+str(total_val)+"')"

    #try:
    cur.execute(qry)
    con.commit()
    L10 = Label(root,text="Order placed",bg="#013220",fg="#DEE1AC",font=("Lucida Console",22),width=10)
    L10.grid(row=11,column=1,padx=10,pady=10)
    """except:
        messagebox.showinfo("Error")"""

def salenpepe():
    global q1,q2,q3,q4,root,cust_name,contact
    root=tkinter.Tk()
    #root.geometry("900x900")    
    root.title("Sale and Pepe")
    root["bg"]="#013220" 

    l1=Label(root,text="Sale and Pepe's Menu",font=("Lucida Console",65),bg="#013220",fg="#DEE1AC").grid(row=0,column=2,pady=10)     #MAIN HEADING
    l2=Label(root,text="Dish",bg="#013220",fg="#DEE1AC",font=("Lucida Console",22)).grid(row=1,column=1,pady=10)    #Items
    l3=Label(root,text="Price(350g)",bg="#013220",fg="#DEE1AC",font=("Lucida Console",22)).grid(row=1,column=2,pady=10)    #price
    l4=Label(root,text="Quantity",bg="#013220",fg="#DEE1AC",font=("Lucida Console",22)).grid(row=1,column=3,pady=10)    #quantity

    dish1=Label(root,text="Baby Corn and Cheese Pizza",bg="#013220",fg="#DEE1AC",font=("Lucida Console",16)).grid(row=2,column=1,pady=10)    #Pizza 1
    price1=Label(root,text="Rs. 179",bg="#013220",fg="#DEE1AC",font=("Lucida Console",16)).grid(row=2,column=2,pady=10)    #Pizza 1
    q1=Entry(root,bg="#013220",fg="#DEE1AC",font=("Lucida Console",16),width=6)
    q1.grid(row=2,column=3,pady=10)    #Quantity


    dish2=Label(root,text="Margerita Pizza",bg="#013220",fg="#DEE1AC",font=("Lucida Console",16)).grid(row=3,column=1,pady=10)    #Pizza 2
    price2=Label(root,text="Rs. 169",bg="#013220",fg="#DEE1AC",font=("Lucida Console",16)).grid(row=3,column=2,pady=10)    #Pizza 1
    q2=Entry(root,bg="#013220",fg="#DEE1AC",font=("Lucida Console",16),width=6)
    q2.grid(row=3,column=3,pady=10)    #Quantity


    dish3=Label(root,text="Cheese and Spinach Lasagna",bg="#013220",fg="#DEE1AC",font=("Lucida Console",16)).grid(row=4,column=1,pady=10)    #Lasagna
    price3=Label(root,text="Rs. 229",bg="#013220",fg="#DEE1AC",font=("Lucida Console",16)).grid(row=4,column=2,pady=10)    #Pizza 1
    q3=Entry(root,bg="#013220",fg="#DEE1AC",font=("Lucida Console",16),width=6)
    q3.grid(row=4,column=3,pady=10)    #Quantity


    dish4=Label(root,text="Irish Coffee Tiramisu",bg="#013220",fg="#DEE1AC",font=("Lucida Console",16)).grid(row=5,column=1,pady=10)    #Tiramisu
    price4=Label(root,text="Rs. 209",bg="#013220",fg="#DEE1AC",font=("Lucida Console",16)).grid(row=5,column=2,pady=10)    #Pizza 1
    q4=Entry(root,bg="#013220",fg="#DEE1AC",font=("Lucida Console",16),width=6)
    q4.grid(row=5,column=3,pady=10)    #Quantity
    
    c_name=Label(root,text="Customer Name",bg="#013220",fg="#DEE1AC",font=("Lucida Console",16)).grid(row=6,column=1,pady=10)   
    cust_name=Entry(root,bg="#013220",fg="#DEE1AC",font=("Lucida Console",16))
    cust_name.grid(row=6,column=2,pady=10)    #Customer name
    c=Label(root,text="Contact number",bg="#013220",fg="#DEE1AC",font=("Lucida Console",16)).grid(row=7,column=1,pady=10)    #rolls
    contact=Entry(root,bg="#013220",fg="#DEE1AC",font=("Lucida Console",16))
    contact.grid(row=7,column=2,pady=10)    #Contact number
    
    view_bill=Button(root,text="View Bill",bg="#013220",fg="#DEE1AC",font=("Lucida Console",16),command=View_bill).grid(row=8,column=2,pady=10)    #View Bill
    Place=Button(root,text="Place order",bg="#013220",fg="#DEE1AC",font=("Lucida Console",16),width=10,command=Place_order).grid(row=8,column=3,padx=10,pady=10)    
    ex=Button(root,text="Exit",bg="#013220",fg="#DEE1AC",font=("Lucida Console",16),command=root.destroy).grid(row=8,column=4,pady=10)   
    root.mainloop()


