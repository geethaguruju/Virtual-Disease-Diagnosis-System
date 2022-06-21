import pandas as pd
import numpy as np
from sklearn.externals import joblib
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from sklearn.linear_model import LogisticRegression
#warnings.filterwarnings("ignore", category=DeprecationWarning) 
from sklearn.preprocessing import StandardScaler
import random
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_validate

data = pd.read_csv("heart.csv")
data["trestbps"]=np.log(data["trestbps"])

data=data.drop(["fbs"],axis=1)
data=data.drop(["ca"],axis=1)
data["chol"]=np.log(data["chol"])
target=data["target"]
print(data.shape[1])

np.random.shuffle(data.values)
data=data.drop(["target"],axis=1)
print(data.columns)
sc= StandardScaler()
data=sc.fit_transform(data)

lr=LogisticRegression()
lr.fit(data,target)
cv_results = cross_validate(lr, data,target, cv=10)
print(cv_results)
y_pred=lr.predict(data)
from sklearn.metrics import accuracy_score
acc_logreg1 = round(accuracy_score(y_pred, target) , 2)*100
print("Accuracy of logistic regression : ",acc_logreg1)
#joblib.dump(lr,"model2")

#accuracy 83