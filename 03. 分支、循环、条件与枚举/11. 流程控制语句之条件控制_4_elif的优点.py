# # Created by MonTage_fz at 2019/7/12
# a = x

# a = 1
# print('apple')
# a = 2
# print('orange')
# a = 3
# print('banana')

# 在终端输入的数字, 其实反映出来的是字符串

a = int(input())

print('a is',a,type(a))
if a==1:
    print('apple')
else:
    if a==2:
        print('orange')
    else:
        if a==3:
            print('banana')
        else:
            print('shopping')





b = input()
print('b is', b)
if b==1:
    print('apple')
elif b==2:
    print('orange')
elif b==3:
    print('banana')
else:
    print('shopping')
