'''
参考YouTube上Google developers的系列视频
https://www.youtube.com/watch?v=cKxRvEZd3Mw
'''

from scipy.spatial import distance


class ScrappyKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)

        return predictions

    def closest(self, row):
        best_dist = self.euc(row, self.X_train[0])
        best_index = 0
        for i in range(len(X_train)):
            dist = self.euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]

    def euc(self, a, b):
        return distance.euclidean(a, b)


from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)

my_classifier = ScrappyKNN()
my_classifier.fit(X_train, y_train)
predictions = my_classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, predictions))


# 0.973684210526
