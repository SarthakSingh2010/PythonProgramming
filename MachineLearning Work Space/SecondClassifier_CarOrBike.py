from sklearn import tree

#0: motorcycle 1: car
label=[0,0,1,0,1,1,0,0]
#[wheels,seats]
feature=[[2,2],[2,2],[3,4],[2,2],[4,4],[4,4],[3,2],[2,2]]

clf=tree.DecisionTreeClassifier()
clf=clf.fit(feature,label)
newData=[[2,1],[3,4]]
print(clf.predict(newData))