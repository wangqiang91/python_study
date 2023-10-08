def find_line(data):
    file_open = open("month02/day03/dict.txt","r")
    for line in file_open:
        list_line = line.split(" ")
        if list_line[0] > data:
            file_open.close()
            break
        if data == list_line[0]:
            file_open.close()
            return line
    return "not find"
print(find_line("home"))

lujin = r'C:\Users\Administrator\Downloads\\'
def copy_file(filename):
    fr1 = open(lujin+filename,"rb")
    fr2 = open(r"month02\day03\\"+filename,"wb")
    while True:
        data = fr1.read(2048)
        if not data:
            break
        fr2.write(data)
    fr1.close()
    fr2.close()
# copy_file("th.jpg")


import time
def write_time_tolog():
    fr = open("month02\day03\my.log","a",encoding="utf-8",buffering=1)
    fr.seek(0)
    num = len(fr.readlines()) + 1
    while True:  
        fr.write("%d. %s\n"%(num,time.ctime()))
        # fr.flush()   #用buffering = 1代替；
        num = num + 1
        time.sleep(3)
# write_time_tolog()

import os
file_dir = "month02\day03\homework_data"
def union():
    fr_union = open(r"month02\day03\union.txt","w",encoding="utf-8")
    file_list = os.listdir(file_dir)
    for item in file_list:
        fr = open(file_dir + "\\" + item,"r",encoding="utf-8")
        for line in fr:
            fr_union.write(line)
        fr_union.write("\n")
        fr.close()
    fr_union.close()
# union()