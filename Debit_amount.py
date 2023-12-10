from tkinter import *
import mysql.connector as ms
from tkinter import messagebox
from twilio.rest import Client
import random

code=random.randrange(1000,10000)
#op = str(debit.get()) + " is creadit" + "available" + str(tam)


mw=Tk()
mw.geometry("320x280+1000+40")
mw.resizable(True,True)

def sms():
    mw.destroy()
    import Gmail



def sub2():
    if acountname.get()=="" or acountnumber.get()=="" or acountpin.get()=="" or debit.get()=="":
        messagebox.showerror("Error,All field are requered")
    else:
        mydb=ms.connect(host="localhost", user="root", password="Rohit@6731#1", auth_plugin="mysql_native_password",database="ATM_customers")
        cur=mydb.cursor()   
        query1="use ATM_customers"
        cur.execute(query1)
        query2="select * from ATM_data where name = %s and accountno = %s and pinno= %s "
        cur.execute(query2,(acountname.get(),acountnumber.get(),acountpin.get()))
        row=cur.fetchone()
        
        if row==None:
            messagebox.showinfo("Detail are incorrect")
        else:
            if int(row[5])>=int(debit.get()):
                tam=int(row[5])-int(debit.get())
                query3="update ATM_data set deposit = %s where accountno = %s"
                d=(tam,acountnumber.get())
                cur.execute(query3,d)
                
                tname = str(acountname.get()) + str(acountnumber.get())
                query1="use ATM_customers"
                cur.execute(query1)
                query4="insert into " + tname + "(Withdrawal,Balance) values(%s,%s)"
                cur.execute(query4,[debit.get(),tam])

                mydb.commit()
                mydb.close()
                data=('Total amount is'),tam
                messagebox.showinfo("Success","Amout is Debit")
                messagebox.showinfo("Success",data)

                #add msg start

                try:
                    op = str(debit.get()) + " is debit for Rs " + "Avl bal " + str(tam)
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


            else:
                messagebox.showerror("Error,Amount is insufficient")
    

label1=Label(mw,text="Debit_amount",font=("Microsoft YaHei UI Light",10,'bold')).place(x=130,y=10)


label1=Label(mw,text="Account name").place(x=10,y=40)
acountname=StringVar()
acountnames=Entry(mw,width=25,textvariable=acountname)
acountnames.place(x=120,y=40)

label1=Label(mw,text="acoount number ").place(x=10,y=80)
acountnumber=IntVar()
acountnumbers=Entry(mw,width=25,textvariable=acountnumber)
acountnumbers.place(x=120,y=80)

label1=Label(mw,text="pin number").place(x=10,y=120)
acountpin=IntVar()
acountpins=Entry(mw,width=25,textvariable=acountpin)
acountpins.place(x=120,y=120)

label1=Label(mw,text="Debit amount").place(x=10,y=160)
debit=IntVar()
debits=Entry(mw,width=25,textvariable=debit)
debits.place(x=120,y=160)

submit_button1=Button(mw,text="Submit",width=12,command=sub2) 
submit_button1.place(x=140,y=220)

submit_button2=Button(mw,text="Want to gmail",width=12,font=("Open Sans",8,'bold'),fg="blue",cursor="hand2",bd=0,command=sms) 
submit_button2.place(x=10,y=230)
line2Frame=Frame(mw,width=90,height=1,bg="blue")
line2Frame.place(x=10,y=247)




mw.mainloop()