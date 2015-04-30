# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:44:12 2015

@author: You-Myeong
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
        
"""
response = variable that we are trying to test for
value = the value that the category has to match to get a true 
"""
class decisionnode:
  def __init__(self,col= -1,value=None,results=None,tb=None,fb=None):
    self.col=col
    self.value=value
    self.results=results
    self.tb=tb
    self.fb=fb
    
    
def divideset(rows,column,value):
    # Make a function that tells us if a row is in 
    # the first group (true) or the second group (false)
    set1 = []
    set2 = [] 
    if isinstance(value,int) or isinstance(value,float):
        for row in rows: 
            if row[column] >= value:
                set1.append(row)
            else:
                set2.append(row)
        return(set1,set2)
    else:
        for row in rows:
            if row[column] == value:
                set1.append(row)
            else:
                set2.append(row)
        return(set1,set2)

#calculate the proportions of end results so we can do calculations.
def uniquecounts(rows):
   results={}
   for row in rows:
      # The result is the last column
      r=row[len(row)-1]
      if r not in results: results[r]=0
      results[r]+=1
   return results 

def proportions(rows):
    total = len(rows)
    counts = uniquecounts(rows)
    p = []
    for keys in counts:
        p1 = float(counts[keys])/total
        p.append(p1)
    return p
    
def giniimpurity(rows): 
    p = proportions(rows)
    return 1 - sum([i**2 for i in p])
    
def entropy(rows): 
    #p here is the list of frequencies
    p = proportions(rows)
    from math import log 
    return sum([(-i * log(i,2)) for i in p])

'''
my_datas = np.array(my_data)

def divider(rows):
    # there are 1 less than number of column number of variables to be tested
   

'''

  
def buildtree(rows):
    if len(rows)==0: return decisionnode()
    current_score=entropy(rows)
#convert to numpy array for this only 

    my_datas = np.array(my_data)
    best_gain = 0.0
    best_criteria = None
    best_sets = None
    column_count = len(rows[0])-1
    for col in range(0,column_count):
      # take on all the values in this column
        values = my_datas[:,col]
        print values 
        for value in values:
            (set1,set2) = divideset(rows,col,value)
            #calculate information gains and update it
            print set1
            p = float(len(set1))/len(rows)
            gain = current_score - p*entropy(set1) - (1-p)*entropy(set2)
            if gain > best_gain and len(set1)>0 and len(set2)>0:
                best_gain = gain
                best_criteria=(col,value)
                best_sets = (set1,set2)
                #recursively create tree
        if best_gain>0:
            trueBranch = buildtree(best_sets[0])
            falseBranch = buildtree(best_sets[1])
            return decisionnode(col=best_criteria[0], value=best_criteria[1],tb=trueBranch,fb=falseBranch)
        else:
            return decisionnode(results=uniquecounts(rows))
       
         
         
'''
        
def information gain        
        
        
#change build tree     
def buildtree(rows,scoref=entropy):
  if len(rows)==0: return decisionnode()
  current_score=scoref(rows)

  # Set up some variables to track the best criteria
  best_gain=0.0
  best_criteria=None
  best_sets=None
  my_datas = np.array(my_data)  
  
  column_count = len(rows[0])-1
  for col in range(0,column_count):
     # take on all the values in this column
     values = my_datas[:,col]
     for value in values:
         (set1,set2) = divideset(rows,col,value)
      
      # Information gain
  p=float(len(set1))/len(rows)
  gain=current_score-p*scoref(set1)-(1-p)*scoref(set2)
  if gain>best_gain and len(set1)>0 and len(set2)>0:
      best_gain=gain
      best_criteria=(col,value)
      best_sets=(set1,set2)
  # Create the sub branches   
  if best_gain>0:
      trueBranch=buildtree(best_sets[0])
      falseBranch=buildtree(best_sets[1])
      return decisionnode(col=best_criteria[0],value=best_criteria[1],
                        tb=trueBranch,fb=falseBranch)
  else:
      return decisionnode(results=uniquecounts(rows))

    
          
# def classify (observation,tree):            
'''




