account=[]
def create_account():
    payee=input("Enter payee")
    amount=input("Enter amount")
    date=input("Enter date ")
    account.append((payee,amount,date))
def display_account():
    print(account)
def delete_account():
    i=int(input("Enter the index you want to remove"))
    account.pop(i)
def update_account():
    i=int(input("Enter the index you want to update"))
    payee=input("Enter payee")
    amount=input("Enter amount")
    date=input("Enter date")
    account[i]=(payee,amount,date)
def menu():
    print("Menu")
    print("1->For insert new account")
    print("2->For Display account")
    print("3->For Delete account")
    print("4->For Update")
    op=int(input("Enter Your Option"))
    return op