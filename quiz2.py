p="www.145.发个.WE34."
p1=p.split(".")
print(p1)
p1[0]="http"  #修改列表一个元素
print(p1)
p1.append("com")  #列表末尾添加新元素
print(p1)
p1.insert(1,'abc')  #在索引1处添加新元素，既有元素右移一个位置
print(p1)
del p1[3]  #删除索引3位置处的列表元素
print(p1)
p2=p1.pop()  #删除末尾数据并赋值p2使用，可在pop(2)加索引删除
print(p1)
print(p2)
p1.remove("145")  #根据"值"所在位置删除元素
print(p1)
print(sorted(p1))  #对列表临时排序
print(p1)
p1.sort()  #对列表永久性排序
print(p1)
p1.reverse()  #倒着元素顺序打印数据
print(p1)
print(len(p1))
#元组（tuple）本身是不可变数据类型，没有增删改查,但可以存储任意数据类型
#元祖变量值交换
a = 1
b = 2
a,b=b,a
print(a)
print(b)
print(a,b)
#元祖打印变量
name = "lily"
age = 14
t = (name,age)
print("%s的年龄：%d"%t)
print("%s的年龄：%d"%(name,age))
#元祖的赋值
t=("bob","25")
name,age=t
print(name)
print(age)
#1字典元素追加
dict = {"name":"小黄","age":12}
dict["sex"]="male"  #直接添加
print(dict)
dict.setdefault("color","red")  #setdefault方法添加
print(dict)
dict.setdefault("name","小红")  #setdefault方法添加,不重复添加key重复数据
print(dict)
dict1 = {"name":"小明"}
dict.update(dict1)  #把字典dict1的键/值对更新到dict里,如果dict和dict1如果有相同的键，那么对应的值，会以更新的为准.即dict1
print(dict)
#2判断key键但存在
print("name" not in dict)
#3字典中的查找：items() keys() values()得到的返回值并不是list，需要转换形如：list(dict.key)
print(dict.keys())  #查找有哪些键
print(list(dict.keys()))
print(dict.values())  #查找有哪些值
print(list(dict.values()))
print(dict.items()) #查询所有键值
print(list(dict.items()))
#4删除字典name元素
del dict["name"]
print(dict)
dict.clear()  #清空字典，输出None
print(dict)
#5字典可以多层嵌套
cc = {'ct':{'sex':'male'},'wj':{'sex':'female'}}
print(cc)
print(cc['ct'])
print(cc['ct']['sex'])
#6字典的遍历
dict2 = {'name': '小二', 'age': 12, 'sex': 'male', 'color': 'red'}
for i in dict2:
    print(i)  #key
    print(i,dict2[i])  #key,value
for i,v in dict2.items():
    print(i,v)  #key,value
#7同一个键可以出现两次。创建时如果同一个键被赋值两次，后一个值会被记住;
# 键必须不可变，可以用数，字符串或元组(元祖不可变)充当,用列表不行
dict3 = {'name':'tom','age':34,'name':'bob'}
print("dict3['name']:",dict3['name'])