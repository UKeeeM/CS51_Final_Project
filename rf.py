
import numpy as np
#import pandas as pd
import os
import random
import treepredict as tp
import stagec
import copy
import test2

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

# Subset a data by removing nth column
def subdat(data, n):
	# making sure we are working with a copy of data
	# and not modifying the data set itself
	sub = copy.deepcopy(data)
	#print ("SUBDAT")
	for row in sub:
		#print ("deleteing " + str(n) + "th column")
		#print ("from" + str(row))
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

		# random column to be removed
		# make sure the last column (response variable) is not removed
		rand_column = np.random.randint(len(data[0])-1)

		# boot_data should be subsetted here
		sub_data = subdat(boot_data, rand_column)

		# observation should be subsetted here by the same chosen column
		sub_obs = subdat_obs(observation, rand_column)

		# run a tree on that bootsampled data
		this_tree = tp.buildtree(sub_data, tp.giniimpurity)

		# classification of this specific tree should be done here
		t_result = tp.classify(sub_obs, this_tree)
		
		#print ("printing keys")
		#print (t_result)

		for key in t_result.keys():
			#print ("appending" + key)
			results.append(key)

	return(results)


# Returns the most common element in the list
def most_common(lst):
	return max(set(lst), key=lst.count)

# Random Forest classifier will figure out the result
# that most trees vote on
def rf_classify(rf):
	# a list that keeps count of all the results
	result_count = []

	# shows the proportion of trees that voted for the mode
	mode = most_common(rf)
	mode_count = rf.count(mode)
	proportion = (float(mode_count) / float(len(rf)))

	return(mode, proportion)



#if __name__ == "__main__":
	#print ("hello")
	#print (my_data)
	#predict = ['kiwitobes','France','yes',19,'Basic']
	#predict2 = ['3rd', '70.0000', 'male', '?']
	#check = build_rf(test2.titanic_list, 100, 500, predict2)
	#check = build_rf(my_data, 16, 1000, predict)
	#print(rf_classify(check))


