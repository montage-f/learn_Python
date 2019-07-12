# Created by MonTage_fz at 2019/7/12

# tuple 与 list 的区别

a = [1, 2, 3]
id(a)

a[0] = '1'
id(a)

a.append(4)

b = (1, 2, 3, [4, 5, 6])
b[3][1] = 999
print(b[3][1])
