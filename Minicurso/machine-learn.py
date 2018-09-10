import scipy
import numpy
import pandas
import sklearn

iris_url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

iris_dataset = pandas.read_csv(iris_url)

iris_names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "classe"]

iris_dataset = pandas.read_csv(iris_url, names=iris_names)

iris_dataset.shape #tamanho da base de dados trabalhada

iris_dataset.tail(n_rows)) #primeiras n linhas do final

iris_dataset.head(n_rows)) #primeiras n linhas do começo

iris_dataset.groupby('classe').size() #tamanho de cada classe na base

wines = pandas.read_csv('/home/carlos_vinicios/Downloads/winequality-red.csv', sep=";") #abre uma nova base de dados, declarando que o separado são ';'

wines.describe() #mostra algumas estatisticas presente na base de dados


#APRENDIZADO DE MAQUINA
from sklearn.tree import DecisionTreeClassifier as dt #tipo de arvore de deicisão
tree = dt() #atribuindo a arvore de decisão a uma variavel

dados = iris_dataset.values
x = dados[:, 0:4] #pegando todas as linhas e da primeira até a terceira coluna
y = dados[:, 4] #pegando todas as linhas e pegando apenas a classe

tree.fit(x, y) #instancia de um algoritmo de aprendizado de maquina, que faz o algoritmo se ajustar a quantidade de exemplos e saidas (treinando o algo com a base que possuimos)

new_example = numpy.array([5.1,2.5,3.6,1.0 ]).reshape(1, 4) #valores para um novo exemplo para o teste no aprendizado de maquina

tree.predict(new_example) #faz uma predição com base em um novo array com valores
