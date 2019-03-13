from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score

#data IRIS_FLOWER
#sepal lenght,sepal width,petal length,petal width,species(label)
#0: Iris setosa 1: Iris versicolor 2:Iris virginica
iris=load_iris()
#feature
x=iris.data
#label or class
y=iris.target
# split: training and test set 0.5 mean 50% training and 50% testing
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5)
#train classifier
clf=tree.DecisionTreeClassifier()
clf.fit(x_train,y_train)
#predict for test data
prediction=clf.predict(x_test)
print(accuracy_score(y_test,prediction))
