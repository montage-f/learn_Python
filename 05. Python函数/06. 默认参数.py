# Created by MonTage_fz at 2019/7/12


# 默认参数
def add(x, y=100):
    return x+y


result = add(1)
print(result)


def agree_info(name, age=18, info='你们', school='中山大学'):
    print('my name is ', name, "I'm", age, 'I thank', info, "I'm in", school)


# 如果我想直接填入info, 那我们就可以使用关键字参数,来避开参数没对应上的问题
agree_info('樊铮',)
agree_info('樊铮', school='广州大学')
