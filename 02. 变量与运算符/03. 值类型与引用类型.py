# Created by MonTage_fz at 2019/7/12

# int str tuple(不可改变) boolean  是值类型
# list set dict(可变)  是引用类型

a = [1, 2, 3, 4, 5]
b = a

print(a)
print(b)

a[1] = '我被改变了'

print(a)
print(b)

a = 'hello'
a += ' world'
print(a)

# id() 显示变量指向的地址
id(a)
