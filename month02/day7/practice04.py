from multiprocessing import Process,Queue
import re
import time

from multiprocessing import Manager
class TestProcess(Process):
    def __init__(self,begin,end,q):
        super().__init__()
        self.begin = begin
        self.end = end
        self.q = q
    def run(self):
        data_list1 = []
        # data_list2 = []
        for i in range(self.begin,self.end):
            print(i)
            data_list1.append(i+1)
            # data_list2.append(i+2)
            time.sleep(0.5)
        self.q.put(data_list1)
        # self.q.put(data_list2)

if __name__ == "__main__":
    q = Queue()
    process_list = []
    for i in range(1,20,2):
        proc = TestProcess(begin=i,end=i+2,q=q)
        process_list.append(proc)
        proc.start()
    print(f"共有几个进程》》{len(process_list)}")
    for item in process_list:
        item.join()
    print(f"共有几个进程》》{len(process_list)}")
    result = [q.get() for j in process_list]
    faile_list = re.findall('[0-9]+',str(result))
    # for item in result:
    #     for i in item:
    #         list1.append(i)
    print(faile_list)

