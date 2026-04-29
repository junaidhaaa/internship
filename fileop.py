name=input("enter your name")
email=input("enter email")
mobile=input("enter mobile")
data=name+" "+email+" "+mobile

fp=open("data.txt","a")
fp.write("data")
fp.close()
