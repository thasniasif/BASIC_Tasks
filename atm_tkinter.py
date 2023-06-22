from tkinter import*
import tkinter.font as font
import mysql.connector
from tkinter import messagebox



top=Tk()
top.configure(bg='khaki')

NAME=StringVar()
ACCN_NUM=StringVar()
PIN=StringVar()
AMNT=StringVar()
EMAIL=StringVar()
PH_NUM=StringVar()
DEPOSIT=StringVar()
WITHDRAW=StringVar()
BALANCE=StringVar()

width = 640
height = 480
def Exit():
    result = messagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    #messagebox.showinfo("","  Successfully Deposited your amount!!!" )
    if result == 'yes':
        top.destroy()
        exit() 

def Database():
    global mydb, mycursor

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="atm_db")

    mycursor = mydb.cursor()
def gotomain_reg():
    headerframe.destroy()
    registerframe.destroy()
    mainpage()
def gotomain():
    ACCN_NUM.set("")
    PIN.set("")
    balanceframe.destroy()
    mainpage()
def gotomain_depo():
    ACCN_NUM.set("")
    PIN.set("")
    depositframe.destroy()
    mainpage()
def gotomain_with():
    ACCN_NUM.set("")
    PIN.set("")
    
    withdrawframe.destroy()
    mainpage()

def gotowith():
    ACCN_NUM.set("")
    PIN.set("")
    balanceframe.destroy()
    withdraw()
def gotodepo():
    balanceframe.destroy()
    deposit()

def toggletochoice_depo():
    depositframe.destroy()
    choice()
def toggletochoice_with():
    withdrawframe.destroy()
    choice()

def toggletoregister(event=None):
    register()
    mainframe.destroy()
    btnframe.destroy()
def toggletologin_main(event=None):
    login()
    mainframe.destroy()
    btnframe.destroy()
    
def toggletologin_register(event=None):
    headerframe.destroy()
    registerframe.destroy()
    login()
def toggletobal():
    withdrawframe.destroy()
    balance()
def depositdb():
    Database()
    mycursor = mydb.cursor()
    
    sql1="SELECT * FROM atm_tb WHERE  acc_num=%s AND pin=%s "
    val1=(ACCN_NUM.get(),PIN.get())
    mycursor.execute(sql1,val1)
    myresult = mycursor.fetchone()
    #print(myresult)
    result=list(myresult)
    #print(result[3])
    
    n_amnt=result[3]+int(DEPOSIT.get())
    #print(n_amnt)

    sql2 = "UPDATE  atm_tb SET amnt=%s WHERE acc_num=%s AND pin=%s"
    val2=(n_amnt,ACCN_NUM.get(),PIN.get())
    mycursor.execute(sql2,val2)
    
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    if(mycursor.rowcount==1):
        messagebox.showinfo("","  Successfully Deposited your amount!!!" )
    
        btn_balance=Button(depositframe,text="Check your bank balance here...",command=toggletochoice_depo,fg="red",font=("Courier",15,"bold"))
                    
        btn_balance.place(x=500,y=500)



    

def deposit():
    global depositframe
    choiceframe.destroy()
    depositframe=Frame(top)
    depositframe.pack(side=TOP,padx=60,pady=80)

    emptylabel=Label(depositframe,text="",height=100,width=200,bg="sienna3")
    emptylabel.grid(row=0,column=0)
    deposit=Label(depositframe,text="Amount to deposit : ",width=20,font=("Courier",20,"bold"))
    deposit.place(x=300,y=200)
    
    deposit_e=Entry(depositframe,width=20,textvariable=DEPOSIT,font=("Courier",20,"bold"))
    deposit_e.place(x=700,y=200)
    btn_log=Button(depositframe,text="Make Deposit",command=depositdb,fg="blue",font=("Courier",15,"bold"))
                    
    btn_log.place(x=550,y=300)
    btn_register=Button(depositframe,text="Exit",command=gotomain_depo,bg="red2",fg="black",activebackground="orange",
                        bd=10,highlightthickness = 2)
    btn_font = font.Font(size=20,weight="bold")
    btn_register['font']=btn_font
    btn_register.place(x=900,y=450)


