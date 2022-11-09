'''
    练习
'''

def calculate_cure_rate(confirmed, cure):
    """
        计算治愈比例
        :param confirmed int类型 确诊人数
        :param cure int类型 治愈人数
        :return return float类型 治愈比例
    """
    cure_rate = cure / confirmed * 100
    return cure_rate
print(calculate_cure_rate(100,34))

def calculate_jin_and_liang(total):
    jin = total // 16
    liang = total % 16
    return (jin,liang)  #小括号可以省略，返回的数据扔是一个元祖；
print(calculate_jin_and_liang(100))
jin,liang = calculate_jin_and_liang(100)
print(jin)
print(liang)


def get_class_name(num):
    """
        根据课程阶段获取课程名称
        :parem num 1-5,课程阶段
        :return 课程名称
    """
    dict_class_name = {1:"python语言核心",2:"python高级软件",3:"web全栈",4:"项目实战",5:"数据分析"}
    if num in dict_class_name.keys():
        return dict_class_name[num]
print(get_class_name(2))


def calculate_iq_name(ma,ca): #由于return执行后，后面的代码不再执行，所以可以把elif换成if；
    iq = ma / ca * 100
    if iq >= 140: return "天才"
    if iq >= 120: return "超常"
    if iq >= 100: return "聪慧"
    if iq >= 90: return "正常"
    if iq >= 80: return "迟钝"
    return "低能"
print(calculate_iq_name(25,22))
