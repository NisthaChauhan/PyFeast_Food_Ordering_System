import tkinter
from tkinter import *
import mysql.connector as m
from tkinter import messagebox
import random as r
from tkinter.messagebox import showinfo      

def View_bill():
    global Order_id, samosa, pavbhaji, cholle, panipuri,order_val,total_val,orderid
    samosa=q1.get()
    pavbhaji=q2.get()
    cholle=q3.get()
    panipuri=q4.get()
    if samosa=="":
        samosa='0'
    if pavbhaji=="":
        pavbhaji='0'
    if cholle=="":
        cholle='0'
    if panipuri=="":
        panipuri='0'
#Random order id
    orderid=r.randint(100000,999999)
    Ord_id=Label(root,text="Order ID: ",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",20)).grid(row=9,column=1,pady=10)
    Order_id=Label(root,text=orderid,bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",20))
    Order_id.grid(row=9,column=2,pady=10)

#Billing
    order_val=(int(samosa)*89)+(int(pavbhaji)*169)+(int(cholle)*179)+(int(panipuri)*89)
    gst=0.18*order_val
    total_val=order_val+gst
    total_label=Label(root,text="Total bill\nIncluding taxes",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",20)).grid(row=10,column=1,pady=10)
    to_val=Label(root,text=order_val,bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16))
    to_val.grid(row=10,column=2,pady=10)
    print(order_val)

def Place_order():
    pas="nistha"
    db="urbanchowk"
    con=m.connect(host="localhost",user="root",passwd=pas,database=db,auth_plugin='mysql_native_password')
    cur=con.cursor()
    t="masalahouse"
    qry="insert into masalahouse values('"+str(orderid)+"','"+(cust_name.get())+"','"+(contact.get())+"','"+str(q1.get())+"','"+str(q2.get())+"','"+str(q3.get())+"','"+str(q4.get())+"','"+str(order_val)+"','"+str(total_val)+"')"
    #try:
    cur.execute(qry)
    con.commit()
    print("Successful")
    L10 = Label(root,text="Order placed",bg="black",fg="white",font=("Arial bold",22),width=10)
    L10.grid(row=11,column=1,padx=10,pady=10)
    """except:
        messagebox.showinfo("Error")"""
def masalahouse():
    global q1,q2,q3,q4,root,contact,cust_name
    root=tkinter.Tk()
    root.title("Masala House")
    root["bg"]="#ffff99" 

    l1=Label(root,text="Masala House's Menu",font=("Yu Gothic UI Bold",65),bg="#ffff99",fg="#d0320b").grid(row=0,column=2,pady=10)     #MAIN HEADING
    l2=Label(root,text="Dish",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",22)).grid(row=1,column=1,pady=10)    #Items
    l3=Label(root,text="Price(350g)",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",22)).grid(row=1,column=2,pady=10)    #price
    l4=Label(root,text="Quantity",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",22)).grid(row=1,column=3,pady=10)    #qunatity


    dish1=Label(root,text="Samosa",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16)).grid(row=2,column=1,pady=10)    #Samosa
    price1=Label(root,text="Rs. 89",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16)).grid(row=2,column=2,pady=10)    #Samosa
    q1=Entry(root,bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16),width=6)
    q1.grid(row=2,column=3,pady=10)    #Quantity


    dish2=Label(root,text="Pav Bhaji",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16)).grid(row=3,column=1,pady=10)    #Pav Bhaji
    price2=Label(root,text="Rs. 169",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16)).grid(row=3,column=2,pady=10)    #Pav Bhaji
    q2=Entry(root,bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16),width=6)
    q2.grid(row=3,column=3,pady=10)    #Quantity


    dish3=Label(root,text="Chole Bhature",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16)).grid(row=4,column=1,pady=10)    #Chole Bhature
    price3=Label(root,text="Rs. 179",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16)).grid(row=4,column=2,pady=10)    #Chole Bhature
    q3=Entry(root,bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16),width=6)
    q3.grid(row=4,column=3,pady=10)    #Quantity


    dish4=Label(root,text="Pani Puri",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16)).grid(row=5,column=1,pady=10)    #Pani Puri
    price4=Label(root,text="Rs. 89",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16)).grid(row=5,column=2,pady=10)    #Pani Puri
    q4=Entry(root,bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16),width=6)
    q4.grid(row=5,column=3,pady=10)    #Quantity
    

    c_name=Label(root,text="Customer Name",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16)).grid(row=6,column=1,pady=10)   
    cust_name=Entry(root,bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16))
    cust_name.grid(row=6,column=2,pady=10)    #Customer name
    c=Label(root,text="Contact number",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16)).grid(row=7,column=1,pady=10)    #rolls
    contact=Entry(root,bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16))
    contact.grid(row=7,column=2,pady=10)    #Contact number
    
    view_bill=Button(root,text="View Bill",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16),command=View_bill).grid(row=8,column=2,pady=10)    #View Bill
    Place=Button(root,text="Place order",bg="#ffff99",fg="#d0320b",font=("Arial bold",20),width=10,command=Place_order).grid(row=8,column=3,padx=10,pady=10)    
    ex=Button(root,text="Exit",bg="#ffff99",fg="#d0320b",font=("Yu Gothic UI Bold",16),command=root.destroy).grid(row=8,column=4,pady=10)   
    root.mainloop()
    print(samosa,pavbhaji,cholle,panipuri)
