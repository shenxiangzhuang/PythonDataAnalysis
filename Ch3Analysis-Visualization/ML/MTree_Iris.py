'''
pip install pydotplus
pip install graphviz
sudo apt-get install graphviz
'''

import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
import pydotplus
from io import StringIO

# 载入数据集
iris = load_iris()
'''
do somethings to explore the dataset
'''
test_idx = [0, 50, 100]

# training data
train_data = np.delete(iris.data, test_idx, axis=0)
train_target = np.delete(iris.target, test_idx)
print(train_target)
# testing data
test_data = iris.data[test_idx]
test_target = iris.target[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)
print("正确类别：", test_target)
print("预测类别：", clf.predict(test_data))

# Displaying the decision tree
out = StringIO()
tree.export_graphviz(clf, out_file=out,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     impurity=False)
graph = pydotplus.graph_from_dot_data(out.getvalue())
# graph.write_pdf('iris.pdf')
data = graph.create_png()  # 图片的二进制数据
with open('tree.png', 'wb') as f:
    f.write(data)

print("测试集其一数据：", test_data[0], test_target[0])
print("特征：", iris.feature_names)
print("标签", iris.target_names)
