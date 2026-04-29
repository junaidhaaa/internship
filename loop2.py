lmt = int(input("Enter a limit"))
x = 0

while x < lmt:
    x += 1
    if x % 2 == 0:
        continue   
    print(x)
    