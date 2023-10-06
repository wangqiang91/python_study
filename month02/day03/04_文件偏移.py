# seek:seek(M,N)：N为0时，定位在开头，为1时，为2时定位在结尾，
# 且只能是二进制打开时用1,2；M为正时向前移动M字符，
# 为负时向后移动M字符，如fr.seek(-4,2);

fr1 = open("month02\day03\demo11.txt","wb+")
fr1.write(b"hello world")
fr1.seek(-5,2)
data = fr1.read()
fr1.flush()
print(data)
print(fr1.tell())