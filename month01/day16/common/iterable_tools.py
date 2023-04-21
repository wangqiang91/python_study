class IterableHelper:
    @staticmethod
    def find_single(iterable,condition):
        for item in iterable:
            if condition(item):
                return item 
    @staticmethod
    def find_all(iterable,condition):
        for item in iterable:
            if condition(item):
                yield item
    @staticmethod
    def sum(iterable,condition):
        sum_data = 0
        for item in iterable:
            sum_data += condition(item)
        return sum_data
    @staticmethod
    def get_count(iterable,condition):
        count_data = 0
        for item in iterable:
            if condition(item):
                count_data += 1
        return count_data
    @staticmethod
    def delete_single(iterable,condition):
        """
            在可迭代对象中删除满足条件的第一个元素；
        param iterable:可迭代对象；
        param condition:条件；
        return:是否删除成功；
        """
        for iter in range(len(iterable)):
            if condition(iterable[iter]):
                del iterable[iter]
                return "删除成功"
        return "删除失败，未找到符合条件的数据"

    @staticmethod
    def delete_all(iterable,condition):
        """
            在可迭代对象中删除满足条件的所有元素：
        :param iterable:可迭代对象；
        :param condition:条件
        :return 返回删除的元素个数；
        """
        sum = 0
        for i in range(len(iterable)-1,-1,-1):
            if condition(iterable[i]):
                del iterable[i]
                sum += 1
        return f"共删除了{sum}条数据"
    
    @staticmethod
    def select(iterable,condition):
        """
            根据传入的条件对可迭代对象中的每个元素进行选择
        """
        for item in iterable:
            yield condition(item)

    @staticmethod
    def asc_employee(iterable,condition):
        """
            根据传入的条件对可迭代对象从小到大排序
        :param iterable:可迭代对象
        :param condition:传入的条件
        """
        for i in range(len(iterable)-1):
            for j in range(i+1,len(iterable)):
                if condition(iterable[i]) > condition(iterable[j]):
                    iterable[i],iterable[j] = iterable[j],iterable[i]
    
    @staticmethod
    def is_repeat(iterable,condition):
        """
            根据传入的条件判断是否有相同的数据
        :param iterable:可迭代对象
        :param conditon:条件
        :return 布尔值
        """
        for i in range(len(iterable)-1):
            for j in range(i+1,len(iterable)):
                if condition(iterable[i]) == condition(iterable[j]):
                    return "True"
        return "false" 