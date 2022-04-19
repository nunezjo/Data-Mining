# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z4_qaKSEBaFoS5DYqUHB7wMjvGm69qG9
"""

from google.colab import files 
files.upload()

files.upload()

import pandas as pd
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")
#print(train_df.head())
#print(test_df.head())

train_df = train_df.drop(['id'], axis = 1)
test_df = test_df.drop(['id'], axis = 1)
# print(train_df.head())
# print(test_df.head())

train_df.loc[train_df["diagnosis"] == "M", "diagnosis"] = 1
train_df.loc[train_df["diagnosis"] == "B", "diagnosis"] = 0

test_df.loc[test_df["diagnosis"] == "M", "diagnosis"] = 1
test_df.loc[test_df["diagnosis"] == "B", "diagnosis"] = 0
#print(list(train_df.columns))
#print(test_df.head())

features = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

y_train = train_df['diagnosis']
y_test = test_df['diagnosis']

x_train = train_df[features]
x_test = test_df[features]

y_train = y_train.astype('int')
y_test = y_test.astype('int')

#print(y_train)

#Min-Max normalization

x_min_train = x_train.min() 
x_min_test = x_test.min()

#print(x_min_train, "\n") 
#print(x_min_test, "\n \n \n \n ")

x_max_train = x_train.max()
x_max_test = x_test.max()

#print(x_max_train, "\n")
#print(x_max_test, "\n" "\n")

max_x = pd.concat([x_max_train,x_max_test]).max(level = 0)
min_x = pd.concat([x_min_train,x_min_test]).min(level = 0)

#print(max_x,"\n")
#print(min_x)

min_max_train = (x_train - x_min_test) / (max_x - min_x) 
min_max_test = (x_test - x_min_test) / (max_x - min_x)

#print(min_max_train)
#print(min_max_test)

#Z-Score Normalization

x_train_z = (x_train - x_train.mean()) / (x_train.std())
x_test_z = (x_test - x_train.mean()) / (x_train.std())

print(x_train_z)

from sklearn.tree import DecisionTreeClassifier
decision_tree_clf = DecisionTreeClassifier(max_depth= 5, splitter = "random")
#decision_tree_clf_min_max = DecisionTreeClassifier(max_depth= 3, splitter = "random" )
#decision_tree_clf_z = DecisionTreeClassifier(max_depth= 5, splitter = "random" )

decision_tree_clf.fit(x_train, y_train)
#decision_tree_clf_min_max.fit(min_max_train, y_train)
#decision_tree_clf_z.fit(x_train_z, y_train)

predictions = decision_tree_clf.predict(x_test)
#predictions_min_max = decision_tree_clf_min_max.predict(min_max_test)
#predictions_z = decision_tree_clf_z.predict(x_test_z)

from sklearn.metrics import accuracy_score
score = accuracy_score(y_test,predictions)
print(score)
#score_min_max = accuracy_score(y_test,predictions_min_max)
#print(score_min_max)
#score_z = accuracy_score(y_test,predictions_z)
#print(score_z)