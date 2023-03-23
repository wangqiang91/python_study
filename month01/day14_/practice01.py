import time
def calculate_week(year,month,day):
    date= time.strptime(str(year)+"年"+str(month)+"月"+str(day)+"日","%Y年%m月%d日")
    week_dict = {0:"一",1:"二",2:"三",3:"四",4:"五",5:"六",6:"日",}
    print(f"星期{week_dict[date[6]]}") 

calculate_week(2023,3,22)