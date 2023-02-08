from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import sqlite3
con=sqlite3.Connection('hrdb')
rootp=Tk()
rootp.title("Flight Booking Simulation")
rootp.geometry('650x440')
rootp.config(bg='SkyBlue')
Label(rootp,text="AIR INDIGO",font="Times 50",bg="LightCyan",fg="MidnightBlue").pack()
Label(rootp,text="Welcome to AIR INDIGO website, the one place to\nBook, Cancel and Plan your Air Journey...",font="Times 20",fg="Black",bg="LightCyan").pack()
def fun8():
    rootp.destroy()
    root2=Tk()
    root2.geometry('600x175')
    root2.config(bg='SkyBlue')
    root2.title("Welcome,Customer To our Cancellation System")
    Label(root2,text="Enter last 4 digit of your Citizenship Number",font="Times 15").grid(row=0,column=0)
    e1=Entry(root2,width=38)
    e1.grid(row=0,column=1)
    Label(root2,text="Choose your class",font="Times 15").grid(row=1,column=0)
    w2=ttk.Combobox(root2,height=30,width=35,values=["Economic","BusinessClass"])
    w2.grid(row=1,column=1)
    Label(root2,text="Select Boarding",font="Times 15").grid(row=2,column=0)
    w3=ttk.Combobox(root2,height=5,width=35,values=["PATNA","MUMBAI","BANGALORE","LUCKNOW"])
    w3.grid(row=2,column=1)
    
    def fun2():
        d=e1.get()
        b=w2.get()
        c=w3.get()
        cur=con.cursor()
        x=str(d)
        y=str(c)
        con.commit()
        if d=='' or b=='' or c=='':
             messagebox.showerror("Oops","You can't Enter the leave any field empty")
        else:     
             if b=="Economic" or b=="BusinessClass":
                cur.execute("delete from economic2 where adno=(?) and boarding=(?)",(d,b,))
                cur.execute("select * from economic2")
                messagebox.showinfo("Your reservation is Cancelled",cur.fetchall())
             else:
                    cur.execute("delete from common2 where adno=x and boarding=y")
                    cur.execute("select * from common2")       
    Bc=Button(root2,text="Cancel Reservation",command=fun2,font="Times 13",bg="OrangeRed").grid(row=4,column=1)
    Back=Button(root2,text='Quit Page',command=root2.destroy,font="Times 13",bg="MediumAquaMarine",fg="Black").grid(row=5,column=1)
    root2.mainloop()
    
def fun9():
    rootp.destroy()
    root4=Tk()
    root4.geometry('500x175')
    root4.config(bg='SkyBlue')
    root4.title("Welcome,Search flights")
    Label(root4,text="Enter Boarding",font="Times 15").grid(row=0,column=0)
    w1=ttk.Combobox(root4,height=5,width=35,values=["PATNA","MUMBAI","BANGALORE","LUCKNOW"])
    w1.grid(row=0,column=1)
    Label(root4,text="Select destination",font="Times 15").grid(row=1,column=0)
    w2=ttk.Combobox(root4,height=5,width=35,values=["PATNA","MUMBAI","BANGALORE","LUCKNOW"])
    w2.grid(row=1,column=1)
    Label(root4,text="Choose day of Travel",font="Times 15").grid(row=2,column=0)
    w3=ttk.Combobox(root4,text="choose day",height=5,width=35,values=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])
    w3.grid(row=2,column=1)
    def fun10():
        a=w1.get()
        b=w2.get()
        c=w3.get()
        cur=con.cursor()
        if a=='' or b=='' or c=='':
            messagebox.showerror("Error","Cant leave any field empty")
           
                
        else:
             if a!=b:

                 cur.execute("insert into eco values('PATNA','MUMBAI','Sunday',1.00,'Economic',2500\n)")
                 cur.execute("insert into eco values('PATNA','BANGALORE','Monday',1.00,'BusinessClass',4000\n)")
                 cur.execute("insert into eco values('PATNA','LUCKNOW','Tuesday',1.00,'Economic',5500\n)")
                 cur.execute("insert into eco values('MUMBAI','LUCKNOW','Wednesday',1.00,'Economic',3500\n)")
                 cur.execute("insert into eco values('MUMBAI','BANGALORE','Thursday',1.00,'BusinessClass',4500\n)")
                 cur.execute("insert into eco values('MUMBAI','PATNA','Friday',1.00,'Economic',3500\n)")
                 cur.execute("insert into eco values('BANGALORE','LUCKNOW','Saturday',1.00,'BusinessClass',4500\n)")
                 cur.execute("select * from eco where boarding=? and destination=? and day=?",(a,b,c,))
                 con.commit()
                 e=cur.fetchall()
                 messagebox.showinfo("Flights availble -->",e)
             else:
                 messagebox.showerror("Oops","boarding and destination can't be same")
        
    Bs=Button(root4,text="Search",command=fun10,font="Times 13",bg="Gold",width=15).grid(row=3,column=1)
    Back=Button(root4,text='Quit Page',command=root4.destroy,font="Times 13",bg="MediumAquaMarine",fg="Black").grid(row=4,column=1)
    root4.mainloop()
