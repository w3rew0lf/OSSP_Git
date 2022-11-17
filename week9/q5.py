import numpy as np
import pandas as pd

from sklearn.datasets import load_boston

b_d = load_boston()
data = pd.DataFrame(b_d.data, columns=b_d.feature_names)
data['MEDV'] = b_d.target
X = pd.DataFrame(np.c_[data['LSTAT'], data['RM']], columns = ['LSTAT','RM'])
Y=data['MEDV']
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=24)

from sklearn.preprocessing import StandardScaler
scale=StandardScaler()
X_train = scale.fit_transform(X_train)
X_test = scale.transform(X_test)
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train,y_train)

y_pred = lr.predict(X_test)


print("Accuracy of Logistic Regression: ", accuracy_score(y_test,y_pred))