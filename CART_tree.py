'''
CS51 Final CS51_Final_Project
CART_tree.py

Implementation of the decision tree class and related functions
'''

# We initialize the basecase for the code itself, so that we can return thi
class decision_tree:
  def __init__(self,attr_index=-1,compare=None,answer=None,r=None,l=None):
    #this is an index to keep track of attribute being tested
    self.attr_index = attr_index
    # this is the value that we are comparing attributes with
    self.compare=compare
    # end result that we are trying to determine
    self.answer=answer
    #The right branch of the tree, it is always right
    self.r=r
    #The left branch of the tree, it is always false
    self.l=l

''' helper function that will 
    1.) determine whether we are looking at numerical or categorical data
    2.) divide into two sets accordingly 
        a.) Set 1 is the true group or right branch
        b.) set 2 is the false group or left branch'''
def divide(data,attr_index,compare):
    tset = []
    fset = [] 
    # this checks if the data that we are dealing with is true or false 
    if isinstance(compare,int) or isinstance(compare,float):
        for row in data: 
            # put into right branch because this is true
            if row[attr_index] >= compare:
                tset.append(row)
            else:
                fset.append(row)
        return(tset,fset)
    else:
        for row in data:
            # put into right branch because this is true
            if row[attr_index] == compare:
                tset.append(row)
            else:
                fset.append(row)
        return(tset,fset)

'''This is a helper function that keeps track of number of times a result 
appears. this is very useful when calculating Gini Impurity and Entropy '''
def counter(data):
    #dicitonary to store the results in
   results={}
   for row in data:
      # note the minus one due ommitting the last column that contains answer
      r=row[len(row)-1]
      if r not in results: results[r]=0
      results[r]+=1
   # the answer will be returned with it being the key and frequency as value 
   return results 

# Calculates the proportions of certain answer vs total answers
def proportions(data):
    total = len(data)
    counts = counter(data)
    p = []
    for keys in counts:
        p1 = float(counts[keys])/total
        p.append(p1)
    #output is now a list that contains all the proportions 
    return p

# Function to calculate the Gini Impurity    
def giniimpurity(data): 
    p = proportions(data)
    return 1 - sum([i**2 for i in p])

# Function to calculate the Entropy    
def entropy(rows): 
    p = proportions(rows)
    from math import log 
    return sum([(-i * log(i,2)) for i in p])

# A small helper function that will remove any duplicaets from a list
def remove_duplicate(list):
    list_two = [] 
    for i in list:
        if i not in list_two:
            list_two.append(i)
    return list_two

''' a recursive function that will build the decision tree using the values
    that we have obtained from above '''
    
def create(data, measure = giniimpurity):
    #return the basecase if the data is empty
    if len(data)==0: return decision_tree()
    # keeps track of current entropy and gini impurity  
    current_measure = measure(data)
    
    # initialize variables to keep track of what our next branch lookks like
    # Most amount of information gained
    information_gain = 0.0
    # attribute to be used
    attribute=None
    # set that will be used
    sets=None
    
    # this is number of attributes our dataset has
    attr_count=len(data[0])-1
  
    for attr in range(0,attr_count):

        # saves all the values of an attribute here
        values_o = []
        for row in data:
            values_o.append(row[attr])
        # we remove duplicates here so we only test for this once
        values = remove_duplicate(values_o)   
        # This part is where we use each value to divide the data 
        
        for value in values:
            (tset,fset)=divide(data,attr,value)
            # Here we calculate the information gain and save ones most gain
            p=float(len(tset))/len(data) 
            gain=current_measure-p*measure(tset)-(1-p)*measure(fset)
            # checks if information gained is better than saved best gain
            if gain>information_gain and len(tset)>0 and len(fset)>0:
                #in that case we update the saved sets
                information_gain = gain
                attribute=(attr,value)
                sets=(tset,fset)
    # This is where we use recursion to build the tree again in branches
    if information_gain>0:
        #whenever the best gain is greater than zero, we build branches
        tTree=create(sets[0])
        fTree=create(sets[1])
        #finally update and return the tree with updated information
        return decision_tree(attr_index = attribute[0],compare = attribute[1],
                        r=tTree,l=fTree)
    # if the best combination did not yield more information gain , branch ends
    else:
        return decision_tree(answer=counter(data))

    ''' this is the function that then takes in a data set as an input
    and it also takes in the CART tree built from training dataset
    Then it will tell us likley hodd of beloning to one of the answers '''    
def classify(data_point,cart):
    ''' this checks if the tree's end point has been rechead since only endpoints 
    do not have None as a value '''
    if cart.answer!=None:
        return cart.answer
        # Again checks for the data types of values at each branch and compares  
    else:
        x = data_point[cart.attr_index]
        branch=None
        if isinstance(x,int) or isinstance(x,float):
            if x >= cart.compare: branch=cart.r
            else: branch=cart.l
        else:
            if x == cart.compare: branch=cart.r
            else: branch=cart.l
            # recursive classification again on the created branches. 
        return classify(data_point,branch)

