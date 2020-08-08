from tkinter import *
from tkinter import ttk
#import mysql.connector
from tkinter import messagebox
#import pyttsx3
#engine = pyttsx3.init()
#voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. of for male
#engine.setProperty('voice', voices[1].id)  
pi = ""
def main():
    root=Tk()
    #customer(root)
    login(root)

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Axis Bank customwr")
        self.root.geometry("1550x900")
        self.root.config(bg="black")
        self.frame=Frame(bg="black")
        self.frame.pack()

        
        self.Username=StringVar()
        self.Pin=StringVar()
        

        self.title=Label(self.frame,text="Axis Bank customer ",bd=1,relief=GROOVE,font=("Apex Mk2",20,"bold"),bg="BLACK",fg="red")
        self.title.grid(row=0,column=0,columnspan=2,pady=20)

        #=============================================Login Frames=================================================================
        self.login1=LabelFrame(self.frame,width=145,height=350,font=("times new roman",20,"bold"),relief=GROOVE,bg='BLACK')
        self.login1.grid(row=7,column=0)
        #self.login2=LabelFrame(self.frame,width=125,height=350,font=("times new roman",20,"bold"),relief=GROOVE,bg='black')
        #self.login2.grid(row=9,column=0)
        #=======================================================Login Frame Entry Field================================================
        self.title=Label(self.login1,text='Insert Your Card ',bd=1,relief=GROOVE,font=("Apex Mk2",35,"bold"),bg="black",fg="Red")
        self.title.grid(row=0,column=1,columnspan=2,pady=20)
        
        self.pin=Label(self.login1,text='Enter your Pin:',font=("times new roman",25,"bold"),bg="black",fg="white")
        self.pin.grid(row=2,column=1)

        self.txtpas=Entry(self.login1,font=("times new roman",25,"bold"),show="*",textvariable=self.Pin)
        self.txtpas.grid(row=2,column=2)
        
        #============================Log Frame Button============================================================================
        self.btlog=Button(self.login1,text='Enter',font=("times new roman",20,"bold"),width=5,bg="black",fg="white",command=self.customer)
        self.btlog.grid(row=4,column=1)#,pady=20,padx=8)

        self.exit=Button(self.login1,text='Cancel',font=("times new roman",20,"bold"),width=5,bg="black",fg="white",command=exit)
        self.exit.grid(row=4,column=2)#,padx=8,pady=20)
        
        #================================================Command Section========================================================

    def login_system(self):
        if self.Pin.get()=="" :
            messagebox.askyesno("LOGIN","please enter all the field")
            engine.say("please enter all the field")
            engine.runAndWait() 
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
            cur=con.cursor()
            cur.execute("select * from customer where pin=%s",[(self.Pin.get()),])
            global pi
            pi = self.Pin.get()
            print(pi)
            re=cur.fetchall()
            if re:
                for i in re:
                    self.login_window()
                    #con.commit()
            else:
                messagebox.showerror("LOGIN","Invaild Pin")
                engine.say("Invalid")
                engine.runAndWait() 
                
                
            #messagebox.showerror("ERROR","invalid user name or password")

    def iexit(self):

        self.iexit=messagebox.askyesno("LOGIN","Are you sure you want to exit")
        engine.say("Are you sure you want to exit.")
        engine.runAndWait() 

        if self.iexit>0:
            self.root.destroy()
            return

    def login_window(self):
        self.newWindow=Toplevel(self.root)
        self.log=customer(self.newWindow)

    def  customer_window(self):
        self.newWindow=Toplevel(self.root)
        self.log=customer(self.newWindow)
class  customer:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Banking Management System")
        self.root.geometry("1550x900")
        self.root.config(bg="black")
        title=Label(self.root,text="AXIS BANK ATM",font=("Apex Mk2",40,"bold"),bg="black",fg="red")
        title.pack(side=TOP,fill=X)

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=400,y=100,width=550,height=400)

        #c=Button(Manage_Frame,text="Create  Account",bg="black", fg="white",width=15,height=3,command=self.CreateAcc_window).grid(row=0,column=5,padx=220,pady=30)
        v=Button(Manage_Frame,text="Balance Enquiry",bg="black", fg="white",width=15,height=3,command=self.view_window).grid(row=0,column=5,padx=220,pady=30)
        w=Button(Manage_Frame,text="Cash Withdrawal ",bg="black", fg="white",width=15,height=3,command=self.With_window).grid(row=1,column=5,padx=20,pady=30)
        #d=Button(Manage_Frame,text="Deposit Cash",bg="black", fg="white",width=15,height=3,command=self.Deposit_window).grid(row=3,column=5,padx=20,pady=30)
        e =Button(Manage_Frame,text="EXIT",bg="black", fg="red",width=10,command=exit).grid(row=2,column=5,padx=20,pady=30)

    #def CreateAcc_window(self):
             #self.newWindow=Toplevel(self.root)
             #self.log=CreateAcc(self.newWindow)

    def With_window(self):
             self.newWindow=Toplevel(self.root)
             self.log=With(self.newWindow)

   #def Deposit_window(self):
             #self.newWindow=Toplevel(self.root)
             #self.log=Deposit(self.newWindow)

    def view_window(self):
             self.newWindow=Toplevel(self.root)
             self.log=view(self.newWindow)

