
import numpy as np
import pandas as pd
import os
import csv

# Setting absolute path at the project folder
os.path.abspath("/Desktop/CS51_Final_Project/")

data_df = pd.read_csv('titanic.csv')
#titanic_X = data_df[:, [1,4,10]]

with open('titanic.csv', 'rt') as csvfile:
	titanic_reader = csv.reader(csvfile, delimiter=',',
		quotechar = '"')

	row = titanic_reader.__next__()
	feature_names = np.array(row)

	titanic_X, titanic_y = [], []
	for row in titanic_reader:
		titanic_X.append(row)
		titanic_y.append(row[2])
		"survived"

	# X are the predictors
	titanic_X = np.array(titanic_X)
	# y is the response variable we're trying to predict
	titanic_y = np.array(titanic_y)

# we keep class, age, and sex
titanic_X = titanic_X[:, [1, 4, 10]]
feature_names = feature_names[[1,4,10]]

vars = feature_names
data_len = len(titanic_X)

print (vars)
print (data_len)
print (titanic_X[1])
print (titanic_y[582])