def withdrawdb():
    Database()
    mycursor = mydb.cursor()
    
    sql1="SELECT * FROM atm_tb WHERE acc_num=%s AND pin=%s "
    val1=(ACCN_NUM.get(),PIN.get())
    mycursor.execute(sql1,val1)
    myresult = mycursor.fetchone()
    #print(myresult)
    result=list(myresult)
    
    #print(n_amnt)
    if(result[3]>=2000):
        if(result[3]-int(WITHDRAW.get())>=2000):
            n_amnt=result[3]-int(WITHDRAW.get())
            sql2 = "UPDATE  atm_tb SET amnt=%s WHERE acc_num=%s AND pin=%s"
            val2=(n_amnt,ACCN_NUM.get(),PIN.get())
            mycursor.execute(sql2,val2)
            
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
            if(mycursor.rowcount==1):
                messagebox.showinfo("","  Successfully Withdrawed your amount!!!" )
            
                btn_balance=Button(withdrawframe,text="Check your bank balance here...",command=toggletochoice_with,fg="red",font=("Courier",15,"bold"))
                            
                btn_balance.place(x=500,y=500)
        else:
            messagebox.showinfo("","Can't withdraw the amount... your balance will become less than minimum balance-2000!!!!!!")
            btn_balance=Button(withdrawframe,text="Check your bank balance here...",command=toggletobal,fg="red",font=("Courier",15,"bold"))
                    
            btn_balance.place(x=500,y=500)
    else:
            messagebox.showinfo("","You dont have the minimum amount to withdraw")
            btn_balance=Button(withdrawframe,text="Check your bank balance here...",command=toggletobal,fg="red",font=("Courier",15,"bold"))
                    
            btn_balance.place(x=500,y=500)




       
   
    
def withdraw():
    global withdrawframe
    choiceframe.destroy()
    withdrawframe=Frame(top)
    withdrawframe.pack(side=TOP,padx=60,pady=80)

    emptylabel=Label(withdrawframe,text="",height=100,width=200,bg="sienna3")
    emptylabel.grid(row=0,column=0)
    deposit=Label(withdrawframe,text="Amount to withdraw : ",width=20,font=("Courier",20,"bold"))
    deposit.place(x=300,y=200)
    
    deposit_e=Entry(withdrawframe,width=20,textvariable=WITHDRAW,font=("Courier",20,"bold"))
    deposit_e.place(x=700,y=200)
    
    btn_log=Button(withdrawframe,text="Withdraw the amount",command=withdrawdb,fg="blue",font=("Courier",15,"bold"))
                    
    btn_log.place(x=550,y=300)

    btn_register=Button(withdrawframe,text="Exit",command=gotomain_with,bg="red2",fg="black",activebackground="orange",
                        bd=10,highlightthickness = 2)
    btn_font = font.Font(size=20,weight="bold")
    btn_register['font']=btn_font
    btn_register.place(x=900,y=450)

    