def fun5():
    rootp.destroy()
    root=Tk()
    root.geometry('500x300')
    root.config(bg='SkyBlue')
    root.title('Flight search And booking')
    Label(root,text="Enter Boarding",font="Times 15").grid(row=1,column=0)

    w=ttk.Combobox(root,height=5,width=35,values=["PATNA","MUMBAI","BANGALORE","LUCKNOW"])
    w.grid(row=1,column=1)
    Label(root,text='Enter Destination',font="Times 15").grid(row=2,column=0)
    w1=ttk.Combobox(root,height=5,width=35,values=["PATNA","MUMBAI","BANGALORE","LUCKNOW"])
    w1.grid(row=2,column=1)

    Label(root,text='Enter last 4 digit of your\nCitizenship Number',font="Times 15").grid(row=3,column=0)
    e=Entry(root,width=38)
    e.grid(row=3,column=1)
    w2=ttk.Combobox(root,text='BusinessClass',height=5,width=35,values=["Economic","BusinessClass"])
    w2.grid(row=4,column=1)
    Label(root,text='Choose Class',font="Times 15").grid(row=4,column=0)
    Label(root,text="Choose day of travel",font="Times 15").grid(row=5,column=0)
    w3=ttk.Combobox(root,text="choose day",height=5,width=35,values=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])
    w3.grid(row=5,column=1)
    Label(root,text="Choose time of your flight",font="Times 15").grid(row=6,column=0)
    w4=ttk.Combobox(root,height=5,width=35,values=["1:00 AM","7:00 AM","1:00 PM","4:00 PM","6:00 PM","8:00 PM","10:00 PM"])
    w4.grid(row=6,column=1)
    def fun():
        a=w.get()
        b=w1.get()
        c=e.get()
        d=w2.get()
        f=w3.get()
        g=w4.get()
        x=(a,b,c,f,g)
        cur=con.cursor()
        
        if a=='' or b=='' or c=='' or d=='' or f=='' or g=='':
            messagebox.showerror("OOPS","you can't leave any field empty")
        else :
            if d=='Economic':
                
                if a!=b:

                    cur.execute("insert into economic2 values(?,?,?,?,?)",x)
                    messagebox.showinfo("Congrats","Your seat has been reserved.\nYour boarding pass has been mailed to your e-mail id")
                    con.commit()
                    cur.execute("select * from economic2 where adno=(?)",(c,))
                    messagebox.showinfo("records",cur.fetchall())
                else:
                    messagebox.showerror("Error","you can't choose same city")
            if d=='BusinessClass':

                if a!=b:
                    cur.execute("insert into common2 values(?,?,?,?,?)",x)
                    messagebox.showinfo("Congrats","Your seat has been reserved.\nYour boarding pass has been mailed to your e-mail id")
                    con.commit()
                    cur.execute("select * from common2 where adno=(?)",(c,))
                    messagebox.showinfo("records",cur.fetchall())
                else :
                    messagebox.showerror("Error","you can't choose same city")
    Bi=Button(root,text="Insert",command=fun,font="Times 13",bg="DarkSlateGray",fg="white",width=15).grid(row=7,column=1)
    Back=Button(root,text='Quit Page',command=root.destroy,font="Times 13",bg="MediumAquaMarine",fg="Black").grid(row=8,column=1)

    root.mainloop()
    
B1=Button(rootp,text="Book Flight",command=fun5,height=3,width=20,font="Times 13").pack()
B2=Button(rootp,text="Cancle Booking",command=fun8,height=3,width=20,font="Times 13").pack()
B3=Button(rootp,text="Search Flights ",command=fun9,height=3,width=20,font="Times 13").pack()
Quit=Button(rootp,text='Quit Page',command=rootp.destroy,height=3,width=20,font="Times 13",fg="Red").pack()

rootp.mainloop()
    
