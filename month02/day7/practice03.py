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
def precess_1():
    prime = []
    for i in range(1,1000001):
        if is_prime(i):
            prime.append(i)
    print(sum(prime))
begin = time.time()
precess_1()
print("花费时间：",time.time() - begin)
