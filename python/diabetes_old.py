from json import load
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

# DATA FOR PRED
data=pd.read_csv("diabetes.csv")
print(data.head())


logreg=LogisticRegression()



X=data.iloc[:,:8]
print(X.shape[1])


y=data[["Outcome"]]

X=np.array(X)
y=np.array(y)

logreg.fit(X,y.reshape(-1,))
y_pred=logreg.predict(X)
from sklearn.metrics import accuracy_score
acc_logreg1 = round(accuracy_score(y_pred, y) , 2)*100
print("Accuracy of logistic regression : ",acc_logreg1)