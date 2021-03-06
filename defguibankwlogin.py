from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import re
#import pyttsx3
#engine = pyttsx3.init()
#voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. of for male
#engine.setProperty('voice', voices[1].id)  

def main():
    root=Tk()
    #customer(root)
    login(root)

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1550x900")
        self.root.config(bg="black")
        self.frame=Frame(bg="black")
        self.frame.pack()
        
        self.Username=StringVar()
        self.Password=StringVar()

        self.title=Label(self.frame,text="LOGIN ",bd=2,relief=GROOVE,font=("times new roman",20,"bold"),bg="BLACK",fg="red")
        self.title.grid(row=0,column=0,columnspan=2,pady=20)

        #=============================================Login Frames=================================================================
        #self.login1=LabelFrame(self.frame,width=125,height=350,font=("times new roman",20,"bold"),relief=GROOVE,bg='BLACK')
       # self.login1.grid(row=3,column=0)
        #self.login2=LabelFrame(self.frame,width=110,height=280,font=("times new roman",20,"bold"),relief=GROOVE,bg='black')
        #self.login2.grid(row=5,column=0)

        Manage_Frame=Frame(self.root,bg="BLACK",bd=4,relief=RIDGE)
        Manage_Frame.place(x=350,y=100,width=700,height=550)
        #m=Label(Manage_Frame)
        #m.grid(row=0,columnspan=2,pady=20)
        #=======================================================Login Frame Entry Field================================================
        username=Label(Manage_Frame,text="Username:",bg="black",fg="white",font=("Lucida Sans Unicode",20,"bold"))
        username.grid(row=4,column=0,pady=10,padx=10,sticky="w")

        txtusername=Entry(Manage_Frame,textvariable=self.Username,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        txtusername.grid(row=5,column=1,pady=10,padx=10, sticky="w")

        password=Label(Manage_Frame,text="Password:",bg="black",fg="white",font=("Lucida Sans Unicode",20,"bold"))
        password.grid(row=7,column=0,pady=10,padx=10,sticky="w")

        txtpas=Entry(Manage_Frame,textvariable=self.Password,show="*",font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        txtpas.grid(row=8,column=1,pady=10,padx=10, sticky="w")

        #self.username=Label(self.login1,text='Username',font=("times new roman",25,"bold"),bg="black",fg="white")
        #self.username.grid(row=0,column=0)

        #self.txtusername=Entry(self.login1,font=("times new roman",25,"bold"),textvariable=self.Username,width=30)
        #self.txtusername.grid(row=0,column=1,padx=55)

        #self.password=Label(self.login1,text='Password',font=("times new roman",25,"bold"),bg="black",fg="white")
        #self.password.grid(row=1,column=0)

        #self.txtpas=Entry(self.login1,font=("times new roman",25,"bold"),show="*",textvariable=self.Password,width=30)
        #self.txtpas.grid(row=1,column=1,columnspan=2,pady=30)
        
        #============================Log Frame Button============================================================================
        bt_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        bt_Frame.place(x=370,y=520,width=660,height=60)

        regis=Button(bt_Frame,text="LOGIN",width=19,bg="black",fg="white",command=self.login_system).grid(row=1,column=1,padx=10,pady=5)
        reset=Button(bt_Frame,text="RESET",width=19,bg="black",fg="white",command=self.ireset).grid(row=1,column=3,padx=10,pady=5)
        exet=Button(bt_Frame,text="EXIT",width=19,bg="black",fg="red",command=self.iexit).grid(row=1,column=5,padx=10,pady=5)
        ext=Button(bt_Frame,text="SIGNUP",width=19,bg="black",fg="red",command=self.regestration_window).grid(row=1,column=7,padx=10,pady=5)



        #self.btlog=Button(self.login2,text='Login',font=("times new roman",20,"bold"),width=5,bg="black",fg="white",command=self.login_system)
        #self.btlog.grid(row=3,column=0)#,pady=20,padx=8)

       # self.btreset=Button(self.login2,text='Reset',font=("times new roman",20,"bold"),width=5,bg="black",fg="white",command=self.ireset)
        #self.btreset.grid(row=3,column=1)#,padx=8,pady=20)

        #self.exit=Button(self.login2,text='Exit',font=("times new roman",20,"bold"),width=5,bg="black",fg="white",command=self.iexit)
        #self.exit.grid(row=3,column=2)#,padx=8,pady=20)

        #self.register=Button(self.login2,text='Register',font=("times new roman",20,"bold"),width=6,bg="black",fg="white",command=self.regestration_window)
        #self.register.grid(row=3,column=3)#padx=8,pady=20)
        
        
        #================================================Command Section========================================================

    def login_system(self):
        if self.Username.get()=="" or self.Password.get()=="":
            messagebox.askyesno("LOGIN","Please enter all the field")
            engine.say("Please enter all the field")
            engine.runAndWait() 
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
            cur=con.cursor()
            cur.execute("select * from login where uname=%s and pword=%s",[(self.Username.get()),(self.Password.get())])
            re=cur.fetchall()
            if re:
                for i in re:
                    self.login_window()
                    #con.commit()
            else:
                messagebox.showerror("LOGIN","Invalid  Username or Password.")
                engine.say("Invalid")
                engine.runAndWait() 
                
                
            #messagebox.showerror("ERROR","invalid user name or password")
    def ireset(self):
        self.Username.set("")
        self.Password.set("")

    def iexit(self):

        self.iexit=messagebox.askyesno("LOGIN","Are you sure you want to exit")

        if self.iexit>0:
            self.root.destroy()
            #return

    def login_window(self):
        self.root.withdraw()
        self.newWindow=Toplevel(self.root)
        self.log=customer(self.newWindow)

    def regestration_window(self):
        self.root.withdraw()
        self.newWindow=Toplevel(self.root)
        self.log=register(self.newWindow)

    def  customer_window(self):
        self.root.withdraw()
        self.newWindow=Toplevel(self.root)
        self.log=customer(self.newWindow)

    

    
class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register page")
        self.root.geometry("1550x900")
        self.root.config(bg="black")
        self.frame=Frame(self.root,bg="black")
        self.frame.pack()

        #title=Label(self.root,text="REGISTER",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        #itle.pack(side=TOP,fill=X)

        self.r_username=StringVar()
        self.r_password=StringVar()
        self.r_name=StringVar()
        self.r_eid=StringVar()
        self.r_ph=StringVar()

        Manage_Frame=Frame(self.root,bg="BLACK",bd=4,relief=RIDGE)
        Manage_Frame.place(x=400,y=100,width=600,height=490)
        m=Label(Manage_Frame,text="SIGNING UP",bg="black",fg="white",font=("Lucida Sans Unicode",40,"bold"))
        m.grid(row=0,columnspan=2,pady=20)

        name=Label(Manage_Frame,text="Name:",bg="black",fg="white",font=("Lucida Sans Unicode",20,"bold"))
        name.grid(row=3,column=0,pady=10,padx=10,sticky="w")

        nam=Entry(Manage_Frame,textvariable=self.r_name,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        nam.grid(row=3,column=1,pady=10,padx=10, sticky="w")

        uname=Label(Manage_Frame,text="Username:",bg="black",fg="white",font=("Lucida Sans Unicode",20,"bold"))
        uname.grid(row=4,column=0,pady=10,padx=10,sticky="w")

        unam=Entry(Manage_Frame,textvariable=self.r_username,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        unam.grid(row=4,column=1,pady=10,padx=10, sticky="w")

        eid=Label(Manage_Frame,text="Employee ID:",bg="black",fg="white",font=("Lucida Sans Unicode",20,"bold"))
        eid.grid(row=5,column=0,pady=10,padx=10,sticky="w")

        e=Entry(Manage_Frame,textvariable=self.r_eid,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        e.grid(row=5,column=1,pady=10,padx=10, sticky="w")

        no=Label(Manage_Frame,text="Phone Number:",bg="black",fg="white",font=("Lucida Sans Unicode",20,"bold"))
        no.grid(row=6,column=0,pady=10,padx=10,sticky="w")

        n=Entry(Manage_Frame,textvariable=self.r_ph,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        n.grid(row=6,column=1,pady=10,padx=10, sticky="w")

        upassword=Label(Manage_Frame,text="Create Password:",bg="black",fg="white",font=("Lucida Sans Unicode",20,"bold"))
        upassword.grid(row=7,column=0,pady=10,padx=10,sticky="w")

        upas=Entry(Manage_Frame,textvariable=self.r_password,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        upas.grid(row=7,column=1,pady=10,padx=10, sticky="w")

        bt_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        bt_Frame.place(x=350,y=600,width=720,height=50)

        regis=Button(bt_Frame,text="REGISTER",width=19,bg="black",fg="white",command=self.register).grid(row=1,column=1,padx=20,pady=10)
        chk=Button(bt_Frame,text="Check",width=19,bg="black",fg="white",command=self.check).grid(row=1,column=3,padx=20,pady=10)
        reset=Button(bt_Frame,text="RESET",width=19,bg="black",fg="white",command=self.ireset).grid(row=1,column=5,padx=20,pady=10)
        ext=Button(bt_Frame,text="EXIT",width=19,bg="black",fg="red",command=self.ie).grid(row=1,column=7,padx=20,pady=10)


    def register(self):
        if  self.r_name.get()=="" or self.r_username.get()=="" or self.r_password.get()=="":
            messagebox.showerror("ERROR","Fields are empty")
            engine.say("Fields are empty")
            engine.runAndWait()

            self.check()
            
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
            cur=con.cursor()
            cur.execute("insert into login values(%s,%s)",(self.r_username.get(),self.r_password.get()))
            cur.execute("insert into register values(%s,%s,%s)",(self.r_name.get(),self.r_username.get(),self.r_password.get()))
            con.commit() 
            con.close()
            messagebox.showinfo("REGISTER ","REGISTRATION DONE")

    def ireset(self):
        self.r_name.set("")
        self.r_username.set("")
        self.r_password.set("")

    def iexit(self):
        self.iexit=messagebox.askyesno("LOGIN","confirm if you want to exit")
        if self.iexit>0:
            self.root.destroy()
            #return

    def ie(self):
        self.root.withdraw()
        self.newWindow=Toplevel(self.root)
        self.log=login(self.newWindow)

    def check(self): 
        #passwd = 'Geek12@'
        passwd=self.r_password.get()
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
      
        # compiling regex 
        pat = re.compile(reg) 
      
        # searching regex                  
        mat = re.search(pat, passwd) 
      
        # validating conditions 
        if mat: 
            messagebox.showinfo("OK ","Password is Vaild")
        else: 
            messagebox.showinfo("Please Enter a vaild password "," 1.length should be at least 6 2. length should be not be greater than 20 3.Password should have at least one numeral 4.Password should have at least one uppercase letter. 5.Password should have at least one lowercase letter.6.Password should have at least one of the symbols $@#")
      

    
    
    
class  customer:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Banking Management System")
        self.root.geometry("1550x900")
        self.root.config(bg="black")
        self.frame=Frame(self.root)
        self.frame.pack()

        title=Label(self.root,text="Banking System",font=("Apex Mk2",40,"bold"),bg="black",fg="red")
        title.pack(side=TOP,fill=X)

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=400,y=100,width=550,height=550)

        c=Button(Manage_Frame,text="Create  Account",bg="black", fg="white",width=15,height=3,command=self.CreateAcc_window).grid(row=0,column=5,padx=220,pady=30)
        v=Button(Manage_Frame,text="View Accounts",bg="black", fg="white",width=15,height=3,command=self.view_window).grid(row=1,column=5,padx=20,pady=30)
        w=Button(Manage_Frame,text="Withdraw Amount ",bg="black", fg="white",width=15,height=3,command=self.With_window).grid(row=2,column=5,padx=20,pady=30)
        d=Button(Manage_Frame,text="Deposit Amount",bg="black", fg="white",width=15,height=3,command=self.Deposit_window).grid(row=3,column=5,padx=20,pady=30)
        e =Button(Manage_Frame,text="EXIT",bg="black", fg="red",width=10,command=self.iexit).grid(row=4,column=5,padx=20,pady=10)

    def CreateAcc_window(self):
             self.newWindow=Toplevel(self.root)
             self.log=CreateAcc(self.newWindow)

    def With_window(self):
             self.newWindow=Toplevel(self.root)
             self.log=With(self.newWindow)

    def Deposit_window(self):
             self.newWindow=Toplevel(self.root)
             self.log=Deposit(self.newWindow)

    def view_window(self):
             self.newWindow=Toplevel(self.root)
             self.log=view(self.newWindow)

    def iexit(self):

        self.iexit=messagebox.askyesno("LOGIN","Are you sure you want to exit")
        self.iexit>0
        self.root.withdraw()
        self.root=Toplevel(self.login)
        
            
            

class CreateAcc:
    def __init__(self,root):
        self.root=root
        self.root.title("Creating Account")
        self.root.geometry("1550x900")
        self.root.config(bg="black")
        self.frame=Frame(self.root)
        self.frame.pack()

        title=Label(self.root,text="CREATING ACCOUNT",font=("Apex Mk2",40,"bold"),bg="black",fg="red")
        title.pack(side=TOP,fill=X)

        self.r_name=StringVar()
        self.r_Accno=StringVar()
        self.r_bal=StringVar()
        self.r_type=StringVar()
        self.r_aad=StringVar()
        self.r_pan=StringVar()
        self.r_phone=StringVar()

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=400,y=100,width=600,height=500)
        
        #m=Label(Manage_Frame,text="CREATE ACCOUNT",bg="black",fg="red",font=("Apex Mk2",40,"bold"))
        #m.grid(row=0,columnspan=2,pady=20)

        name=Label(Manage_Frame,text="Account Holder Name:",bg="black",fg="white",font=("times new roman",20,"bold"))
        name.grid(row=3,column=0,pady=10,padx=10,sticky="w")

        nam=Entry(Manage_Frame,textvariable=self.r_name,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        nam.grid(row=3,column=1,pady=5,padx=5, sticky="w")

        Accno=Label(Manage_Frame,text="Account Number:",bg="black",fg="white",font=("times new roman",20,"bold"))
        Accno.grid(row=4,column=0,pady=10,padx=10,sticky="w")

        accNo=Entry(Manage_Frame,textvariable=self.r_Accno,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        accNo.grid(row=4,column=1,pady=10,padx=10, sticky="w")

        bal=Label(Manage_Frame,text="Initial Balance:",bg="black",fg="white",font=("times new roman",20,"bold"))
        bal.grid(row=5,column=0,pady=10,padx=10,sticky="w")

        bala=Entry(Manage_Frame,textvariable=self.r_bal,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        bala.grid(row=5,column=1,pady=10,padx=10, sticky="w")

        t=Label(Manage_Frame,text="Type of Account[C/S]:",bg="black",fg="white",font=("times new roman",20,"bold"))
        t.grid(row=6,column=0,pady=10,padx=10,sticky="w")

        ty=ttk.Combobox(Manage_Frame,textvariable=self.r_type,font=("time new roman",15,"bold"))
        ty['values']=("Saving","Current")
        ty.grid(row=6,column=1,pady=10,padx=10, sticky="w")

        an=Label(Manage_Frame,text="Aadhar Number:",bg="black",fg="white",font=("times new roman",20,"bold"))
        an.grid(row=7,column=0,pady=10,padx=10,sticky="w")

        al=Entry(Manage_Frame,textvariable=self.r_aad,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        al.grid(row=7,column=1,pady=10,padx=10, sticky="w")

        p=Label(Manage_Frame,text="Pan card No. :",bg="black",fg="white",font=("times new roman",20,"bold"))
        p.grid(row=8,column=0,pady=10,padx=10,sticky="w")

        pl=Entry(Manage_Frame,textvariable=self.r_pan,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        pl.grid(row=8,column=1,pady=10,padx=10, sticky="w")

        ph=Label(Manage_Frame,text="Phone Number:",bg="black",fg="white",font=("times new roman",20,"bold"))
        ph.grid(row=9,column=0,pady=10,padx=10,sticky="w")

        phl=Entry(Manage_Frame,textvariable=self.r_phone,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        phl.grid(row=9,column=1,pady=10,padx=10, sticky="w")

        bt_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        bt_Frame.place(x=400,y=560,width=600,height=50)

        regis=Button(bt_Frame,text="CREATE",width=19,bg="black",fg="white",command=self.create).grid(row=1,column=1,padx=20,pady=10)
        reset=Button(bt_Frame,text="RESET",width=19,bg="black",fg="white",command=self.ireset).grid(row=1,column=3,padx=20,pady=10)
        ext=Button(bt_Frame,text="EXIT",width=19,bg="black",fg="red",command=self.ie).grid(row=1,column=5,padx=20,pady=10)


    def create(self):
        if  self.r_name.get()=="" or self.r_bal.get()=="" or self.r_type.get()=="":
            messagebox.showerror("Account not Created.","please fill all the data entery field ")
            engine.say(" ")
            engine.runAndWait()   
        else:
            if(re.search()):
            #a= id(self.r_aad)
            #con=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
            #cur=con.cursor()
            #cur.execute("insert into customer values(%s,%s,%s,%s)",(self.r_name.get(),self.r_Accno.get(),self.r_bal.get(),self.r_type.get()))
            #cur.execute("insert into register values(%s,%s,%s)",(self.r_name.get(),self.r_username.get(),self.r_password.get()))
            
            #con.commit() 
            #con.close()
            #messagebox.showinfo("Success","Account Created Successfully.")
            #engine.say("Success","Account Created Successfully.")
            #engine.runAndWait() 
            

   def ireset(self):
       self.r_name.set("")
       self.r_Accno.set("")
       self.r_bal.set("")
       self.r_type.set("")
       self.r_aad.set("")
       self.r_pan.set("")
       self.r_phone.set("")

    def ie(self):
        self.root.withdraw()
        self.root=Toplevel(self.customer)


      

class With:
    def __init__(self,root):
        self.root=root
        self.root.title("Withraw Amount")
        self.root.geometry("1550x900")
        self.root.config(bg="black")
        self.frame=Frame(self.root)
        self.frame.pack()

        title=Label(self.root,text="WITHDRAW AMOUNT",font=("Apex Mk2",40,"bold"),bg="black",fg="red")
        title.pack(side=TOP,fill=X)

        #self.r_name=StringVar()
        self.r_Accno=StringVar()
        self.r_WithA=StringVar()
        
        

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=400,y=210,width=600,height=250)
        
        #m=Label(Manage_Frame,text="CREATE ACCOUNT",bg="black",fg="red",font=("Apex Mk2",40,"bold"))
        #m.grid(row=0,columnspan=2,pady=20)

        Accno=Label(Manage_Frame,text="Account Number:",bg="black",fg="white",font=("times new roman",20,"bold"))
        Accno.grid(row=4,column=0,pady=10,padx=10,sticky="w")

        accNo=Entry(Manage_Frame,textvariable=self.r_Accno,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        accNo.grid(row=4,column=1,pady=10,padx=10, sticky="w")

        WithA=Label(Manage_Frame,text="Withraw Amount:",bg="black",fg="white",font=("times new roman",20,"bold"))
        WithA.grid(row=5,column=0,pady=10,padx=10,sticky="w")

        With=Entry(Manage_Frame,textvariable=self.r_WithA,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        With.grid(row=5,column=1,pady=10,padx=10, sticky="w")

        bt_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        bt_Frame.place(x=400,y=560,width=600,height=50)

        regis=Button(bt_Frame,text="WITHDRAW",width=19,bg="black",fg="white",command=self.Withdraw).grid(row=1,column=1,padx=20,pady=10)
        reset=Button(bt_Frame,text="RESET",width=19,bg="black",fg="white",command=self.ireset).grid(row=1,column=3,padx=20,pady=10)
        ext=Button(bt_Frame,text="BACK",width=19,bg="black",fg="red",command=self.ie).grid(row=1,column=5,padx=20,pady=10)


    def Withdraw(self):
        if  self.r_Accno.get()=="" or self.r_WithA.get()=="":
            messagebox.showerror("ERROR","Amount Not Withdrawn. ")
            engine.say("please fill all the data entery field ")
            engine.runAndWait() 
            
        else:
           con=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
           cur=con.cursor()
           cur.execute("select balance  from customer where accNo=%s",(self.r_Accno.get(),))
           ro=cur.fetchall()
           for i in ro:
               
               a=i[0]
               b=int(self.r_WithA.get())
               c= int(a) - b
               cur.execute("update  customer set balance=%s where accNo=%s",(c,self.r_Accno.get()))
           
           con.commit() 
           con.close()
           messagebox.showinfo("Success. ","Amount WithdrawSuccessfully.")
           engine.say("Success. ","Amount WithdrawSuccessfully.")
           engine.runAndWait() 
 
    def ireset(self):
        self.r_Accno.set("")
        self.r_WithA.set("")

    def ie(self):
        self.root.withdraw()
        self.root=Toplevel(self.customer)
        

 
class Deposit:
    def __init__(self,root):
        self.root=root
        self.root.title("Deposit Amount")
        self.root.geometry("1550x900")
        self.root.config(bg="black")
        self.frame=Frame(self.root)
        self.frame.pack()

        title=Label(self.root,text="DEPOSIT AMOUNT",font=("Apex Mk2",40,"bold"),bg="black",fg="red")
        title.pack(side=TOP,fill=X)

        #self.r_name=StringVar()
        self.r_Accno=StringVar()
        self.r_deposit=StringVar()

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=400,y=210,width=600,height=250)
        
        #m=Label(Manage_Frame,text="CREATE ACCOUNT",bg="black",fg="red",font=("Apex Mk2",40,"bold"))
        #m.grid(row=0,columnspan=2,pady=20)

        Accno=Label(Manage_Frame,text="Account Number:",bg="black",fg="white",font=("times new roman",20,"bold"))
        Accno.grid(row=4,column=0,pady=10,padx=10,sticky="w")

        accNo=Entry(Manage_Frame,textvariable=self.r_Accno,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        accNo.grid(row=4,column=1,pady=10,padx=10, sticky="w")

        depo=Label(Manage_Frame,text=" Deposit Amount:",bg="black",fg="white",font=("times new roman",20,"bold"))
        depo.grid(row=5,column=0,pady=10,padx=10,sticky="w")

        deposit=Entry(Manage_Frame,textvariable=self.r_deposit,font=("time new roman",15,"bold"),bd=10,relief=GROOVE)
        deposit.grid(row=5,column=1,pady=10,padx=10, sticky="w")

        bt_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        bt_Frame.place(x=400,y=560,width=600,height=50)

        regis=Button(bt_Frame,text="DEPOSIT",width=19,bg="black",fg="white",command=self.DEPO).grid(row=1,column=1,padx=20,pady=10)
        reset=Button(bt_Frame,text="RESET",width=19,bg="black",fg="white",command=self.ireset).grid(row=1,column=3,padx=20,pady=10)
        ext=Button(bt_Frame,text="BACK",width=19,bg="black",fg="red",command=self.ie).grid(row=1,column=5,padx=20,pady=10)


    def DEPO(self):
        if  self.r_Accno.get()=="" or self.r_deposit.get()=="":
            messagebox.showerror("ERROR","Amount Not Deposited. ")
            engine.say("please fill all the data entery field ")
            engine.runAndWait() 
            
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
            cur=con.cursor()
            cur.execute("select  balance from customer where accNo=%s",(self.r_Accno.get(),))
            f=cur.fetchall()
            for i in f:
                a=i[0]
                b=int(self.r_deposit.get())
                c=int(a)+b
                cur.execute("update  customer set balance=%s where accNo=%s",(c,self.r_Accno.get()))
            #cur.execute("insert into register values(%s,%s,%s)",(self.r_name.get(),self.r_username.get(),self.r_password.get()))
            
            con.commit() 
            con.close()
            messagebox.showinfo("Success. ","Amount Deposited Successfully.")

    def ireset(self):
        self.r_Accno.set("")
        self.r_deposit.set("")

    def ie(self):
        self.root.withdraw()
        self.root=Toplevel(self.customer)
        #self.log=customer(self.Window)

class view:
    def __init__(self,root):
        self.root=root
        self.root.title("View Accounts")
        self.root.geometry("1550x900")
        self.root.config(bg="black")
        self.frame=Frame(self.root)
        self.frame.pack()
        
        #Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        #Manage_Frame.place(x=400,y=210,width=900,height=600)
        
        Table_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Table_Frame.place(x=300,y=150,width=870,height=480)
        
        x_scroll=Scrollbar(Table_Frame,orient=HORIZONTAL)
        y_scroll=Scrollbar(Table_Frame,orient=VERTICAL)
        self.customer_Table=ttk.Treeview(Table_Frame,column=("Name","Account Number","Initial_Balance","Type"),xscrollcommand=x_scroll.set,yscrollcommand=y_scroll.set)
        x_scroll.pack(side=BOTTOM,fill=X)
        y_scroll.pack(side=RIGHT,fill=Y)
        x_scroll.config(command=self.customer_Table.xview)
        y_scroll.config(command=self.customer_Table.yview)
        self.customer_Table.heading("Name",text="Name")
        self.customer_Table.heading("Account Number",text="Account Number")
        self.customer_Table.heading("Initial_Balance",text="Balance")
        self.customer_Table.heading("Type",text="Type")
        self.customer_Table['show']='headings'
        self.customer_Table.column("Name",width=100)
        self.customer_Table.column("Account Number",width=100)
        self.customer_Table.column("Initial_Balance",width=100)
        self.customer_Table.column("Type",width=100)
        self.customer_Table.pack(fill=BOTH,expand=1)
        self.customer_Table.bind("<ButtonRelease-1>")
        self.fetch_data()

    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
        cur=con.cursor()
        cur.execute("select * from customer")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.customer_Table.delete(*self.customer_Table.get_children())
            for i in rows:
                self.customer_Table.insert('',END,values=i)
            con.commit()
        con.close()

if __name__=='__main__':
    main()
    
