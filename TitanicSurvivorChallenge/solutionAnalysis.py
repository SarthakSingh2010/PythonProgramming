import pandas as pd
import numpy as np

train_df=pd.read_csv('train.csv')
test_df=pd.read_csv('test.csv')
print('\nTRAIN')
print('-'*40)
print(train_df.info())
print('\nTEST')
print('-'*40)
print(test_df.info())
print('\nNaN Count for TRAIN')
print('-'*40)
print(train_df.isnull().sum())
print('\nNaN Count for TEST')
print('-'*40)
print(test_df.isnull().sum())

#visualize
print('-'*40)
print(train_df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False))
print('-'*40)
print(train_df[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))
print('-'*40)
print(train_df[["SibSp", "Survived"]].groupby(['SibSp'], as_index=False).mean().sort_values(by='Survived', ascending=False))
print('-'*40)
print(train_df[["Parch", "Survived"]].groupby(['Parch'], as_index=False).mean().sort_values(by='Survived', ascending=False))

# feature Ticket and Cabin
train_df["CabinBool"] = (train_df["Cabin"].notnull().astype('int'))
test_df["CabinBool"] = (test_df["Cabin"].notnull().astype('int'))
train_df = train_df.drop(['Ticket', 'Cabin'], axis=1)
test_df = test_df.drop(['Ticket', 'Cabin'], axis=1)

# combine datasets
train_test_df=[train_df,test_df] 

# feature name
for dataset in train_test_df:
    dataset['Title']=dataset['Name'].str.extract('([A-Za-z]+)\.',expand=False)
print('-'*40)
print(train_df['Title'].head())
print('-'*40)
print(test_df['Title'].head())

print('-'*40)
print(train_df['Title'].value_counts())

for dataser in train_test_df:
    dataset['Title']=dataset['Title'].replace(['Dr','Rev','Major','Col','Don','Countess','Sir','Capt','Lady','Jonkheer'],'Rare')
    dataset['Title']=dataset['Title'].replace('Mlle','Miss')
    dataset['Title']=dataset['Title'].replace('Ms','Miss')
    dataset['Title']=dataset['Title'].replace('Mme','Mrs')

print('-'*40)
print(train_df[["Title", "Survived"]].groupby(['Title'], as_index=False).mean().sort_values(by='Survived', ascending=False))

title_mapping={'Mr':1,'Miss':2,'Mrs':3,'Master':4,'Rare':5}
for dataset in train_test_df:
    dataset['Title']=dataset['Title'].map(title_mapping)
    dataset['Title']=dataset['Title'].fillna(0)
print('-'*40)
print(train_df['Title'].head())
print('-'*40)
print(test_df['Title'].head())

train_df=train_df.drop('Name',axis=1)
test_df=test_df.drop('Name',axis=1)
train_test_df=[train_df,test_df] #combining again becoz we changed it

# feature sex
sex_mapping={'male':0,'female':1}
for dataset in train_test_df:
    dataset['Sex']=dataset['Sex'].map(sex_mapping)    
print('-'*40)
print(train_df['Sex'].head())
print('-'*40)
print(test_df['Sex'].head())

#feature age
train_df['Age'].fillna(train_df.groupby('Title')['Age'].transform('median'),inplace=True)
test_df['Age'].fillna(test_df.groupby('Title')['Age'].transform('median'),inplace=True)
#range for age based on Pclass
train_df['AgeBand'] = pd.cut(train_df['Age'], 5)
print('-'*40)
print(train_df[['AgeBand', 'Survived']].groupby(['AgeBand'], as_index=False).mean().sort_values(by='AgeBand', ascending=True))

for dataset in train_test_df:    
    dataset.loc[ dataset['Age']<=16,'Age'] = 0
    dataset.loc[(dataset['Age']>16) & (dataset['Age']<=32),'Age'] = 1
    dataset.loc[(dataset['Age']>32) & (dataset['Age']<=48),'Age'] = 2
    dataset.loc[(dataset['Age']>48) & (dataset['Age']<=64),'Age'] = 3
    dataset.loc[dataset['Age']>64,'Age']=4
train_df = train_df.drop(['AgeBand'], axis=1)
train_test_df= [train_df, test_df]
print('-'*40)
print(train_df['Age'].head())
print('-'*40)
print(test_df['Age'].head())

#feature Embarked
pclass1=train_df[train_df['Pclass']==1]['Embarked'].value_counts()
pclass2=train_df[train_df['Pclass']==2]['Embarked'].value_counts()
pclass3=train_df[train_df['Pclass']==3]['Embarked'].value_counts()
print('-'*40)
print(pclass1)
print('-'*40)
print(pclass2)
print('-'*40)
print(pclass3)

