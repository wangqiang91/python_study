def n01_find_number():
    for i in range(2000,3201):
        if i % 7 == 0 and i % 5 != 0:
            print(i,end=",")

def n02_factorial():
    num = int(input())
    fac = 1
    for i in range(1,num+1):
        fac = fac * i
    print(fac)


if __name__ == "__main__":
    n02_factorial()
