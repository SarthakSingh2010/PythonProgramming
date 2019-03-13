from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score

wine=datasets.load_wine()
print(wine.feature_names)
print(wine.data[0])
print(wine.target[0])
x=wine.data
y=wine.target
x_train,x_test,y_train,y_test=tts(x,y,test_size=0.2)
clf=svm.SVC()
clf.fit(x_train,y_train)
predictions=clf.predict(x_test)
print(accuracy_score(y_test,predictions))
