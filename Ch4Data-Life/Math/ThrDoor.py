import random as rnd


# 计算在第二次采取不同策略时,是否在游戏中获胜[选中汽车]
def game(strategy):
    win = 0
    # 假定汽车在0号门（参赛者并不了解这一事实）
    doors = [0, 1, 2]
    # 因为事先我们并不知道任何信息,所以第一次随机选取一扇门
    first_choice = rnd.choice(doors)
    # 根据第一次的选择情况的不同，第二次决策面临两种不同的备选组合

    # 如果第一次选择了0号门，那么在主持人打开另外两个门中的其中一个门后
    # 第二次将要在0号门和未打开的空门（1 or 2）中作出选择
    if first_choice == 0:
        doors = [0, rnd.choice([1, 2])]

    # 如果第一次没有选中0，那么此时被打开的必然是另一个有山羊的门，那么
    # 在第二次选择时，将在0和自己现在所处的门（first_choice）作出选择
    else:
        doors = [0, first_choice]

    # 采取不同的策略进行第二次选择

    # 保持原来位置不变
    if strategy == 'stick':
        second_choice = first_choice

    # 排除一扇空门后，放弃原来的选择，直接选择另一扇门
    else:
        doors.remove(first_choice)
        second_choice = doors[0]

    # 记得，奖品在0号门
    if second_choice == 0:
        win = 1

    return win


# 对特定策略进行的一定次数的模拟
def MC(strategy, times):
    wins = 0
    for i in range(times):
        wins += game(strategy)
    # 计算获奖的概率值
    p = wins / times
    print('第二次选择采用' + strategy + '方法，获奖的概率为：' + str(p) + '(模拟次数为' + str(times) + ')')


if __name__ == '__main__':
    MC('stick', 10000)
    MC('switch', 10000)
