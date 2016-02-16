
import glob, os
import pandas as pd

theFiles = glob.glob('data/*.csv')
#print theFiles

df_list = []

for i in theFiles:
    df = pd.read_csv(i)
    
    #print df.head(10)
    df = df.T
    df.columns = ['error_rate']
    df['date'] = i.replace('data/output','').replace('.csv','')
    df['samp'] = df.index
    
    #print df.head(10)
#     for i in df.columns:
#         print  i
    
    df_list.append(df)

df = pd.concat(df_list)
 
print df.head(5) 


df['count'] = 1

dfg = df.groupby(['samp'],as_index=False).sum()

dfg['error_rate'] = dfg['error_rate'] / dfg['count']

print dfg.head(10)

dfgby = df.groupby(['samp']).std()
                   
dfgby.head(10)


#%matplotlib inline

#!/usr/bin/env python
import numpy as np

import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = dfg['samp']
y = dfg['error_rate']

theError = dfgby['error_rate']

# First illustrate basic pyplot interface, using defaults where possible.
plt.figure()
plt.errorbar(x, y, yerr=theError)#, xerr=0.2)
plt.title("Error Rate for 1-nearest neighbor classifier with Euclidean distance")
plt.ylim(ymax=0.13)
plt.xlim(xmin=0, xmax=9000)

plt.show()