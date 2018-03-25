# # 无等式约束
import numpy as np
from cvxopt import matrix, solvers

c = matrix([-4., -5.])
G = matrix([[2., 1., -1., 0.], [1., 2., 0., -1.]])
h = matrix([3., 3., 0., 0.])
sol = solvers.lp(c, G, h)
print(sol['x'])


# 有等式约束
G = matrix([[1.0, 4.0, -2.0, -1.0, 0.0, 0.0], [-2.0, -1.0, 0.0, 0.0, -1.0, 0.0], [1.0, -2.0, 1.0, 0.0, 0.0, -1.0]])
h = matrix([11.0, -3.0, 1.0, 0.0, 0.0, 0.0])
A = matrix([-2.0, 0.0, 1.0])
A = A.trans()  # 这里不转置会报错
b = matrix([1.0])
c = matrix([-3.0, 1.0, 1.0])
sol = solvers.lp(c, G, h, A=A, b=b)
print(sol['x'])
