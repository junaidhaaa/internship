FILE = "students.txt"

def add():
    f = open(FILE, "a")
    f.write(input("ID: ") + "," + input("Name: ") + "," +
            input("M1: ") + "," + input("M2: ") + "," + input("M3: ") + "\n")
    f.close()

def view():
    try:
        for i in open(FILE):
            print(i.strip())
    except:
        print("No file")

def search():
    s = input("ID: ")
    for i in open(FILE):
        if i.split(",")[0] == s:
            print(i.strip())

def delete():
    s = input("ID: ")
    data = []
    for i in open(FILE):
        if i.split(",")[0] != s:
            data.append(i)
    open(FILE, "w").writelines(data)

while True:
    ch = input("\n1.Add 2.View 3.Search 4.Delete 5.Exit: ")
    if ch == "1": add()
    elif ch == "2": view()
    elif ch == "3": search()
    elif ch == "4": delete()
    elif ch == "5": break