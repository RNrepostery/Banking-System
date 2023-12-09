from tkinter import *
mw2=Tk()
mw2.geometry("280x300+780+40")
mw2.resizable(0,0)
def fun1():
    mw2.destroy()
    import Credit_amount
def fun2():
    mw2.destroy()
    import Debit_amount

def fun3():
    mw2.destroy()
    import Update_pin

def fun4():
    mw2.destroy()
    import Create_account
 

def fun5():
    mw2.destroy()
    import pay

def fun6():
    mw2.destroy()
    import Ac_del_ 
credit_button=Button(mw2,text="Credit amount",command=fun1,width=14 ).place(x=78,y=15)
debit_button=Button(mw2,text="Debit amount",command=fun2,width=14).place(x=78, y=60)
create_account=Button(mw2,text="update_pin",command=fun3,width=14).place(x=78, y=105)
#create_account=Button(mw2,text="Change ATM.pin",command=fun3,width=14).place(x=78
#, y=150)
create_account=Button(mw2,text="Create account",command=fun4,width=14).place(x=78, y=150)
send_bal=Button(mw2,text="Send balance",command=fun5,width=14).place(x=78, y=195)
Del_Ac=Button(mw2,text="Del_Account",command=fun6,width=14).place(x=78, y=235)


mw2.mainloop()

