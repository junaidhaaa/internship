import random
num=int(input("Guess a number between 1 and 20"))
generated_num=random.randint(1,20)
#print(generaed_num)
c=True
while c:
    if (num==generated_num):
        print("You succesfully predicted")
        break;
    if(num<generated_num):
        print("You are predicted too low ")
    if(num>generated_num):
        print("You are predicted too high")
    num=int(input("Guess a number between 1 and 20"))
