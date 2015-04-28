"""
so each data will have attributes, n = number of data, g = gini impurity,
D = actual data sets)
"""

'''The decision tree is made up of, 
	col = index of attribute to be tested, 
	value = value that a column must match to be classified true


modify it a bit to fit the data frame model!!
'''
class Node:
    def __init__(self, col = -1, value = None, results = None, true_b = None, false_b = None):
        self.col = col #data frame thingie#
        self.value = value
        self.results = results
        self.true_b = true_b
        self.false_b = false_b



def divide_tree 
