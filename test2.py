
import numpy as np
import pandas as pd
import os
import sys
import csv

# Setting absolute path at the project folder
os.path.abspath("C:\Users\You-Myeong\Documents\GitHub\CS51_Final_Project")

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

#dates = date_range('1/1/2000', periods=8)
#df = DataFrame(randn(8,4), index=dates, columns=['A', 'B', 'C', 'D'])

print (vars)
#print (titanic_X)
#print (titanic_X[1])
#print (titanic_y[1])
#print (type(titanic_X))

df = pd.DataFrame(titanic_X)
df.columns = vars
df['survived'] = titanic_y

# We now have a complete df

# Practicing subsetting
# Subset a new value where people survived

#print (df[df['age'] > 0])
new_df = df[df['age'] != 'NA']
#print (new_df)

len(new_df.columns)
df_age = new_df[['pclass']]
print(df_age)
print (type(df_age))
print (sys.version)

