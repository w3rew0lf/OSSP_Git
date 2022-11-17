import pandas as pd
from sklearn.model_selection import train_test_split
iris = pd.read_csv("iris.csv")
X = iris.iloc[:, :-1].values
y = iris.iloc[:, 4].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
print(X_train[:5])
print(y_train[:5])