def write_contact(data):
    fp=open("contact.txt","w")
    for item in data:
        contact_data=item[0]+"#"+item[1]+"#"+item[2]+"\n"
        fp.write(contact_data)
    fp.close()
def read_contact():
    result_data=[]
    with open("contact.txt","r") as file:#For opening the file
        for line in file: #To read the file line by line
             t=line.split("#") #We split the line based on #
             result_data.append((t[0],t[1],t[2]))#we create a list
    return result_data

