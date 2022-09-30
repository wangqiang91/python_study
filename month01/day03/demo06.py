"""
    字符串   
    转义字符\：改变原始含义的特殊字符

"""
#占位符  %s  %f  %d
a = 100
b = 200.235
#%.nd 当数值不足n位时，高位用0填充； %.nf四舍五入保留n位小数，不足后面补0；
print("测试输入%.3d，输出%.4f" %(a,b))
c = 30
#如果在字符串中显示%，需要写两个%
print("治愈比例为%s%%" %c)

city = "湖北"
num1 = 67802
num2 = 63326
rate = num2/num1
print("%s确诊%s人，治愈%s人，治愈率%.2f" %(city,num1,num2,rate))


seconds = 70
print("%s秒是%.2d分%.2d秒" %(seconds,seconds//60,seconds%60))

print("{}秒是{}分{}秒" .format(seconds,seconds//60,seconds%60))