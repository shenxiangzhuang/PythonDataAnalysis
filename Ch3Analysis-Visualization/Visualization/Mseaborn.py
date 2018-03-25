import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 核密度估计

x = np.random.normal(0, 1, 100)
y = np.random.normal(1, 2, 100)

sns.kdeplot(x)
sns.kdeplot(y)
plt.show()

# 频数图
tips = sns.load_dataset("tips")
plt.subplot(121)
sns.countplot('day', data=tips)
plt.subplot(122)
sns.countplot('sex', data=tips)
plt.show()

# 线性回归
sns.lmplot(x='total_bill', y='tip', hue='day', data=tips, fit_reg=True)
plt.show()

# 小提琴图
sns.violinplot(x='day', y='tip', data=tips)
plt.show()

# 多因素分析
sns.factorplot('day', 'total_bill', 'sex', data=tips, kind='violin')
plt.show()
