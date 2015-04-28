import numpy as np
import pandas as pd
import os
import csv
import treepredict as tp

sc_file = pd.read_csv('sc.csv')

sc_df = pd.DataFrame(sc_file)

#print(sc_df)

# getting rid of missing data


