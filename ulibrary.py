from itertools import permutations
import  datetime
p=[1,2,3,4,5,6,7,8,9]
before=datetime.datetime.now()
s=permutations(p) #存储器，全排列，穷举存储
for s1 in s:
    a1=''.join(str(i) for i in s1[:4] )
    b1=s1[4]
    c1=''.join(str(i) for i in s1[5:])
    if int(a1)*int(b1) == int (c1):
        print(a1,b1,c1)
end=datetime.datetime.now()
print((end-before).total_seconds())
print("------------------------")
import random
for i in range(5):
    j=random.randint(0,i)
    print(j)