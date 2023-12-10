from tkinter import *
import mysql.connector as ms
from tkinter import messagebox
from twilio.rest import Client
import random

mw=Tk()
mw.geometry("370x450+700+40")
mw.resizable(0,0)

code=random.randrange(1000,10000)
op = str(code)+ " is your varification code"

def otps():
    if mobilenumber.get()== "" or acountnumber.get()=="" or acountpin.get()=="":
        messagebox.showerror("Error","all field are requered")
    else:
        try:
            #op = str(code)+ " is your varification code"
            account_sid = 'ACbd6eb7fc035cd449d12aff30a598b793'
            auth_token = '56c010088581fb1b89b5066b39e53619'
            client = Client(account_sid, auth_token)
            message = client.messages.create(from_='+14172330647',body=op,to=str(mobilenumber.get()))
            print(message.sid)
        except:
            messagebox.showerror("Error","Please fill the correct detail")

def check():
    if  acountnumber.get()=="" or acountpin.get()=="" or mobilenumber.get()=="" or otp.get()=="" or npin.get()=="" or cpin.get()=="" :
        messagebox.showerror("Error,All field are requered")
    elif  npin.get()!= cpin.get():
        messagebox.showerror("Error,Password are mismatch")
    elif code!=otp.get():
        messagebox.showerror("Error","Please enter valid code")
    else:
        mydb=ms.connect(host="localhost", user="root", password="Rohit@6731#1", auth_plugin="mysql_native_password",database="ATM_customers")
        cur=mydb.cursor()   
        query1="use ATM_customers"
        cur.execute(query1)
        query2="select * from ATM_data  where accountno= %s  and pinno = %s and mobileno = %s"
        cur.execute(query2,(acountnumber.get(),acountpin.get(),mobilenumber.get()))
        row=cur.fetchall()
        #print(row)
        if row==None:
            messagebox.showinfo("Detail are mismatch") 
        else:
            query3="update ATM_data set pinno = %s where accountno = %s"
            #d=(acountnumber.get())
            cur.execute(query3,(cpin.get(),acountnumber.get()))
            mydb.commit()
            mydb.close()
            messagebox.showinfo("success","ATM is update now login with new pin")
            mw.destroy()
            import credit_debit  

label1=Label(mw,text="Update ATM PIN",font=("Microsoft YaHei UI Light",12,'bold')).place(x=140,y=30)

label1=Label(mw,text="account nuumber ").place(x=10,y=80)
acountnumber=IntVar()
acountnumbers=Entry(mw,width=25,textvariable=acountnumber)
acountnumbers.place(x=120,y=80)


label1=Label(mw,text="pinno").place(x=10,y=120)
acountpin=IntVar()
acountpins=Entry(mw,width=25,textvariable=acountpin)
acountpins.place(x=120,y=120)

label1=Label(mw,text="Mobile number ").place(x=10,y=160)
mobilenumber=StringVar()
acountnumbers=Entry(mw,width=25,textvariable=mobilenumber)
acountnumbers.place(x=120,y=160)

submit_button1=Button(mw,text="Generete OTP",width=12,command=otps) 
submit_button1.place(x=140,y=200)


label1=Label(mw,text="OTP").place(x=10,y=240)
otp=IntVar()
otpe=Entry(mw,width=25,textvariable=otp)
otpe.place(x=120,y=240)

label1=Label(mw,text="new pinno").place(x=10,y=280)
npin=IntVar()
npins=Entry(mw,width=25,textvariable=npin)
npins.place(x=120,y=280)

label1=Label(mw,text="canform pinno").place(x=10,y=320)
cpin=IntVar()
cpins=Entry(mw,width=25,textvariable=cpin)
cpins.place(x=120,y=320)

submit_button2=Button(mw,text="Submit",width=12,command=check) 
submit_button2.place(x=140,y=380)



mw.mainloop()