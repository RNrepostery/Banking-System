from tkinter import *
import mysql.connector as ms
from tkinter import messagebox
from twilio.rest import Client
import random

mw=Tk()
mw.geometry("350x370+700+40")
mw.resizable(0,0)

def send():
    if  uacountname.get()=="" or uacountnumber.get()=="" :
        messagebox.showerror("Error,All field are requered")
    else:
        mydb=ms.connect(host="localhost", user="root", password="Rohit@6731#1", auth_plugin="mysql_native_password",database="ATM_customers")
        cur=mydb.cursor()   
        query1="use ATM_customers"
        cur.execute(query1)
        query2="select * from ATM_data where name = %s  and accountno = %s "
        cur.execute(query2,(sacountname.get(),sacountnumber.get()))
        row=cur.fetchone()
        print(row)
        
    if row==None:
        messagebox.showinfo("Error","Detail are incorrect")    
    else:
        if int(row[5])>=int(pay.get()):
                
           stam=int(row[5])-int(pay.get())
           query3="update ATM_data set deposit = %s where accountno = %s"
           d=(stam,sacountnumber.get())
           cur.execute(query3,d)
           print(1)

           tname = str(sacountname.get()) + str(sacountnumber.get())
           query1="use ATM_customers"
           cur.execute(query1)
           query4="insert into " + tname + "(Withdrawal,Balance) values(%s,%s)"
           cur.execute(query4,[pay.get(),stam])

           mydb.commit()
           mydb.close()
           data='Total amount is',stam
           messagebox.showinfo("Success","Amout is Transfer")
           messagebox.showinfo("Success",data)
           print(2)

                #add msg start+918756555978

           '''try:
               op = str(pay.get()) + " is debit for Rs " + "Avl bal " + str(stam)
               account_sid = 'ACbd6eb7fc035cd449d12aff30a598b793'
               auth_token = '56c010088581fb1b89b5066b39e53619'
               client = Client(account_sid, auth_token)
               message = client.messages.create(from_='+14172330647',body=op,to=str(sacountname.get()))
               print(message.sid)
           except:
               messagebox.showerror("Error","Please fill the correct detail")'''
        else:
            messagebox.showerror("Error,Amount is insufficient")


            

    
        if  uacountname.get()=="" or uacountnumber.get()=="" :
            messagebox.showerror("Error,All field are requered")
        else:
            mydb=ms.connect(host="localhost", user="root", password="Rohit@6731#1", auth_plugin="mysql_native_password",database="ATM_customers")
            cur=mydb.cursor()   
            query1="use ATM_customers"
            cur.execute(query1)
            query2="select * from ATM_data where name = %s  and accountno = %s "
            cur.execute(query2,(uacountname.get(),uacountnumber.get()))
            row=cur.fetchone()
            print(row)
        
        if row==None:
            messagebox.showinfo("Error","Detail are incorrect")
        else:
            
                
            utam=int(row[5])+int(pay.get())
            query3="update ATM_data set deposit = %s where accountno = %s"
            d=(utam,uacountnumber.get())
            cur.execute(query3,d)

            tname = str(uacountname.get()) + str(uacountnumber.get())
            query1="use ATM_customers"
            cur.execute(query1)
            query4="insert into " + tname + "(Withdrawal,Balance) values(%s,%s)"
            cur.execute(query4,[pay.get(),utam])

            mydb.commit()
            mydb.close()
            data='Total amount is',utam
            messagebox.showinfo("Success","Amout is credit")
            messagebox.showinfo("Success",data)

                #add msg start

            '''try:
                op = str(pay.get()) + " is debit for Rs " + "Avl bal " + str(utam)
                account_sid = 'ACbd6eb7fc035cd449d12aff30a598b793'
                auth_token = '56c010088581fb1b89b5066b39e53619'
                client = Client(account_sid, auth_token)
                message = client.messages.create(from_='+14172330647',body=op,to=str(row[3]))
                print(message.sid)
            except:
                messagebox.showerror("Error","Please fill the correct detail")'''


                # add msg end

        mw.destroy()
        import credit_debit


label3=Label(mw,text=" Sendr detail ",font=("Microsoft YaHei UI Light",10,'bold')).place(x=130,y=30)

label1=Label(mw,text="account name ").place(x=10,y=60)
sacountname=StringVar()
sacountnumbers=Entry(mw,width=25,textvariable=sacountname)
sacountnumbers.place(x=120,y=60)

label2=Label(mw,text="account number ").place(x=10,y=110)
sacountnumber=StringVar()
sacountnumbers=Entry(mw,width=25,textvariable=sacountnumber)
sacountnumbers.place(x=120,y=110)

label3=Label(mw,text=" Receiver detail ",font=("Microsoft YaHei UI Light",10,'bold')).place(x=130,y=145)

label4=Label(mw,text="account name ").place(x=10,y=180)
uacountname=StringVar()
uacountnumbers=Entry(mw,width=25,textvariable=uacountname)
uacountnumbers.place(x=120,y=180)

label5=Label(mw,text="account number ").place(x=10,y=230)
uacountnumber=StringVar()
uacountnumbers=Entry(mw,width=25,textvariable=uacountnumber)
uacountnumbers.place(x=120,y=230)

label5=Label(mw,text="Pay").place(x=10,y=280)
pay=IntVar()
pays=Entry(mw,width=25,textvariable=pay)
pays.place(x=120,y=280)


submit_button1=Button(mw,text="send",width=16,command=send ) 
submit_button1.place(x=138,y=320)


mw.mainloop()