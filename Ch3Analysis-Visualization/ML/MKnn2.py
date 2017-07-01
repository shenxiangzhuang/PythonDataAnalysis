'''
参考YouTube上Google developers的系列视频
https://www.youtube.com/watch?v=cKxRvEZd3Mw
'''

import numpy as np
import operator
from scipy.spatial import distance


class ScrappyKNN():
    def fit(self, X_train, y_train, k):
        self.X_train = X_train
        self.y_train = y_train
        self.k = k

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest_k(row)
            predictions.append(label)

        return predictions

    def closest_k(self, row):
        # distances存储测试点到数据集各个点的距离
        distances = []
        for i in range(len(X_train)):
            dist = self.euc(row, self.X_train[i])
            distances.append(dist)

        # 转换成数组，对距离排序（从小到大）,返回位置信息
        distances = np.array(distances)
        sortedDistIndicies = distances.argsort()

        classCount = {}
        for i in range(self.k):
            voteIlabel = y_train[sortedDistIndicies[i]]
            # 此处get，原字典有此voteIlabel则返回其对应的值，没有则返回0
            classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

        # 根据值（对应“票数”）进行排序，使得获得票数多的类在前（故使用reverse=True）
        sortedClassCount = sorted(classCount.items(),
                                  key=operator.itemgetter(1), reverse=True)
        # 返回该测试点的类别
        return sortedClassCount[0][0]

    # 计算欧式距离
    def euc(self, a, b):
        return distance.euclidean(a, b)


from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)

my_classifier = ScrappyKNN()
my_classifier.fit(X_train, y_train, k=3)
predictions = my_classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, predictions))

# 0.973684210526
