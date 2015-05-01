'''
CS51 Final CS51_Final_Project
rf.py

This is where random forest is implemented
'''
import numpy as np
import os
import random
import CART_tree as cart
import copy
import training_data as td


# Subset a data by removing nth column
def subdat(data, n):
	# making sure we are working with a copy of data
	# and not modifying the data set itself
	sub = copy.deepcopy(data)
	for row in sub:
		del row[n]
	return(sub)	

# Subset an observation
def subdat_obs(obs,n):
	sub = copy.deepcopy(obs)
	del sub[n]
	return(sub)

# Bootstrap sample (sampling with replacement) our data
# Return a new bootstrap data set
def bootstrap(data,n):
	new_data = []
	for x in range(0,n):
		new_data.append(copy.deepcopy(random.choice(data)))
	return (new_data)

# Build a random forest with ntree many trees
def build_rf(data, n, ntree, observation):
	results = []
	# take a bootstrap sample and run a tree
	for x in range(0,ntree):
		boot_data = bootstrap(data,n)
		# print("the nth tree is " + str(x))
		# random column to be removed
		# make sure the last column (response variable) is not removed
		# rand_column = np.random.randint(len(data[0])-1)
		rand_column = np.random.randint(len(data[0])-1)

		# boot_data should be subsetted here
		sub_data = subdat(boot_data, rand_column)

		# observation should be subsetted here by the same chosen column
		sub_obs = subdat_obs(observation, rand_column)

		# run a tree on that bootsampled data
		this_tree = cart.create(sub_data, cart.giniimpurity)

		# classification of this specific tree should be done here
		t_result = cart.classify(sub_obs, this_tree)

		for key in t_result.keys():
			results.append(key)
	
	return(results)


# Returns the most common element in the list
def most_common(lst):
	return max(set(lst), key=lst.count)

# Random Forest classifier will figure out the result
# that most trees vote on
def rf_vote(rf):
	# a list that keeps count of all the results
	result_count = []

	# shows the proportion of trees that voted for the mode
	mode = most_common(rf)
	mode_count = rf.count(mode)
	proportion = (float(mode_count) / float(len(rf)))

	return(mode, proportion)

def test_accuracy(training_data, test_data):
	
	accuracy_count = 0
	
	for row in range(0,len(test_data)):
		one_row = test_data[row]
		rf_build = build_rf(training_data, 100, 200, one_row)
		rf_decision = rf_vote(rf_build)

		# Comparing prediction and the actual result
		if (rf_decision[0] == one_row[-1]):
			accuracy_count = accuracy_count + 1

	accuracy_rate = float(accuracy_count) / float(len(test_data))
	return(accuracy_rate)




