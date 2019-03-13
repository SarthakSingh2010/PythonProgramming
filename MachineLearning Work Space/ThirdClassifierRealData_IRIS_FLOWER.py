from sklearn import tree
from sklearn.datasets import load_iris
#data IRIS_FLOWER
#sepal lenght,sepal width,petal length,petal width,species(label)
#0: Iris setosa 1: Iris versicolor 2:Iris virginica
iris=load_iris()
print(iris.feature_names)
print(iris.data[0]) #[sepal lenght,sepal width,petal length,petal width]feature
print(iris.target[0])#[species] target
#Train Data
clf=tree.DecisionTreeClassifier()
clf=clf.fit(iris.data,iris.target)
#Predict for new data
newData=[[6.4,3.1,4.4,1.2]]
print(clf.predict(newData))