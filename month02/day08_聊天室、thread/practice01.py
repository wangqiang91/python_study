from threading import Thread
from time import sleep,time

list_ticket = ["T%d"%x for x in range(1,501)]     
def sell(w):
        while list_ticket:
            print(w,"------",list_ticket.pop(0))
            sleep(0.1)  
jobs = []
start = time()
for i in range(1,10):
    t = Thread(target=sell,args=(i,))
    jobs.append(t)
    t.start()
for i in jobs:
    i.join()
end = time()
print("票已售罄")
print(end-start)

