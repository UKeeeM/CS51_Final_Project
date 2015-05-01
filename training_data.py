'''
CS51 Final CS51_Final_Project
training_data.py

This file imports our test datasets as well as other data frames
to test the accuracy of our algorithm
'''
import os as os
import numpy as np
import pandas as pd
import csv

os.path.abspath("/Users/seungjaecha/Desktop/CS51_Final_Project")

titanic_csv = pd.read_csv('titanic2.csv')
pima_csv = pd.read_csv('pima.csv')
stagec_csv = pd.read_csv('stagec.csv')
spam_csv = pd.read_csv('spam.csv')

titanic = titanic_csv.values.tolist()
pima = pima_csv.values.tolist()
stagec = stagec_csv.values.tolist()
spam = spam_csv.values.tolist()

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

# Training Data is for the last 2500 rows
spam_training = spam[-2500:]
# Testing data is for the first 50 rows
spam_testing = pima[:50]