def balance():
    global balanceframe
    choiceframe.destroy()
    balanceframe=Frame(top)
    balanceframe.pack(side=TOP,padx=60,pady=80)

    emptylabel=Label(balanceframe,text="",height=100,width=200,bg="sienna3")
    emptylabel.grid(row=0,column=0)
    balance_lb=Label(balanceframe,text="Your current balance : ",width=25,font=("Courier",20,"bold"))
    balance_lb.place(x=300,y=200)
    
    balance_e=Entry(balanceframe,width=20,textvariable=BALANCE,font=("Courier",20,"bold"))
    balance_e.place(x=750,y=200)
    Database()
    mycursor = mydb.cursor()
    
    sql1="SELECT * FROM atm_tb WHERE  acc_num=%s AND pin=%s "
    val1=(ACCN_NUM.get(),PIN.get())
    mycursor.execute(sql1,val1)
    myresult = mycursor.fetchone()
    
    result=list(myresult)
    BALANCE.set(result[3])
    if(result[3]>=2001):
        deposit_lb=Label(balanceframe,text="You have minimum balance 2000. Go for... ",width=50,font=("Courier",20,"bold"))
        deposit_lb.place(x=300,y=400)

        btn_login=Button(balanceframe,text="Deposit",command=gotodepo,bg="red2",fg="black",activebackground="orange",
                    bd=10,highlightthickness = 2)
        btn_font = font.Font(size=20,weight="bold")
        btn_login['font']=btn_font
        btn_login.place(x=500,y=450)
        
    

        btn_register=Button(balanceframe,text="Withdraw",command=gotowith,bg="red2",fg="black",activebackground="orange",
                        bd=10,highlightthickness = 2)
        btn_register['font']=btn_font
        btn_register.place(x=800,y=450)
    else:
        deposit_lb=Label(balanceframe,text="You don't have enough balance to withdraw. Go fro... ",width=55,font=("Courier",20,"bold"))
        deposit_lb.place(x=300,y=400)
        btn_login=Button(balanceframe,text="Deposit",command=gotodepo,bg="red2",fg="black",activebackground="orange",
                    bd=10,highlightthickness = 2)
        btn_font = font.Font(size=20,weight="bold")
        btn_login['font']=btn_font
        btn_login.place(x=500,y=450)

    btn_register=Button(balanceframe,text="Exit",command=gotomain,bg="red2",fg="black",activebackground="orange",
                    bd=10,highlightthickness = 2)
    btn_register['font']=btn_font
    btn_register.place(x=800,y=450)

        







    

def choice():
    global choiceframe
    choiceframe=Frame(top)
    choiceframe.pack(side=TOP,padx=60,pady=80)
    emptylabel=Label(choiceframe,text="",height=100,width=200,bg="sienna3")
    emptylabel.grid(row=0,column=0)
    
    btn_login=Button(choiceframe,text="Deposit",command=deposit,bg="red2",fg="black",activebackground="orange",
                    bd=10,highlightthickness = 2)
    btn_font = font.Font(size=30,weight="bold")
    btn_login['font']=btn_font
    btn_login.place(x=200,y=200)
 

    btn_register=Button(choiceframe,text="Withdraw",command=withdraw,bg="red2",fg="black",activebackground="orange",
                    bd=10,highlightthickness = 2)
    btn_register['font']=btn_font
    btn_register.place(x=500,y=200)

    btn_login=Button(choiceframe,text="Check Balance",command=balance,bg="red2",fg="black",activebackground="orange",
                    bd=10,highlightthickness = 2)
    btn_font = font.Font(size=30,weight="bold")
    btn_login['font']=btn_font
    btn_login.place(x=800,y=200)

    

def login():
    global loginframe
    loginframe=Frame(top)
    loginframe.pack(side=TOP,padx=60,pady=80)

    emptylabel=Label(loginframe,text="",height=100,width=200,bg="sienna3")
    emptylabel.grid(row=0,column=0)
   
    accn_num=Label(loginframe,text="Account number  : ",width=20,font=("Courier",20,"bold"))
    accn_num.place(x=300,y=200)
    
    accn_num_e=Entry(loginframe,width=20,textvariable=ACCN_NUM,font=("Courier",20,"bold"))
    accn_num_e.place(x=700,y=200)
    

    pin=Label(loginframe,text="pin   :  ",width=20,font=("Courier",20,"bold"))
    pin.place(x=300,y=250)
    pin_e=Entry(loginframe,width=20,textvariable=PIN,font=("Courier",20,"bold"),show="*")
    pin_e.place(x=700,y=250)

    btn_login=Button(loginframe,text="Login",command=logindb,bg="red2",fg="black",activebackground="orange",
                 bd=10,highlightthickness = 2)
    btn_font = font.Font(size=20,weight="bold")
    btn_login['font']=btn_font
    btn_login.place(x=600,y=350)
    

   
    
    
    
    


