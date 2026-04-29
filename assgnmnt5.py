from datetime import datetime

d1 = input("Enter first date (DD-MM-YYYY): ")
d2 = input("Enter second date (DD-MM-YYYY): ")

date1 = datetime.strptime(d1, "%d-%m-%Y")  #convert string to date
date2 = datetime.strptime(d2, "%d-%m-%Y")

diff = date2 - date1

print("Number of days:", diff.days)