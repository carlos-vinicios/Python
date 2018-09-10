import scipy
import numpy
import pandas
import sklearn

wine_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"

wine_names = ["classe", "Alcohool", "Malic Acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]
wine_dataset = pandas.read_csv(wine_url, names=wine_names)

from sklearn.tree import DecisionTreeClassifier as dt
tree = dt()

dados = wine_dataset.values

x = dados[:, 1:14]
y = dados[:, 0]

tree.fit(x,y)

new_example = numpy.array([7.84,2.0,1.70,16.0,88,3.0,2.12,0.30,1.90,4.383400,0.92,3.59,1040]).reshape(1, 13)

print(tree.predict(new_example))
