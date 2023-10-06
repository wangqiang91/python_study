fr = open("month02\day03\demo11.txt","w",encoding="utf-8")
# 方法1：write
fr.write("嘿嘿哈哈或\n")
fr.write("lalalala\n")

# 方法2：writelines(str_list)
fr.writelines(["飞流直下三千尺\n","疑似银行落九天\n"])
fr.close()

# 以追加方式打开写入，不清空原有内容
fr1 = open("month02\day03\demo11.txt","a",encoding="utf-8")
fr1.write("追加呀")
fr1.close()

# with
with open("month02\day03\demo11.txt","r",encoding="utf-8") as fr2:
    data = fr2.read()
    print(data)

"""buffering:默认值为-1，即使用电脑自定义缓存；若为1，
遇到\n刷新缓存； 若大于1为N时，则写入N个字符就刷新缓存写入，
大于1时必须以二进制方式打开文件；"""
fr3 = open("month02\day03\demo11.txt","ab",buffering=8)
while True:
    data = input(">>")
    if not data :
        break
    fr3.write(data.encode())
    # fr3.write(data+"\n")
    # fr3.flush() #刷新缓存，立即写入
fr3.close()