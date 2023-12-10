from tkinter import *
from tkinter import messagebox
import mysql.connector as ms
from twilio.rest import Client
import random

mw1=Tk()
mw1.geometry("450x550+700+40")
mw1.resizable(0,0)

code=random.randrange(1000,10000)
print(code)
op = str(code)+ " is your varification code"

accode=random.randrange(1000000000,10000000000)
print(accode)
ac =  "Genereated account  number is" + str(accode) 


def generate_ac():
    if acountnames.get()=="" or acountpins.get()==""   or Deposits.get()==""  or mobilenos.get()==""  or otps.get()=="":
        messagebox.showerror("Error","All field are requered")

    elif otp.get()==code:
        messagebox.showerror("Error","invalid OTP")
    elif len(str(acountpins.get()))==5:
        messagebox.showerror("Error","Select pin are 4 digit ")
    else:
        try:
            op = str(code)+ " is your varification code"
            account_sid = 'ACbd6eb7fc035cd449d12aff30a598b793'
            auth_token = '56c010088581fb1b89b5066b39e53619'
            client = Client(account_sid, auth_token)
            message = client.messages.create(from_='+14172330647',body=ac,to=str(mobilenos.get()))
            acountnumber.config(state= "normal")
            submit_button2.config(state= "normal")
            gen_ac.config(state= "disabled")
            messagebox.showinfo("Success", ac)
            #submit_button2['state']='enable'
        except:
            messagebox.showerror("Error","Please fill the correct detail")



def generate_otp():
    if mobilenos.get()=="" or acountnames.get()=="" or Deposits.get()=="":
        messagebox.showerror("Error","please enter the detail")
    elif len(str(acountpins.get()))==5:
        messagebox.showerror("Error","Select pin are 4 digit ")
        messagebox.showinfo("Success","Your acount number is ")
    
    else:
        try:
            op = str(code)+ " is your varification code"
            account_sid = 'ACbd6eb7fc035cd449d12aff30a598b793'
            auth_token = '56c010088581fb1b89b5066b39e53619'
            client = Client(account_sid, auth_token)
            message = client.messages.create(from_='+14172330647',body=op,to=str(mobilenos.get()))
            print(message.sid)
            otp.config(state= "normal")
            gen_ac.config(state= "normal")
            
            
        except:
            messagebox.showerror("Error","Please fill the correct detail")


def sub():
    if acountnames.get()=="" or acountpins.get()==""  or acountnumbers.get()==""  or Deposits.get()==""  or mobilenos.get()=="" or otps.get()=="":
        messagebox.showerror("Error","All field are requered")    
    elif otp.get()==code:
        messagebox.showerror("Error","invalid OTP")
    elif otp.get()==accode:
        messagebox.showerror("Error","Invalid  Account number")
    elif len(str(acountpins.get()))==5:
        messagebox.showerror("Error","Select pin are 4 digit ")
    else:
        try:
            mydb=ms.connect(host="localhost", user="root", password="Rohit@6731#1", auth_plugin="mysql_native_password")
            cur=mydb.cursor()
            print(0)
        except:
            messagebox.showerror("Error","database are not stable to connectvity")
            return 
        try:
            query0="create database ATM_customers"
            cur.execute(query0)
            #print("1s")
            query1="use ATM_customers"
            cur.execute(query1)
            query2="create table ATM_data(id int auto_increment primary key not null,name varchar(50), varchar(20),mobileno varchar(16),pinno int,deposit varchar(30))"
            cur.execute(query2)
            
        
            print("t")
        except:
            cur.execute('use ATM_customers')
            print("2s")
            

        query3="select * from ATM_data where accountno = %s"
        cur.execute(query3,[acountnumber.get()])
        row=cur.fetchone()
        if row!=None:
            messagebox.showerror("Error,account number already exist")
        else:
            query4="insert into ATM_data(name,accountno,pinno,deposit,mobileno) values(%s,%s,%s,%s,%s)"
            cur.execute(query4,(acountnames.get(),acountnumbers.get(),acountpins.get(),Deposits.get(),mobilenos.get()))
            
            tname= str(acountname.get()) + str(acountnumbers.get()) 
            query1="use ATM_customers"
            cur.execute(query1)

            tname= str(acountname.get()) + str(acountnumbers.get()) 
            query5="create table " + tname + " (id int auto_increment primary key not null,Deposit int default 0, Withdrawal int default 0, Balance int)"
            cur.execute(query5)
           
            query6="insert into" + tname + "(Deposit,Balance) values(%s,%s)"
            cur.execute(query6,(Deposits.get(),Deposits.get))


            mydb.commit()
            mydb.close()
            messagebox.showinfo("Info","Registration is succsessful")
            mw1.destroy()
            import credit_debit        

label1=Label(mw1,text="Create_account",font=("Microsoft YaHei UI Light",12,'bold')).place(x=130,y=20)

label0=Label(mw1,text="Account name").place(x=10,y=70)
acountnames=StringVar()
acountname=Entry(mw1,width=25,textvariable=acountnames)
acountname.place(x=120,y=70)

label1=Label(mw1,text="Account number").place(x=10,y=110)
acountnumbers=IntVar()
acountnumber=Entry(mw1,width=25,textvariable=acountnumbers)
acountnumber.place(x=120,y=110)
acountnumber.config(state= "disabled")

label2=Label(mw1,text="ATM pin number").place(x=10,y=150)
acountpins=IntVar()
acountpin=Entry(mw1,width=25,textvariable=acountpins) 
acountpin.place(x=120,y=150)

label3=Label(mw1,text="Debit amount").place(x=10,y=190)
Deposits=IntVar()
Deposit=Entry(mw1,width=25,textvariable=Deposits)
Deposit.place(x=120,y=190)

label3=Label(mw1,text="Mobile number").place(x=10,y=230)
mobilenos=StringVar()
mobileno=Entry(mw1,width=25,textvariable=mobilenos)
mobileno.place(x=120,y=230)

label3=Label(mw1,text="OTP").place(x=10,y=320)
otps=IntVar()
otp=Entry(mw1,width=25,textvariable=otps)
otp.place(x=120,y=320)
otp.config(state= "disabled")

submit_button1=Button(mw1,text="Gnerate OTP",width=12)
submit_button1.place(x=145,y=270)


gen_ac=Button(mw1,text="Gnerate a/c no ",width=12)
gen_ac.place(x=145,y=360)
gen_ac.config(state= "disabled")


submit_button2=Button(mw1,text="Submit",command=sub,width=16)
submit_button2.place(x=135,y=420)
submit_button2.config(state= "disabled")

mw1.mainloop()