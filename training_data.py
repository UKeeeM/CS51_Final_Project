import os as os
import numpy as np
import pandas as pd
import csv
from random import shuffle

os.path.abspath("/Users/seungjaecha/Desktop/CS51_Final_Project")

titanic_csv = pd.read_csv('titanic.csv')
pima_csv = pd.read_csv('pima.csv')
stagec_csv = pd.read_csv('stagec.csv')
spam_csv = pd.read_csv('spam.csv')

#print (stagec_csv.columns.values)

titanic = titanic_csv.values.tolist()
pima = pima_csv.values.tolist()
stagec = stagec_csv.values.tolist()
spam = spam_csv.values.tolist()

##print (len(titanic))
#print (len(pima))
#print (len(stagec))

# Training Data is the first 550 rows of the data
titanic_training = titanic[:550]
# Testing data is the last 83 rows of the data
titanic_testing = titanic[-83:]

# First 100 rows of data
stagec_training = stagec[:100]
# Last 34 rows of data
stagec_testing = stagec[-34:]

# Training Data is the first 300 rows
pima_training = pima[:300]
# Testing Data is the last 92 rows
pima_testing = pima[-92:]

# Training Data is for the first 2500 rows
spam_training = spam[-2500:]
# Testing data is for the last 100 rows
spam_testing = pima[:50]
