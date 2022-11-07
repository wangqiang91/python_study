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
    return dict_class_name[num]
print(get_class_name(3))
