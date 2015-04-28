import numpy as np
import pandas as pd
import os
import csv
#import treepredict as tp

sc_file = pd.read_csv('sc.csv')

sc_df = pd.DataFrame(sc_file)
sc_df = sc_df[['pgtime', 'age', 'eet', 'g2', 'grade', 'gleason', 'ploidy', 'pgstat']]

#print(sc_df)

# getting rid of missing data