def logindb():
    Database()
    mycursor = mydb.cursor()
    #mycursor2 = mydb.cursor()
    sql = "SELECT * FROM atm_tb WHERE acc_num=%s AND pin=%s"
    val=(ACCN_NUM.get(),PIN.get())
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    #print(myresult)
    result=list(myresult)
    #print(result[0][1])
    if(mycursor.rowcount==1):
        #print(mycursor.rowcount, "record selected")
        messagebox.showinfo("","Login  Successfully!!!")
        loginframe.destroy()
        choice()
    elif(ACCN_NUM.get()=="" or PIN.get()==""):
         messagebox.showinfo("","Account number and pin can't be empty!!!")
    else:
         messagebox.showinfo("","Please enter valid account number or pin !!!")

    

        

    

    # ACCN_NUM.set("")
    # PIN.set("")
    

     

   
    
   
def registerdb():
    Database()
    mycursor = mydb.cursor()
    sql = "INSERT INTO atm_tb (name,acc_num,pin,amnt,email,ph_num) VALUES (%s, %s,%s,%s,%s,%s)"
    val = (NAME.get(), ACCN_NUM.get(), PIN.get(),AMNT.get(),EMAIL.get(),PH_NUM.get())
    mycursor.execute(sql, val)
    mydb.commit()
    if(NAME.get()=="" or ACCN_NUM.get()=="" or PIN.get()=="" or AMNT.get()=="" or EMAIL.get()=="" or PH_NUM.get()==""):
         messagebox.showinfo("","PLease fill all the feilds!!!")
    elif(mycursor.rowcount==1):
        print(mycursor.rowcount, "record inserted.")
        messagebox.showinfo("","Registered Successfully")
   
    
    NAME.set("")
    ACCN_NUM.set("")
    PIN.set("")
    AMNT.set("")
    EMAIL.set("")
    PH_NUM.set("")
    btn_log=Button(registerframe,text="Now Login here...",command=toggletologin_register,fg="blue",font=("Courier",15,"bold"))
                    
    btn_log.place(x=600,y=50)
    


    # lb_login=Label(registerframe,text="Now Login here...",fg="blue",font=("Courier",20,"bold"))
    # lb_login.place(x=600,y=50)
    # lb_login.bind('<Button-1>', toggletologin)
        


    




