'''
https://uqer.io/community/share/55c9a55df9f06c91f818c675
'''

# from cvxopt import solvers, matrix
# import numpy as np
#
# P = matrix(np.diag([1.0, 0]))  # 对于一些特殊矩阵，用numpy创建会方便很多（在本例中可能感受不大）
# q = matrix(np.array([3.0, 4]))
# G = matrix(np.array([[-1.0, 0], [0, -1], [-1, -3], [2, 5], [3, 4]]))
# h = matrix(np.array([0.0, 0, -15, 100, 80]))
# sol = solvers.qp(P, q, G, h)
# print(sol['x'])

import numpy as np
from cvxopt import solvers, matrix

P = matrix([[1.0, 0.0], [0.0, 0.0]])
q = matrix([3.0, 4.0])
G = matrix([[-1.0, 0.0, -1.0, 2.0, 3.0], [0.0, -1.0, -3.0, 5.0, 4.0]])
h = matrix([0.0, 0.0, -15.0, 100.0, 80.0])
sol = solvers.qp(P, q, G, h)
print(sol['x'])
