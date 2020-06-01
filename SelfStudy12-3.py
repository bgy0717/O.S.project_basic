import threading


def sum1():
    n = 0
    for i in range(1, 1001):
        n += i
    print(n)


def sum2():
    n = 0
    for i in range(1, 100001):
        n += i
    print(n)


def sum3():
    n = 0
    for i in range(1, 10000001):
        n += i
    print(n)


th1 = threading.Thread(target=sum1())
th2 = threading.Thread(target=sum2())
th3 = threading.Thread(target=sum3())

th1.start()
th2.start()
th3.start()
