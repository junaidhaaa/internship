from helper import *
y=0
while y==0:
    opt=menu()
    if(opt==1):
       create_account() 
    if(opt==2):
       display_account() 
    if(opt==3):
       delete_account() 
    if(opt==4):
       update_account() 
    y=int(input("Do you want to continue?Press 0 for yes"))