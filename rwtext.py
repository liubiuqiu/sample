print("-----------0分割线-------------")
import os
path=os.getcwd()  #获取当前路径
print(path)
a_path=os.path.join(path+"/Data/text")
print(a_path)
print("-----------1分割线-------------")
f = open(a_path,"r") #通过path函数值获取路径
lines =f.readlines()
print(lines)
f.close()
f = open("/Users/liubaiquan/Desktop/sample/Data/text","r") #绝对路径
lines =f.readlines()
f.close()
print(lines)
f = open("Data/text","r") #相对路径
lines =f.readlines()
print(lines)
print(len(lines))
f.close()
print("-----------2分割线-------------")
for line in lines:
    a=line.strip()  #去掉换行符'\n'
    print(a)
b=[] #位置决定输出的blist格式
for line in lines:
    i=0
    #b=[]
    if i< len(lines):
        b.append(line.strip())
        i=i+1
    else:
        break
print(b)
print("-----------3分割线-------------")
with open("Data/text","r") as f:
    for line in f:
        t = line.strip().split('|')
        print(t)
f_name='banana'
f_price=8
f_adress='china'
#a追加写，w覆盖写
with open('Data/text','a') as f:
    f.write('|'.join([f_name, str(f_adress), str(f_price)]) + '\n')
print("-----------4分割线list-------------")
def getgoods():
    with open('Data/dtext') as f:
        goods =[]
        for line in f:
            goods.append(line.strip().split('|')[0])
    return goods
print(getgoods())
print("-----------5分割线dict-------------")
#获取商品信息及价格  字典
import os
def getgoods():
    with open('Data/dtext') as f:
        goods = {}
        for line in f:
            t = line.strip().split('|')
            goods[t[0]] = t[1]
    return goods
print(getgoods())

def postgooda(f_name,f_price):
    goods=getgoods()
    if goods.get(f_name):
        pass
    else:
        with open('Data/dtext','a') as f:
            f.write('|'.join([f_name,str(f_price)])+ '\n')

postgooda("banna",6.7)

def putgoods(f_name,f_price):
    goods=getgoods()
    if goods.get(f_name):
        goods[f_name]=str(f_price)
    else:
        pass
    with open('Data/dtext1','a') as f:
        for k,v in goods.items():
            f.write('|'.join([k,v]) +'\n')
    os.remove('Data/dtext')
    os.rename('Data/dtext1','Data/dtext')
putgoods('apple',100)
