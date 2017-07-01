import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 调入数据
iris = load_iris()

# sklearn对数据集的介绍
print(iris.DESCR)

# 提取数据集内容
# 这里根据需要可以不进行另外的赋值
iris_data = iris.data
feature_names = iris.feature_names
iris_target = iris.target

# 格式整理
iris_target.shape = (150, 1)
iris_all = np.hstack((iris_data, iris_target))
# 转化为DataFrame
iris_data_df = DataFrame(iris_data, columns=feature_names)
iris_target_df = DataFrame(iris_target, columns=['target'])
iris_data_all_df = DataFrame(iris_all, columns=feature_names + ['target'])

'''
数据集基础信息的获取[以iris_data_df为例]
'''

# 数据预览
print(iris_data_all_df.head())  # 默认为前5行
print(iris_data_all_df.tail())  # 默认为后5行
print(iris_data_all_df.sample(5))  # 随机抽取5行

# 数据描述
'''
这里是处理好的数据集，所以数据格式比较完整，不用进一步的处理。
如有数据乱码或者出现缺失值等情况，我们当按照上一篇的方法进行适当的数据清洗。
'''

# print(iris_data_all_df.isnull().sum())  # 缺失值
print(iris_data_all_df.shape)  # 大小
print(iris_data_all_df.dtypes)  # 类型
print(iris_data_all_df.describe())  # 常见统计量的描述
print(iris_data_all_df.info())  # 多种信息

'''
可视化的方法，来直观了解数据
'''

# 数据范围
sns.boxplot(data=iris_data_df)
plt.show()

# 总览
plt.plot(iris_data_df)
plt.legend(feature_names)
plt.show()

# 为了便于观察，也可以作出部分数据的图
# sepal
sepal_data_df = iris_data_df[['sepal length (cm)', 'sepal width (cm)']]
plt.plot(sepal_data_df)
plt.legend(['sepal length (cm)', 'sepal width (cm)'])
plt.title('sepal data')
plt.show()

# length
length_data = iris_data_df[['sepal length (cm)', 'petal length (cm)']]
plt.plot(length_data)
plt.legend(['sepal length (cm)', 'petal length (cm)'])
plt.title('length data')

# 相关性
sns.pairplot(iris_data_all_df, vars=iris_data_all_df.columns[:4], hue='target', size=3, kind="reg")
plt.show()

'''
Feature engineering
'''

# 变量之间的关系
Corr_Mat = iris_data_df.corr()
Mat_img = plt.matshow(Corr_Mat, cmap=plt.cm.winter_r)
plt.colorbar(Mat_img, ticks=[-1, 0, 1])
plt.show()

# 降维[参考Python DataScience Essentials]
pca = PCA(n_components=2)
pca_2c = pca.fit_transform(iris_data_df)
print(pca.explained_variance_ratio_)
print(pca.explained_variance_ratio_.sum())

plt.scatter(pca_2c[:, 0], pca_2c[:, 1],
            c=np.array(iris_target_df), alpha=0.8,
            cmap=plt.cm.winter)

plt.show()

# train and test our model
X_train, X_test, y_train, y_test = train_test_split(iris_data_df, iris_target_df, test_size=0.3)
clf = SVC()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print(accuracy_score(y_test, predictions))
