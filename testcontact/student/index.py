from helper import*
y=0
while y==0:
    opt=menu()
    if(opt==1):
        create_student()
    elif(opt==2):
        view_student()
        
    elif(opt==3):
        search_student()
    elif(opt==4):
        delete_student()
    elif(opt==5):
        print("existing...")
        break
    y=int(input("do you want to continue? press 0 for yes:"))