
import os
from random import randint
customerfile=open('customer.txt','w')



def create_bank_account(): 
    Account_name= input('"Enter your account name : " \n')  
    while True:
        try:
            Opening_balance=int(input('"Enter your opening balance in digits : " \n'))
        except ValueError:
            print("enter a valid digit : ")
            continue
        break
    Account_type= input ('"Enter desired account type : " \n')
    Account_email=input('"Enter your email : " \n')
    Account_number = randint(1000000000,9999999999)
    print(f'Account successfuly created. Your account number is {Account_number}')
    customerfile.write(f'Account number is {Account_number} , '
                       f'Account name is {Account_name} ,  Opening balance is {Opening_balance} , '
                       f'Account type is {Account_type} , '
                       f'Account email is {Account_email}')

    customerfile.write('\n')

    customerfile.close()
    return access_account()
    #Account_name,Opening_balance,Account_type,Account_email,Account_number


def check_details():
    Response = input("Enter account number: ")
    customerfile=open('customer.txt')
    for line in customerfile:
        if Response in line:
            print(line)
            customerfile.close()
            return access_account()
    else:
        print('Data not found \n')
        return staff_login()

def staff_login():

    Username = input("Enter your username: ")
    Password = input("Enter Password : ")
    stafffile = open('staff.txt')
    for line in stafffile:
        if Username and Password in line:
            print('Successful login \n')
            stafffile.close()
            return access_account() 
    else:
        print('Invalid input, try again \n')
        stafffile.close()
        staff_login()

def access_account():
    sessionfile = open('sessionfile.txt', 'w')
    Action = input('"Enter a, b or c to Create new bank account or check account details or Logout of this session : "\n')

    if Action == "a":
        create_bank_account() 
        sessionfile.write('Customer creates account \n')
    elif Action == "b":
        check_details()
        sessionfile.write('Customer check account')
    elif Action == "c":
        sessionfile.close()
        os.remove('sessionfile.txt')
        Page_display()

    else:
        print('Type any of the options stated above')
        access_account()



def Page_display():
    print(' Welcome User , what operation would you like to perform\n')
    Feedback = input("Enter 1 to login or 2 to exit: ")
    if Feedback == "1":
       staff_login()
    elif Feedback=='2':
        quit()
    else:
        Page_display()


Page_display() 