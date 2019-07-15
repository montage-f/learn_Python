# Created by MonTage_fz at 2019/7/12
# 返回多个值, 返回的类型是元组Tuple


def damage(skill1, skill2):
    damage1 = skill1*3
    damage2 = skill2*2+10
    return damage1, damage2

# 通过变量, 将函数里面返回的值, 进行解刨
skill1_damage1, skill2_damage2 = damage(100, 200)
print(skill1_damage1)
print(skill2_damage2)
