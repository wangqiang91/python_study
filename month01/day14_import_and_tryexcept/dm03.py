"""
    异常处理  
"""
def dev_apple(apple_count):
    try:
        person_count = int(input("请输入人数："))
        result = apple_count / person_count
        print(result)
    except ValueError:
        print("人数输入错误")
    except ZeroDivisionError:
        print("请输入非0整数")
    except Exception:
        print("其他错误")
    else:
        print("分苹果结束拉")
    finally:
        print("最后一定要执行的")
dev_apple(10)

# 方法1
def dev_apple(apple_count):
    try:
        person_count = int(input("请输入人数："))
        result = apple_count / person_count
        print(result)
    except:
        print("人数输入错误")

# dev_apple(10)


# 方法2
def dev_apple(apple_count):
    try:
        person_count = int(input("请输入人数："))
        result = apple_count / person_count
        print(result)
    except ValueError:
        print("人数输入错误")
    except ZeroDivisionError:
        print("请输入非0整数")
    else:
        print("分苹果结束了")
    
# dev_apple(10)

# 方法3
def dev_apple(apple_count):
    try:
        person_count = int(input("请输入人数："))
        result = apple_count / person_count
        print(result)
    finally:
        print("分苹果结束了")

