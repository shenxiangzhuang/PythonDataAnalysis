#!/usr/bin/env/python3

import sys
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


# 使用numpy计算
def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c


# 使用python计算
def pythonsum(n):
    # 这里由于源码为Python2的，python3中range的用法有变,不再直接返回列表
    # 所以强制转化列表
    a = list(range(n))
    b = list(range(n))
    c = []

    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])

    return c


# prt表示是否打印结果
def printest(func, size, prt=True):
    start = datetime.now()
    c = func(size)
    delta = datetime.now() - start
    if prt == True:
        print("The last 2 elements of the sum ", c[-2:])
        print('Elapsed time in microsecondas ', delta.microseconds)
    return delta.microseconds


# 用于作n-time图
def timeplot():
    pts = []
    for i in range(100, 10000, 100):
        t_numpy = printest(numpysum, i, prt=False)
        t_python = printest(pythonsum, i, prt=False)
        pts.append([t_numpy, t_python])
    plt.plot(pts)
    plt.legend(['Numpy', 'Python'])
    plt.show()


if __name__ == '__main__':
    #size = int(sys.argv[1])
    size = 1000
    print('Numpysum...')
    printest(numpysum, size)
    print('Pythonsum...')
    printest(pythonsum, size)
    timeplot()
