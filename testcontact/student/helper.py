student = []

def create_student():
    sid = input("enter student id: ")
    name = input("enter student name: ")
    mark1 = float(input("enter mark1: "))
    mark2 = float(input("enter mark2: "))
    mark3 = float(input("enter mark3: "))
    student.append((sid, name, mark1, mark2, mark3))


def view_student():
    print(student)


def search_student():
    sid = input("enter id to search: ")
    found = False

    for s in student:
        if s[0] == sid:
            found = True
            print("student details")
            print("sid:", s[0])
            print("name:", s[1])
            print("mark1:", s[2])
            print("mark2:", s[3])
            print("mark3:", s[4])
            calculate_grade(s)

    if not found:
        print("student does not exist")


def calculate_grade(s):
    total = s[2] + s[3] + s[4]
    avg = total / 3

    if avg >= 85:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "FAIL"

    print("total:", total, "average:", avg, "grade:", grade)


def delete_student():
    i = int(input("enter index to delete: "))
    if i < len(student):
        student.pop(i)
        print("deleted successfully")
    else:
        print("invalid index")


def menu():
    print("\nmenu")
    print("1.create student")
    print("2.view student")
    print("3.search student")
    print("4.delete student")
    print("5.exit")
    op = int(input("enter your option: "))
    return op