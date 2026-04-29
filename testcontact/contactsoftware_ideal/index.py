from helper import *
from fileop import *
y=0
list_data=read_contact()
set_contact(list_data)
while y==0:
    opt=menu()
    if(opt==1):
       create_contact() 
    if(opt==2):
       display_contact() 
    if(opt==3):
       delete_contact() 
    if(opt==4):
       update_contact() 
    
    y=int(input("Do you want to continue?Press 0 for yes"))
    if(y!=0):
       data=get_contact()
       write_contact(data) 

