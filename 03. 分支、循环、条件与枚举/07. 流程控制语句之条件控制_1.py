# Created by MonTage_fz at 2019/7/12

mood = True
# if 后面可以是一个表达式,:
if mood:
    print('go to left')
else:
    print('go to right')


a = 1
b = 2

if a > b:
    print('a', a)
else:
    print('b', b)


account = 'fan_zheng'
password = 123456

print('please input account')
user_account = input()

print('please input password')
user_password = input()

if user_account == account and user_password == password:
    print('success')
else:
    print('fail')

