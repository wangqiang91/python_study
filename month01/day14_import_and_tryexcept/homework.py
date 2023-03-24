import time
def calculate_days(year,mouth,day):
    now_time = time.time()
    # print(f"当前时间:{now_time}")
    birthday_strtime = "%d-%d-%d"%(year,mouth,day)
    birthday_tupletime = time.strptime(birthday_strtime,"%Y-%m-%d")
    # print(f"生日的时间元祖{birthday_tupletime}")
    birthday_time = time.mktime(birthday_tupletime)
    # print(f"生日的时间戳{birthday_time}")
    live_days = (now_time - birthday_time) / 3600 // 24
    print(live_days)

calculate_days(1992,11,11)