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
print(find_line("one1"))


