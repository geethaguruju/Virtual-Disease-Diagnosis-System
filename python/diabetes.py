import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

# DATA FOR PRED
data=pd.read_csv("diabetes.csv")
print(data.head())

X = data.iloc[:,:-1]
y = y = data.iloc[:,-1]
print(X.shape[1])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 25,random_state = 0)

print("Train Set: ", X_train.shape, y_train.shape)
print("Test Set: ", X_test.shape, y_test.shape)

# random forest Classifier
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 6, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score
acc_rf = round(accuracy_score(y_pred, y_test) , 2)*100
print("Accuracy of random forest: ",acc_rf)

#logistic regression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,r2_score,classification_report
logreg = LogisticRegression(solver='lbfgs',max_iter=1000)
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
acc_logreg1 = round(accuracy_score(y_pred, y_test) , 2)*100
print("Accuracy of logistic regression : ",acc_logreg1)

#knn
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
acc_knn = round(accuracy_score(y_pred,y_test), 2) * 100
print("Accuracy of knn:" ,acc_knn)

#joblib.dump(logreg,"model1")

