contact=[]
def create_contact():
    name=input("Enter Name")
    email=input("Enter Email")
    mobile=input("Enter Mobile")
    contact.append((name,email,mobile))
def display_contact():
    print(contact)
def delete_contact():
    i=int(input("Enter the index you want to remove"))
    contact.pop(i)
def update_contact():
    i=int(input("Enter the index you want to update"))
    name=input("Enter Name")
    email=input("Enter Email")
    mobile=input("Enter Mobile")
    contact[i]=(name,email,mobile)
def menu():
    print("Menu")
    print("1->For insert new contact")
    print("2->For Display contact")
    print("3->For Delete Contact")
    print("4->For Update")
    op=int(input("Enter Your Option"))
    return op
def get_contact():
    return contact
def set_contact(list_data):
    global contact
    if(list_data):
        contact=list_data