
# coding: utf-8

# In[1]:


import sys
get_ipython().system('conda install --yes --prefix {sys.prefix} seaborn')


# In[2]:


import math
import numpy as np
import pandas as pd
from pandas import DataFrame
df =pd.read_csv("content_train.tsv", sep="\t",index_col='customer.id')
#print(df)
df.iloc[:,0:26]

