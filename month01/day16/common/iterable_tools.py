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
        for iter in range(len(iterable)):
            if condition(iter):
                del iterable[iter]
                return "删除成功"