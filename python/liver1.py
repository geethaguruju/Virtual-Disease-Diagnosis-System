import pandas as pd
import numpy as np
pd.pandas.set_option('display.max_columns', None)
dataset = pd.read_csv("liver.csv")
# Top 5 records:
dataset.head()
dataset.shape
dataset.isnull().sum()
dataset['Albumin_and_Globulin_Ratio'] = dataset['Albumin_and_Globulin_Ratio'].fillna(dataset['Albumin_and_Globulin_Ratio'].median())
dataset['Gender'] = np.where(dataset['Gender']=='Male', 1,0)
dataset.columns
dataset = dataset.drop('Direct_Bilirubin', axis=1)
uppper_boundary=dataset['Total_Protiens'].mean() + 3* dataset['Total_Protiens'].std()
lower_boundary=dataset['Total_Protiens'].mean() - 3* dataset['Total_Protiens'].std()
uppper_boundary=dataset['Albumin'].mean() + 3* dataset['Albumin'].std()
lower_boundary=dataset['Albumin'].mean() - 3* dataset['Albumin'].std()
IQR = dataset.Total_Bilirubin.quantile(0.75)-dataset.Total_Bilirubin.quantile(0.25)

# Extreme outliers
lower_bridge = dataset['Total_Bilirubin'].quantile(0.25) - (IQR*3)
upper_bridge = dataset['Total_Bilirubin'].quantile(0.75) + (IQR*3)
# if value greater than upper bridge, we replace that value with upper_bridge value:
dataset.loc[dataset['Total_Bilirubin'] >= upper_bridge, 'Total_Bilirubin'] = upper_bridge

IQR = dataset.Alkaline_Phosphotase.quantile(0.75) - dataset.Alkaline_Phosphotase.quantile(0.25)

# Extreme outliers
lower_bridge = dataset['Alkaline_Phosphotase'].quantile(0.25) - (IQR*3)
upper_bridge = dataset['Alkaline_Phosphotase'].quantile(0.75) + (IQR*3)


# if value greater than upper bridge, we replace that value with upper_bridge value:
dataset.loc[dataset['Alkaline_Phosphotase'] >= upper_bridge, 'Alkaline_Phosphotase'] = upper_bridge

# Lets compute the Interquantile range of Alamine_Aminotransferase feature to calculate the boundaries:
IQR = dataset.Alamine_Aminotransferase.quantile(0.75) - dataset.Alamine_Aminotransferase.quantile(0.25)

# Extreme outliers
lower_bridge = dataset['Alamine_Aminotransferase'].quantile(0.25) - (IQR*3)
upper_bridge = dataset['Alamine_Aminotransferase'].quantile(0.75) + (IQR*3)

# if value greater than upper bridge, we replace that value with upper_bridge value:
dataset.loc[dataset['Alamine_Aminotransferase'] >= upper_bridge, 'Alamine_Aminotransferase'] = upper_bridge

IQR = dataset.Aspartate_Aminotransferase.quantile(0.75) - dataset.Aspartate_Aminotransferase.quantile(0.25)

# Extreme outliers
lower_bridge = dataset['Aspartate_Aminotransferase'].quantile(0.25) - (IQR*3)
upper_bridge = dataset['Aspartate_Aminotransferase'].quantile(0.75) + (IQR*3)

# if value greater than upper bridge, we replace that value with upper_bridge value:
dataset.loc[dataset['Aspartate_Aminotransferase'] >= upper_bridge, 'Aspartate_Aminotransferase'] = upper_bridge
# compute the Interquantile range of Albumin_and_Globulin_Ratio feature to calculate the boundaries
IQR = dataset.Albumin_and_Globulin_Ratio.quantile(0.75) - dataset.Albumin_and_Globulin_Ratio.quantile(0.25)

# Extreme outliers
lower_bridge = dataset['Albumin_and_Globulin_Ratio'].quantile(0.25) - (IQR*3)
upper_bridge = dataset['Albumin_and_Globulin_Ratio'].quantile(0.75) + (IQR*3)


# if value greater than upper bridge, we replace that value with upper_bridge value:
dataset.loc[dataset['Albumin_and_Globulin_Ratio'] >= upper_bridge, 'Albumin_and_Globulin_Ratio'] = upper_bridge
# Independent and Dependent Feature:
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

from imblearn.combine import SMOTETomek
smote = SMOTETomek()
X_smote, y_smote = smote.fit_resample(X,y)
from collections import Counter
#print('Before SMOTE : ', Counter(y))
#print('After SMOTE  : ', Counter(y_smote))

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_smote,y_smote, test_size=0.3, random_state=33)
#print(X_train.shape)

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

### Apply SelectKBest Algorithm
ordered_rank_features=SelectKBest(score_func=chi2,k=9)
ordered_feature=ordered_rank_features.fit(X,y)

dfscores=pd.DataFrame(ordered_feature.scores_,columns=["Score"])
dfcolumns=pd.DataFrame(X.columns)

features_rank=pd.concat([dfcolumns,dfscores],axis=1)

features_rank.columns=['Features','Score']
features_rank.nlargest(9, 'Score')

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# RandomForestClassifier: 83.7
from sklearn.ensemble import RandomForestClassifier
RandomForest = RandomForestClassifier()
RandomForest = RandomForest.fit(X_train,y_train)

# Predictions:
y_pred = RandomForest.predict(X_test)

# Performance:
print('Accuracy of Random forest:', accuracy_score(y_test,y_pred))
#print(confusion_matrix(y_test,y_pred))
#print(classification_report(y_test,y_pred))

from sklearn.ensemble import AdaBoostClassifier
AdaBoost = AdaBoostClassifier()
AdaBoost = AdaBoost.fit(X_train,y_train)

# Predictions:
y_pred = AdaBoost.predict(X_test)

# Performance:
print('Accuracy of Ada Boost Classifier:', accuracy_score(y_test,y_pred))
#print(confusion_matrix(y_test,y_pred))
#print(classification_report(y_test,y_pred))

# GradientBoostingClassifier: 83.5
from sklearn.ensemble import GradientBoostingClassifier
GradientBoost = GradientBoostingClassifier()
GradientBoost = GradientBoost.fit(X_train,y_train)

# Predictions:
y_pred = GradientBoost.predict(X_test)

# Performance:  
print('Accuracy of Gradient:', accuracy_score(y_test,y_pred))
#print(confusion_matrix(y_test,y_pred))
#print(classification_report(y_test,y_pred))

from sklearn.externals import joblib
#joblib.dump(GradientBoost,"model41")