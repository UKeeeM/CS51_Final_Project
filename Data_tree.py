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



def divide_tree (rows, column, value):
	#insert a function to allow us to divide this thing.  depends on if numeric or not
	split_function = None   #for now
	if isinstance(value,int) or isinstance(value, float):
		split_function = lambda row:row[column]>=value
	else:
		split_function = lambda row:row[column]==value

	set1 = [row for row in rows if split_function(row)]
	set2 = [row for row in rows if not split_function(row)]
	return (set1,set2)

#last column will be the target attributes that we are looking for x in xrange(1,10):
def unique_counter (rows):
	result = {}
	for row in rows:
		#result in last column
		r = row[len(row)-1]
		if r not in results: results[r] = 0
		results[r]+=1
	return results

#calculates gini impurity
def gini_calculator(rows):
	total = len(rows)
	counts = unique_counter(rows)
	imp = 0 
	for x1 in counts:
		y1 = float(counts[x1])/total
		for x2 in counts:
			if x1==x2: continue
			y2=float(counts[x2])/total
			imp+= y1*y2
		return imp 

def entropy(rows):
	from match import log 
	log2 = lambda x:log(x)/log(2)
	results = unique_counter(rows)
	ent = 0.0
	for r in results.keys():
		p=float(results[r])/len(rows)
		ent = ent - p*log2(p)
	return ent 

