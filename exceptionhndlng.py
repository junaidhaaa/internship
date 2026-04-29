import datetime 
today=datetime.datetime.now()
from logging import*
try :
    print("Line 1")
    print("Line 2")
    print("Line 3")
    raise Exception("we created a problem in our code")
    print("Line 4")
    print("Line 5")
    print("Line 6")
except Exception as e:
    #print("There is an exception occured")
    ##fp=open("log.txt","a")
    data="Module Login"+"#"+"Exception HandleFile"+"#"+str(today)+"#"+str(e)
    #fp.write(data)
    #fp.close()
    write_log(data)