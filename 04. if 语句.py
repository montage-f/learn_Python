# Created by MonTage_fz at 2019/7/11
x = int(input('Please enter an integer:'))

if x < 0:
    x = 0
    print('Negative changed to zero:', x)
elif x == 0:
    print('Zero:', x)
elif x == 1:
    print('Single:', x)
else:
    print('More:', x)
