import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white", color_codes=True)

iris = pd.read_csv("Iris.csv")
print(iris.head())

# How many examples we have of each species
print(iris["Species"].value_counts())

# scatter
iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")

sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=5)
sns.FacetGrid(iris, hue="Species", size=5).map(plt.scatter, "SepalLengthCm", "SepalWidthCm").add_legend()
sns.boxplot(x="Species", y="PetalLengthCm", data=iris)

ax = sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
ax = sns.stripplot(x="Species", y="PetalLengthCm", data=iris, jitter=True, edgecolor="gray")

sns.violinplot(x="Species", y="PetalLengthCm", data=iris)

sns.FacetGrid(iris, hue="Species", size=6) \
    .map(sns.kdeplot, "PetalLengthCm") \
    .add_legend()

sns.pairplot(iris.drop("Id", axis=1), hue="Species", size=3)

sns.pairplot(iris.drop("Id", axis=1), hue="Species", size=3, diag_kind="kde")
iris.drop("Id", axis=1).boxplot(by="Species", figsize=(12, 6))

from pandas.tools.plotting import andrews_curves

andrews_curves(iris.drop("Id", axis=1), "Species")

from pandas.tools.plotting import radviz

radviz(iris.drop("Id", axis=1), "Species")
