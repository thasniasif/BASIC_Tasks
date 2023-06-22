import mysql.connector
import re

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="atm_db"
)
i = 'y'
j = 'y'


def bank_balance(val):
    query = "SELECT amnt FROM atm_tb WHERE acc_num=%s AND pin=%s"
    mycursor.execute(query, val)
    o_amnt = mycursor.fetchone()
    #print(o_amnt)
    return o_amnt


while (i == 'y'):
    choice = int(input("Enter your choice 1.Register 2.Login"))
    if (choice == 1):
        user_name = input("Enter your name")
        user_acc_num = input("Enter your account number")
        x = re.search("\d", user_acc_num)
        z = len(user_acc_num)
        if (x != None  and z == 8):
            pass

            user_pin = input("Set pin number")
            x = re.search("\d", user_pin)
            y = re.search("[a-zA-Z]", user_pin)
            z = len(user_pin)
            if (x != None and y != None and z == 4):
                pass
                user_email = input("Enter your email")
                e = re.search(".*@gmail.com$", user_email)
                em = re.search("\s", user_email)
                if (e != None and em == None):
                    user_ph_num = input("Enter phone number")
                    p = re.search("\d", user_pin)
                    if (len(user_ph_num)==10 and p!=None):

                        user_amnt = int(input("Enter first amount to deposit"))
                        if(user_amnt>=2000):
                            mycursor = mydb.cursor()
                            sql = "INSERT INTO atm_tb(name,acc_num,pin,amnt,email,ph_num) VALUES(%s,%s,%s,%s,%s,%s)"
                            val = (user_name, user_acc_num, user_pin, user_amnt,user_email,user_ph_num)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            print("Registeration Complete")

                        else:
                            print("Sorry!!! Cannot deposit...Required min balance Rs.2000")
                    else:
                        print("Invalid phone number")
                else:
                    print("Invalid email")
            else:
                print("Invalid Pin")
        else:
            print("Invalid Account number")
    elif(choice==2):
        print("Enter user id and password for login...")
        u_id = input("Enter account number")
        u_passw = input("Enter pin")

        mycursor = mydb.cursor()
        query = "SELECT * FROM atm_tb WHERE acc_num=%s AND pin=%s"
        val = (u_id, u_passw)
        mycursor.execute(query, val)
        result = mycursor.fetchone()
        if (result!=None):
            print("Login successfull")
            print(result)
            while (j == 'y'):
                choice2 = int(input("Click 1.Deposit 2.Withdraw 3.Bank Balance"))
                if (choice2 == 1):
                    u_amnt = int(input("Enter the amount to deposit"))
                    r_amnt = bank_balance(val)
                    r_amnt = list(r_amnt)
                    # print(r_amnt)
                    new_amnt = u_amnt + r_amnt[0]
                    # print(new_amnt)
                    sql = "UPDATE atm_tb SET amnt=%s WHERE acc_num=%s AND pin=%s"
                    value = (new_amnt, u_id, u_passw)
                    mycursor.execute(sql, value)
                    mydb.commit()
                elif (choice2 == 2):
                    w_amnt = int(input("Enter amount to withdraw"))
                    r_amnt = bank_balance(val)
                    r_amnt = list(r_amnt)
                    if (r_amnt[0] > 2000):
                        new_amnt = r_amnt[0] - w_amnt
                    else:
                        print("U shud hav atleast Rs.2000 mininmum to withdarw")
                        ne_amnt = r_amnt[0]
                    sql = "UPDATE atm_tb SET amnt=%s WHERE acc_num=%s AND pin=%s"
                    value = (new_amnt, u_id, u_passw)
                    mycursor.execute(sql, value)
                    mydb.commit()
                elif (choice2 == 3):
                    r_amnt = bank_balance(val)
                    r_amnt = list(r_amnt)
                    print("Current balance in your account :", r_amnt[0])

                j = input("Do you want to deposit, withdraw or check bank balance(y or n)")


        else:
            print("Invalid login")



    i=input("Do you want to register or login (y or n)")