def register():
    
    global NAME,ACCN_NUM,PIN,AMNT,EMAIL,PH_NUM,registerframe,headerframe,label_font,entry_font
    headerframe=Frame(top)
    headerframe.pack(side=TOP,pady=10,padx=80)
    registerframe=Frame(top)
    registerframe.pack(side=LEFT,pady=50,padx=0,anchor="center")


    main_label1=Label(headerframe,text="Hello...If you are a new user, ",width=80,height=1)
    main_label2=Label(headerframe,text="please enter your details and register below!!!",width=80,height=1)
    main_label1.grid(row=0,column=0)
    main_label1.config(font=("Courier",20,"bold"))
    main_label2.grid(row=1,column=0)
    main_label2.config(font=("Courier",20,"bold"))

    emptylabel=Label(registerframe,text="",height=100,width=200,bg="sienna3")
    emptylabel.pack(side=TOP,pady=0)

    label_font=font.Font(size=20,weight="bold")
    entry_font=font.Font(size=20)

    name=Label(registerframe,text="NAME  :  ",width=20,bg="brown4",fg="white")
    name['font']=label_font
    name.place(x=300,y=100)
    name_e=Entry(registerframe,width=20,bg="brown4",fg="white",textvariable=NAME)
    name_e.place(x=800,y=100)
    name_e['font']=entry_font
   

    accn_num=Label(registerframe,text="Account number  :  ",width=20,bg="brown4",fg="white")
    accn_num['font']=label_font
    accn_num.place(x=300,y=150)
    accn_num_e=Entry(registerframe,width=20,bg="brown4",fg="white",textvariable=ACCN_NUM)
    accn_num_e.place(x=800,y=150)
    accn_num_e['font']=entry_font
    #ACCN_NUM=accn_num_e.get()

    pin=Label(registerframe,text="pin   :  ",width=20,bg="brown4",fg="white")
    pin['font']=label_font
    pin.place(x=300,y=200)
    pin_e=Entry(registerframe,width=20,bg="brown4",fg="white",textvariable=PIN)
    pin_e.place(x=800,y=200)
    pin_e['font']=entry_font
   # PIN=pin_e.get()

    email=Label(registerframe,text="Email id   :  ",width=20,bg="brown4",fg="white")
    email['font']=label_font
    email.place(x=300,y=250)
    email_e=Entry(registerframe,width=20,bg="brown4",fg="white",textvariable=EMAIL)
    email_e.place(x=800,y=250)
    email_e['font']=entry_font
    #EMAIL=email_e.get()

    ph_num=Label(registerframe,text="Phone number   :  ",width=20,bg="brown4",fg="white")
    ph_num['font']=label_font
    ph_num.place(x=300,y=300)
    ph_num_e=Entry(registerframe,width=20,bg="brown4",fg="white",textvariable=PH_NUM)
    ph_num_e.place(x=800,y=300)
    ph_num_e['font']=entry_font
    #PH_NUM=ph_num_e.get()

    amnt=Label(registerframe,text="First deposit   :  ",width=20,bg="brown4",fg="white")
    amnt['font']=label_font
    amnt.place(x=300,y=350)
    amnt_e=Entry(registerframe,width=20,bg="brown4",fg="white",textvariable=AMNT)
    amnt_e.place(x=800,y=350)
    amnt_e['font']=entry_font
    #AMNT=amnt_e.get()
   
    


    btn_register=Button(registerframe,text="Register",command=registerdb,bg="red2",fg="black",activebackground="orange",
                        bd=10)
    btn_register.place(x=650,y=420)
    btn_font = font.Font(size=18,weight="bold")
    btn_register['font']=btn_font
    btn_register=Button(registerframe,text="Exit",command=gotomain_reg,bg="red2",fg="black",activebackground="orange",
                    bd=10,highlightthickness = 2)
    btn_register['font']=btn_font
    btn_register.place(x=800,y=420)
   





                

#.............................MAIN PAGE..................#
def mainpage():
    global mainframe,btnframe
    mainframe=Frame(top)
    mainframe.pack(side=TOP, pady=0)
    btnframe=Frame(top)
    btnframe.pack(side=TOP, pady=50)


    atm1=Label(mainframe,text="Helloo...",width=40,fg="black",bg="chocolate3")
    atm1.grid(row=0,column=0)
    atm2=Label(mainframe,text="Welcome to ATM Machine!!!",bg="chocolate3",width=50,height=2)
    atm2.grid(row=1,column=0)

    atm1.config(font=("Courier",50,"bold"))
    atm2.config(font=("Courier",40,"bold","italic"))


    btnlabel=Label(btnframe,text="",height=100,width=200,bg="brown")
    btnlabel.pack(side=TOP,pady=0)
    btn_login=Button(btnframe,text="Login",command=toggletologin_main,bg="red2",fg="black",activebackground="orange",
                    bd=10,highlightthickness = 2)
    btn_font = font.Font(size=30,weight="bold")
    btn_login['font']=btn_font
    btn_login.place(x=500,y=100)

    btn_register=Button(btnframe,text="Register",command=toggletoregister,bg="red2",fg="black",activebackground="orange",
                    bd=10,highlightthickness = 2)
    btn_register['font']=btn_font
    btn_register.place(x=700,y=100)

mainpage()
menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="file", menu=filemenu)
top.config(menu=menubar)


top.mainloop()