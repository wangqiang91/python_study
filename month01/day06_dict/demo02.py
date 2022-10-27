'''
    练习
'''

dict_course = {
    "1":"pyton语言核心编程",
    "2":"python高级",
    "3":"web全栈",
    "4":"项目实战",
    "5":"数据分析、分工智能"
}
number = input("请输入数字：")
if number in dict_course.keys():
    print(dict_course[number])
else:
    print("阶段错误！")