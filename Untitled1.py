#!/usr/bin/env python
# coding: utf-8

# In[186]:


import pandas as pd
import numpy as np
import math


# In[254]:


def valextract(x):
#     x[1] = x[1].replace(",","")
#     return (((int(x[0])*1000) + (int(x[1])))//2)
    return x[0]


# In[255]:


data = pd.read_csv(r'C:\Users\UMA1017\Desktop\MSTask\multipleChoiceResponses.csv')


# In[256]:


def clean_income(value):
    if value == "Prefer not to answer":
        return np.nan
    elif isinstance(value, float) and math.isnan(value):
        return np.nan
    elif value != 'NaN':
        l,u = value.split("-")
        return valextract(l)


# In[257]:


data['inc'] = data['Q9'].apply(clean_income)
data['inc']


# In[169]:


a = "10-20,000"
valextract(a)


# In[261]:


c,b = a.split("-")
b = b.replace(",","")
int(((int(c) * 1000) + int(b))//2)

