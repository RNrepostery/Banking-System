from tkinter import *
from tkinter import messagebox
import mysql.connector as ms
from twilio.rest import Client
import random


mw=Tk()
mw.geometry("400x350+1000+40")
mw.resizable(0,0)

code=random.randrange(1000,10000)
#op = str(debit.get()) + " is creadit" + "available" + str(tam)


def message():
    mw.destroy()
    import Gmail


def sub1():
    if acountname.get()=="" or acountnumber.get()=="" or acountpin.get()=="" or creadit.get()=="":
        messagebox.showerror("Error,All field are requered")
    else:
        mydb=ms.connect(host="localhost", user="root", password="Rohit@6731#1", auth_plugin="mysql_native_password",database="ATM_customers")
        cur=mydb.cursor()   
        query1="use ATM_customers"
        cur.execute(query1)
        query2="select * from ATM_data where name = %s and accountno = %s and pinno= %s "
        cur.execute(query2,(acountname.get(),acountnumber.get(),acountpin.get()))
        row=cur.fetchone()
        print(row)
        
        
        if row==None:
            messagebox.showinfo("Detail are incorraREect")
        else:
            tam=int(row[5])+int(creadits.get())
            query3="update ATM_data set deposit = %s where accountno = %s"
            d=(tam,acountnumber.get())
            cur.execute(query3,d)
            data=("Total Amount is"), tam

            tname = str(acountname.get()) + str(acountnumber.get())
            query1="use ATM_customers"
            cur.execute(query1)
            query4="insert into " + tname + "(Deposit,Balance) values(%s,%s)"
            cur.execute(query4,[creadit.get(),tam])

            mydb.commit()
            mydb.close()
            messagebox.showinfo("Success"," Amout is deposit ")
            messagebox.showinfo("Success",data)
            try:
                op = str(creadit.get()) + " is credit for Rs " + "Avl bal " + str(tam)
                account_sid = 'ACbd6eb7fc035cd449d12aff30a598b793'
                auth_token = '56c010088581fb1b89b5066b39e53619'
                client = Client(account_sid, auth_token)
                message = client.messages.create(from_='+14172330647',body=op,to=str(row[3]))
                print(message.sid)
            except:
                messagebox.showerror("Error","Please fill the correct detail")


            mw.destroy()
            import credit_debit  
            try:
                op = str(creadit.get()) + " is credit for Rs " + "Avl bal " + str(tam)
                account_sid = 'ACbd6eb7fc035cd449d12aff30a598b793'
                auth_token = '56c010088581fb1b89b5066b39e53619'
                client = Client(account_sid, auth_token)
                message = client.messages.create(from_='+14172330647',body=op,to=str(row[3]))
                print(message.sid)
            except:
                messagebox.showerror("Error","Please fill the correct detail")

                # add msg end'''

                mw.destroy()
                import credit_debit
 

label1=Label(mw,text="Creadit_amount",font=("Microsoft YaHei UI Light",10,'bold')).place(x=135,y=10)

label1=Label(mw,text="Account name").place(x=10,y=40)
acountname=StringVar()
acountnames=Entry(mw,width=25,textvariable=acountname)
acountnames.place(x=120,y=40)

label1=Label(mw,text="Account number").place(x=10,y=80)
acountnumber=IntVar()
acountnumbers=Entry(mw,width=25,textvariable=acountnumber)
acountnumbers.place(x=120,y=80)

label1=Label(mw,text="ATM pin number",).place(x=10,y=120)
acountpin=IntVar()
acountpins=Entry(mw,width=25,textvariable=acountpin)
acountpins.place(x=120,y=120)

label1=Label(mw,text="Credit amount").place(x=10,y=160)
creadit=IntVar()
creadits=Entry(mw,width=25,textvariable=creadit)
creadits.place(x=120,y=160)

submit_button=Button(mw,text="Submit",width=12,command=sub1) 
submit_button.place(x=140,y=220)

submit_button1=Button(mw,text="Want to gmail",width=12,font=("Open Sans",8,'bold'),fg="blue",cursor="hand2",bd=0,command=message) 
submit_button1.place(x=10,y=230)
line2Frame=Frame(mw,width=90,height=1,bg="blue")
line2Frame.place(x=10,y=247)

mw.mainloop()