class With:
    def __init__(self,root):
        self.root=root
        self.root.title("Withraw Amount")
        self.root.geometry("1350x600")
        self.root.config(bg="black")
        self.frame=Frame(self.root)
        self.frame.pack()

        title=Label(self.root,text="WITHDRAW  CASH",font=("Apex Mk2",40,"bold"),bg="black",fg="red")
        title.pack(side=TOP,fill=X)

        #self.r_name=StringVar()
        self.r_Pin=StringVar()
        self.r_WithA=StringVar()

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=400,y=210,width=650,height=250)
        
        #m=Label(Manage_Frame,text="CREATE ACCOUNT",bg="black",fg="red",font=("Apex Mk2",40,"bold"))
        #m.grid(row=0,columnspan=2,pady=20)

        #Accno=Label(Manage_Frame,text="Account Number:",bg="black",fg="white",font=("times new roman",20,"bold"))
        #Accno.grid(row=4,column=0,pady=10,padx=10,sticky="w")

        #accNo=Entry(Manage_Frame,textvariable=self.r_Accno,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        #accNo.grid(row=4,column=1,pady=10,padx=10, sticky="w")

        WithA=Label(Manage_Frame,text="Enter Amount:",bg="black",fg="white",font=("times new roman",20,"bold"))
        WithA.grid(row=5,column=0,pady=10,padx=10,sticky="w")

        With=Entry(Manage_Frame,textvariable=self.r_WithA,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        With.grid(row=5,column=1,pady=10,padx=10, sticky="w")
        
        regis=Button(Manage_Frame,text="ENTER",width=19,bg="black",fg="white",command=self.Withdraw).grid(row=8,column=0,padx=5,pady=5)
        reset=Button(Manage_Frame,text="RESET",width=19,bg="black",fg="white",command=self.ireset).grid(row=8,column=1,padx=5,pady=5)
        ext=Button(Manage_Frame,text="EXIT",width=19,bg="black",fg="red",command=exit).grid(row=8,column=2,padx=5,pady=5)


    def Withdraw(self):
        if self.r_WithA.get()=="":
            messagebox.showerror("ERROR","Amount Not Withdrawn. ")
            engine.say("please fill all the data entry field ")
            engine.runAndWait() 
            
        else:
           con=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
           cur=con.cursor()
           
           print("pin no : ",pi)
           cur.execute("select balance from customer where pin=%s",[(pi),])
           ro=cur.fetchall()
           for i in ro:
               a=i[0]
               b=int(self.r_WithA.get())
               c= int(a) - b
               print(c)
               cur.execute("update customer set balance=%s where pin=%s",(c,pi))
           
           con.commit() 
           con.close()
           messagebox.showinfo("Success.","Amount WithdrawSuccessfully.")
           engine.say("Success. ","Amount WithdrawSuccessfully.")
           engine.runAndWait() 
 
    def ireset(self):
        self.r_Accno.set("")
        self.r_WithA.set("")

class view:
    def __init__(self,root):
        self.root=root
        self.root.title("Balance Enqiury")
        self.root.geometry("1350x600")
        self.root.config(bg="black")
        self.frame=Frame(self.root)
        self.frame.pack()

        title=Label(self.root,text="Balance Enquiry",font=("Apex Mk2",40,"bold"),bg="black",fg="red")
        title.pack(side=TOP,fill=X)

        
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=400,y=210,width=650,height=250)
        
        Accno=Label(Manage_Frame,text="Account Number:",bg="black",fg="white",font=("times new roman",20,"bold"))
        Accno.grid(row=4,column=0,pady=10,padx=10,sticky="w")

        #accNo=Entry(Manage_Frame,textvariable=self.r_Accno,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        #accNo.grid(row=4,column=1,pady=10,padx=10, sticky="w")

        WithA=Label(Manage_Frame,text="Balance:",bg="black",fg="white",font=("times new roman",20,"bold"))
        WithA.grid(row=5,column=0,pady=10,padx=10,sticky="w")

        #With=Entry(Manage_Frame,textvariable=self.r_WithA,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        #With.grid(row=5,column=1,pady=10,padx=10, sticky="w")

        #regis=Button(bt_Frame,text="ENTER",width=19,bg="black",fg="white",command=self.Withdraw).grid(row=1,column=1,padx=20,pady=10)
        #reset=Button(bt_Frame,text="RESET",width=19,bg="black",fg="white",command=self.ireset).grid(row=1,column=3,padx=20,pady=10)
        ext=Button(Manage_Frame,text="EXIT",width=19,bg="black",fg="red",command=exit).grid(row=6,column=5,padx=20,pady=10)
        self.fetch_data()
        print("reached")

    def fetch_data(self):
        print("cALLED",type(pi))
        con=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
        cur=con.cursor()
        cur.execute("select accNo , balance from customer where pin=%s",(pi),)
        rows=cur.fetchall()
        if len(rows)!=0:
            for i in rows:
                print(i)
            con.commit()
        con.close()

if __name__=='__main__':
    main()
    
