import time
def calculate_week(year,month,day):
    date= time.strptime(str(year)+"年"+str(month)+"月"+str(day)+"日","%Y年%m月%d日")
    week_dict = {0:"一",1:"二",2:"三",3:"四",4:"五",5:"六",6:"日",}
    print(f"星期{week_dict[date[6]]}") 

# calculate_week(2023,3,22)


def get_score():
    try:
        score = int(input("请输入成绩："))
        return score
    except:
        print("请输入正整数")
        return False

# while True:
#     score = get_score()
#     if score > 0:
#         print(f"成绩是{score}")
#         break
#     else:
#         print("输入错误，请重新输入！")


def get_score_2():
    while True:
        try:
            score = int(input("请输入成绩："))
            return score
        except:
            print("请输入正整数")
            

print(get_score_2())