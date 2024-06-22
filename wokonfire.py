import tkinter
from tkinter import *
import mysql.connector as m
from tkinter import messagebox
import random as r
from tkinter.messagebox import showinfo  

def View_bill():
    global Total,Order_id,rice,noodle,manchurian,rolls,tot,total_val,orderid,order_val
    rice=q1.get()
    noodle=q2.get()
    manchurian=q3.get()
    rolls=q4.get()
    if rice=="":
        Rice=0
    if noodle=="":
        Noodle=0
    if manchurian=="":
        manchurian=0
    if rolls=="":
        rolls=0

#Random order id
    orderid=r.randint(100000,999999)
    Ord_id=Label(root,text="Order ID: ",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",20))
    Ord_id.grid(row=9,column=1,pady=10)
    Order_id=Label(root,text=orderid,bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",20))
    Order_id.grid(row=9,column=2,pady=10)

#Billing
    order_val=(int(rice)*139)+(int(noodle)*149)+(int(manchurian)*179)+(int(rolls)*139)
    gst=0.18*order_val
    Total=order_val+gst
    tot=Label(root,text="Total bill\nIncluding taxes",bg="#191919",fg="#F20D40",font=("Lucida Console",20))
    tot.grid(row=10,column=1,pady=10)
    total_val=Label(root,text=Total,bg="#191919",fg="#F20D40",font=("Lucida Console",16))
    total_val.grid(row=10,column=2,pady=10)

def Place_order():
    pas = "nistha"
    con = m.connect(host="localhost", user="root", passwd=pas, database="urbanchowk",auth_plugin='mysql_native_password')
    cur = con.cursor()
    qry="insert into masalahouse values('"+str(orderid)+"','"+(cust_name.get())+"','"+(contact.get())+"','"+str(q1.get())+"','"+str(q2.get())+"','"+str(q3.get())+"','"+str(q4.get())+"','"+str(order_val)+"','"+str(total_val)+"')"

    #try:
    cur.execute(qry)
    con.commit()
    L10 = Label(root, text="Order placed", bg="black", fg="white", font=("Arial bold", 22), width=10).grid(
        row=11,column=1,padx=10,pady=10)
    '''
        except Exception as e:
        messagebox.showinfo("Error",str(e))
    '''
    cur.close()
    con.close()
    
def wokonfire():
    global q1,q2,q3,q4,root,cust_name,contact
    root=tkinter.Tk()
    root.title("Wok On Fire")
    root["bg"]="#191919" 

    l1=Label(root,text="Wok On Fire's Menu",font=("Yu Gothic UI Bold",65),bg="#191919",fg="#F20D40").grid(row=0,column=2,pady=10)     #MAIN HEADING
    l2=Label(root,text="Dish",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",22)).grid(row=1,column=1,pady=10)    #Items
    l3=Label(root,text="Price(350g)",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",22)).grid(row=1,column=2,pady=10)    #price
    l4=Label(root,text="Quantity",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",22)).grid(row=1,column=3,pady=10)    #qunatity


    dish1=Label(root,text="Fried Rice",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16)).grid(row=2,column=1,pady=10)    #Fried Rice
    price1=Label(root,text="Rs. 139",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16)).grid(row=2,column=2,pady=10)    #Fried Rice
    q1=Entry(root,bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16),width=6)
    q1.grid(row=2,column=3,pady=10)    #Quantity


    dish2=Label(root,text="Hakka Noodles",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16)).grid(row=3,column=1,pady=10)    #Hakka Noodle
    price2=Label(root,text="Rs. 149",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16)).grid(row=3,column=2,pady=10)    #Hakka Noodles
    q2=Entry(root,bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16),width=6)
    q2.grid(row=3,column=3,pady=10)    #Quantity


    dish3=Label(root,text="Machurian",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16)).grid(row=4,column=1,pady=10)    #manchurian
    price3=Label(root,text="Rs. 179",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16)).grid(row=4,column=2,pady=10)    #manchurian
    q3=Entry(root,bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16),width=6)
    q3.grid(row=4,column=3,pady=10)    #Quantity


    dish4=Label(root,text="Spring Rolls",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16)).grid(row=5,column=1,pady=10)    #Spring Rolls
    price4=Label(root,text="Rs. 139",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16)).grid(row=5,column=2,pady=10)    #Spring Rolls
    q4=Entry(root,bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16),width=6)
    q4.grid(row=5,column=3,pady=10)    #Quantity
    

    c_name=Label(root,text="Customer Name",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16)).grid(row=6,column=1,pady=10)   
    cust_name=Entry(root,bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16))
    cust_name.grid(row=6,column=2,pady=10)    #Customer name
    c=Label(root,text="Contact number",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16)).grid(row=7,column=1,pady=10)    #rolls
    contact=Entry(root,bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16))
    contact.grid(row=7,column=2,pady=10)    #Contact number
    
    view_bill=Button(root,text="View Bill",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16),command=View_bill)
    view_bill.grid(row=8,column=2,pady=10)    #View Bill
    Place=Button(root,text="Place order",bg="#191919",fg="#F20D40",font=("Arial bold",20),width=10,command=Place_order).grid(row=8,column=3,padx=10,pady=10)    
    ex=Button(root,text="Exit",bg="#191919",fg="#F20D40",font=("Yu Gothic UI Bold",16),command=root.destroy).grid(row=8,column=4,pady=10)   

    root.mainloop()

