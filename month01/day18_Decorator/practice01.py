import time
def sum_data_run_time(fun):
    def wrapper(*args,**kargs):
        start_time = time.time()
        res = fun(*args,**kargs)
        end_time = time.time()
        print(f"执行了{end_time-start_time}秒")
        return res
    return wrapper
    
@sum_data_run_time
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value
print(sum_data(10))
print(sum_data(1000000))