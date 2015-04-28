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

print divideset(my_data,3,18)
                
          
            





