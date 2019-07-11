# Created by MonTage_fz at 2019/7/11
# 循环语句可能带有一个 else 子句；
# 它会在循环遍历完列表 (使用 for) 或是在条件变为假 (使用 while) 的时候被执行，但是不会在循环被 break 语句终止时被执行。
# 这可以通过以下搜索素数的循环为例来进行说明:
# 仔细看： else 子句属于 for 循环， 不属于 if 语句。
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        print(n, 'is a prime number')
