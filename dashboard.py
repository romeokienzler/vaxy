#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd



df = pd.read_csv('data.csv')


# In[ ]:


df


# In[ ]:


st.bar_chart(df)


# In[ ]:


#!jupyter nbconvert dashboard.ipynb --to python --output dashboard.py


# In[ ]:


#!streamlit run dashboard.py


# In[ ]:




