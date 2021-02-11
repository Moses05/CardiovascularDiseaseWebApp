#importing all libraries for preparing data
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
#importing the algorithms
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

#importing confusion matrix for working out accuracy
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

dataSet = pd.read_csv("heart.csv")

dataSet = dataSet.drop(["thal","ca","slope"], axis=1)

#importing the dataset and dropping "thal", "ca", and "slope" as they are not as important

#Splitting the data set into X (training) and y (test), with a 75% to 25% ratio. Random state of 1 so we have consistent inputs instead of random ones
X = dataSet.iloc[:, :-1].values
y = dataSet.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 1)

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
#Scaling the features

# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)

# I can try use oop with these models
#Decision tree classifier

dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
model1 = dtc
            
#K nearest neighbours

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
model2 = knn

#Random forest classifier

rfc = RandomForestClassifier(n_estimators=10, criterion="entropy", random_state = 1)
rfc.fit(X_train, y_train)
model3 = rfc

X = dataSet.drop(columns=["target"])
y = dataSet["target"]
