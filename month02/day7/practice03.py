"""
    求10万以内的质数之和
"""
from multiprocessing import Process
import time
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True
def precess_1(begin,end):
    prime = []
    for i in range(begin,end):
        if is_prime(i):
            prime.append(i)
    print(sum(prime))
def main():
    begin = time.time()
    list_pro = []
    for item in range(1,100001,25000):
        p = Process(target=precess_1,kwargs={"begin":item,"end":item+25000})
        list_pro.append(p)
        p.start()
    for item in list_pro:
        item.join()
    print("花费时间：",time.time() - begin)
if __name__ == "__main__":
    main()
