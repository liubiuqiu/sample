#单引号（'）、双引号（"）、三单引号（'''）、三双引号（"""）
#1).（单引号、双引号）表示多行时需要添加换行符\n。
#2).（三单引号、三双引号）表示多行时无需使用任何多余字符
#3).（三单引号、三双引号）中可直接使用（单引号、双引号）而无需使用反斜杠\进行转义
import os
c='''a
b
c'''
d="1" \
  "2"  #此处"\"为转义字符
#多行数据
print(c)
#去掉换行符'\n'
print(c.split("\n"))
#分离文件名与路径
print(os.path.split('/dodo/soft/python'))
print(os.path.split('/dodo/soft/python/'))
print(os.path.split('/dodo/soft/python/')[0])
#u = input("请输入数据开始练习>>>") #人为键盘输入数据
u="www.baidu.com.gov."
print(u.strip('m'))  #去除首尾空格 换行符'\n'及首尾chars之内字符，直到第一个不在chars内的字符
#使用默认分隔符
print(u.split())
#以"."为分隔符，返回列表（list）
print(u.split('.'))
s=u.split('.')
print(len(s))  #返回列表长度
print(s[0].isdigit(),s[0].isalpha())  #字符判断函数返回布尔型 True / False
s1=('|'.join(s))  #重新以'｜'拼接列表（list）数据为字符串（str）
print("原始数据为：%s 拼接数据为：%s"%(s,s1)) # %s字符串、%d 十进制整数、%f 浮点数、%%输入%
#分割2次
print(u.split('.',2))
#分割最多次（实际与不加num参数相同）
print(u.split('.',-1))
#分割两次，并把分割后的三个部分保存到三个字符串文件
u1,u2,u3=u.split('.',2)
print(u2)