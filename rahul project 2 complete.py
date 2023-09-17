import tkinter as tk
import random
from tkinter import messagebox

name = 'rahul'
password = 1112

def otp():
            global otp1
            otp1=random.randint(1000,9999)
            messagebox.showinfo("OTP Generated", f"Your One Time Password (OTP) For Login is : {otp1} ")
            

root=tk.Tk()
l1=tk.Label(root,text=" Enter Username")
e1=tk.Entry(root)

l2=tk.Label(root,text=" Enter Password")
e2=tk.Entry(root)

def data():
    username=e1.get()
    user_password=int(e2.get())
      
    if user_password==password and username==name :
        registration()
    else:
        registration_msg()
    
def registration():
    messagebox.showinfo("Login Status","Login Successfully.....")

def registration_msg():

    messagebox.showinfo("Login_Status","Login Unsuccessful....")
    
    n1=tk.Label(root,text="Something Is Wrong Try With OTP ")
    
    b1=tk.Button(root,text="Send OTP",command=otp)
    
    n2=tk.Label(root,text="Enter OTP here :")
    
    e3=tk.Entry(root)
      
    def login():
        
        c=int(e3.get())
        if otp1==c:
                    messagebox.showinfo("RESULT","Your Username and Password are on the screen \n \nTry To Login With Correct Username and Password")
                    n3=tk.Label(root,text=f"Username is : {name}")
                    n4=tk.Label(root,text=f"Password is : {password}")
                    n3.grid(row=0,column=3)
                    n4.grid(row=1,column=3)

        else:
                messagebox.showinfo("OTP", "Entered OTP Is Wrong" )
                b1=tk.Button(root,text="Resend OTP",command=otp)
                b1.grid(row=5,column=1)
                   
        
    b2=tk.Button(root,text="submit",command=login)
    b2.grid(row=6,column=2)
    n1.grid(row=4,column=1)
    b1.grid(row=5,column=1)
    n2.grid(row=6,column=0)
    e3.grid(row=6,column=1)

b=tk.Button(root,text="Login",command=data)

l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
b.grid(row=2,column=1)

root.mainloop()