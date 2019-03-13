from sklearn.tree import DecisionTreeClassifier

#preparing training data and labels
# 0: fish , 1:cat
labels=[0,0,1,1,0]
#[legs,weight] of 5 data
features=[[0,50],[0,150000],[4,5],[4,6],[0,0.05]] #training data

#choosing a classifier
algorithm=DecisionTreeClassifier()

#training the classifier
algorithm=algorithm.fit(features,labels)

#predict with new data
newData=[[0,30]]
print(algorithm.predict(newData))