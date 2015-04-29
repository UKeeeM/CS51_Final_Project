
import numpy as np
import pandas as pd
import os
import random
import treepredict as tp
import stagec

my_data=[['slashdot','USA','yes',18,'None'],
        ['google','France','yes',23,'Premium'],
        ['digg','USA','yes',24,'Basic'],
        ['kiwitobes','France','yes',23,'Basic'],
        ['google','UK','no',21,'Premium'],
        ['(direct)','New Zealand','no',12,'None'],
        ['(direct)','UK','no',21,'Basic'],
        ['google','USA','no',24,'Premium'],
        ['slashdot','France','yes',19,'None'],
        ['digg','USA','no',18,'None'],
        ['google','UK','no',18,'None'],
        ['kiwitobes','UK','no',19,'None'],
        ['digg','New Zealand','yes',12,'Basic'],
        ['slashdot','UK','no',21,'None'],
        ['google','UK','yes',18,'Basic'],
        ['kiwitobes','France','yes',19,'Basic']]

# Bootstrap sample (sampling with replacement) our data
# Return a new bootstrap data set
def bootstrap(data,n):
	new_data = []
	for x in range(0,n):
		new_data.append(random.choice(data))
	return (new_data)

# Build a random forest with ntree many trees
def build_rf(data, n, ntree):
	trees = []
	# take a bootstrap sample and run a tree
	for x in range(0,ntree):
		boot_data = bootstrap(data,n)
		# run a tree on that bootsampled data
		trees.append(tp.buildtree(boot_data))
	return(trees)

# Returns the most common element in the list
def most_common(lst):
	return max(set(lst), key=lst.count)

# Random Forest classifier will figure out the result
# that most trees vote on
def rf_classify(observation, rf):
	# a dictionary that keeps count of all the results
	result_count = []

	for i in range(0, len(rf)):
		t_result = tp.classify(observation, rf[i])
		for key in t_result.keys():
			result_count.append(key)

	mode = most_common(result_count)
	mode_count = result_count.count(mode)
	proportion = (float(mode_count) / float(len(result_count)))

	return(mode, proportion)