for dataset in train_test_df:
    dataset['Embarked']=dataset['Embarked'].fillna('S')

embarked_mapping={'S':0,'C':1,'Q':2}
for dataset in train_test_df:
    dataset['Embarked']=dataset['Embarked'].map(embarked_mapping)

print('-'*40)
print(train_df['Embarked'].head())
print('-'*40)
print(test_df['Embarked'].head())

#feature fare
train_df['Fare'].fillna(train_df.groupby('Pclass')['Fare'].transform('median'),inplace=True)
test_df['Fare'].fillna(test_df.groupby('Pclass')['Fare'].transform('median'),inplace=True)

print('-'*40)
print(train_df['Fare'].head())
print('-'*40)
print(test_df['Fare'].head())

train_df['FamilySize']=train_df['SibSp']+train_df['Parch']+1
test_df['FamilySize']=test_df['SibSp']+test_df['Parch']+1

for dataset in train_test_df:
    dataset['Single'] = dataset['FamilySize'].map(lambda s: 1 if s == 1 else 0)
    dataset['SmallFamily'] = dataset['FamilySize'].map(lambda s: 1 if  s == 2  else 0)
    dataset['MedFamily'] = dataset['FamilySize'].map(lambda s: 1 if 3 <= s <= 4 else 0)
    dataset['LargeFamily'] = dataset['FamilySize'].map(lambda s: 1 if s >= 5 else 0)

train_df=train_df.drop(['SibSp','Parch'],axis=1)
test_df=test_df.drop(['SibSp','Parch'],axis=1)


print('\n\n')
print('-'*40)
print(train_df.info())
print('-'*40)
print(test_df.info())    

#machine larning
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
k_fold = KFold(n_splits=10, shuffle=True, random_state=0)

target=train_df['Survived']
train_df=train_df.drop(['Survived','PassengerId'],axis=1)

scorelis=[]

clf=DecisionTreeClassifier()
score=cross_val_score(clf,train_df,target,cv=k_fold,n_jobs=1,scoring='accuracy')
#print(score)
print('Decision Tree: ',round(np.mean(score)*100, 2))
scorelis.append(['Decision Tree: ',round(np.mean(score)*100, 2)])

clf=GaussianNB()
score=cross_val_score(clf,train_df,target,cv=k_fold,n_jobs=1,scoring='accuracy')
#print(score)
print('Naive Bayes: ',round(np.mean(score)*100, 2))
scorelis.append(['Naive Bayes: ',round(np.mean(score)*100, 2)])

clf=SVC()
score=cross_val_score(clf,train_df,target,cv=k_fold,n_jobs=1,scoring='accuracy')
#print(score)
print('SVM: ',round(np.mean(score)*100, 2))
scorelis.append(['SVM: ',round(np.mean(score)*100, 2)])

clf=RandomForestClassifier(n_estimators=13)
score=cross_val_score(clf,train_df,target,cv=k_fold,n_jobs=1,scoring='accuracy')
#print(score)
print('Random Forest: ',round(np.mean(score)*100, 2))
scorelis.append(['Random Forest: ',round(np.mean(score)*100, 2)])

clf=KNeighborsClassifier(n_neighbors=13)
score=cross_val_score(clf,train_df,target,cv=k_fold,n_jobs=1,scoring='accuracy')
#print(score)
print('K Neighbors: ',round(np.mean(score)*100,2))
scorelis.append(['K Neighbors: ',round(np.mean(score)*100, 2)])

clf=LogisticRegression()
score=cross_val_score(clf,train_df,target,cv=k_fold,n_jobs=1,scoring='accuracy')
#print(score)
print('Logistic Regression: ',round(np.mean(score)*100,2))
scorelis.append(['Logistic Regression: ',round(np.mean(score)*100, 2)])

print('\n'+('-'*40)+'\n')
for i in range(0,len(scorelis),2):
    print(str(scorelis[i])+' '+str(scorelis[i+1]))
print('\n'+('_'*40)+'\n')

#testing
clf = SVC()
clf.fit(train_df, target)
pick=test_df['PassengerId']
test_df = test_df.drop('PassengerId', axis=1)
prediction = clf.predict(test_df)

submission = pd.DataFrame({
        "PassengerId": pick,
        "Survived": prediction
    })

submission.to_csv('submission.csv', index=False)