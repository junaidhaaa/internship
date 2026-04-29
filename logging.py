def write_log(data):
    fp=open("log_data.txt","a")
    fp.write(data)
    fp.close()