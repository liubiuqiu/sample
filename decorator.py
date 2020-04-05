import  datetime
import time
from itertools import permutations
def fun(fun):
    before=datetime.datetime.now()
    time.sleep(1)
    fun()
    end=datetime.datetime.now()
    print((end-before).total_seconds())

@fun
def new():
    print('原函数')
new

def timecount(fun):
    before = datetime.datetime.now()
    fun()
    end = datetime.datetime.now()
    print((end-before).total_seconds())
print('------------------')
@timecount#装饰器，一个装饰器只能跟一个函数，但是可以多个装饰器
def numsort():
    p = [1,2,3,4,5,6,7,8,9]
    s = permutations(p)
    for s1 in s:
        a1 = "".join([str(i) for i in s1[:4]])
        b1 = str(s1[4])
        c1 = "".join([str(i) for i in s1[5:]])
        if int(a1) * int(b1) == int(c1):
            print(a1,b1,c1)

numsort
