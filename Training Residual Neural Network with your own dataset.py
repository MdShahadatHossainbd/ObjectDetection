#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install split_folders')


# In[3]:


import splitfolders


# In[5]:


input_folder = "flowers/Input"
output = "flowers/processed"
splitfolders.ratio(input_folder, output, seed=42, ratio=(.6, .2, .2 ))


# In[6]:


help(splitfolders.ratio)


# In[ ]:




