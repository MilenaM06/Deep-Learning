#!/usr/bin/env python
# coding: utf-8

# # My First Jupiter Notebook

# <img src="https://petljamediastorage.blob.core.windows.net/root/Media/Default/Kursevi/international/jupyter-international/logo.png" width=300px>

# This tutorial will go over,
# 1) What is jupyter or ipython notebook?
# 2) Installation of jupyter notebook
# 3) Build first notebook using python pandas
# 4) Cover markdown and embedding video links
# 5) Plotting chart using matplotlib
# 6) What is line magic and cell magic and how to use them 
# 7) Export notebook as py and html file
# 
# https://www.youtube.com/watch?v=EEEZX_0FMEc&list=PLeo1K3hjS3uuZPwzACannnFSn9qHn8to8&index=3&ab_channel=codebasics

# In[33]:


get_ipython().run_cell_magic('HTML', '', '<iframe frameborder="0" scrolling="no" marginheight="0" marginwidth="0"width="800" height="443" type="text/html" src="https://www.youtube.com/embed/EEEZX_0FMEc?autoplay=0&fs=0&iv_load_policy=3&showinfo=0&rel=0&cc_load_policy=0&start=0&end=0"></iframe>\n')


# In[3]:


from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
y_symbols = ['SCHAND.NS', 'TATAPOWER.NS', 'ITC.NS']
from datetime import datetime
startdate = datetime(2022,12,1)
enddate = datetime(2022,12,15)
data = pdr.get_data_yahoo(y_symbols, start=startdate, end=enddate)
data.head()


# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
data.plot(y="Close", color = "Green")


# In[7]:


get_ipython().run_line_magic('lsmagic', '')


# In[8]:


get_ipython().run_line_magic('time?', '#tells me what can time do')


# In[9]:


get_ipython().run_line_magic('time', 'for i in range(100000): i*i')


# In[12]:


get_ipython().run_line_magic('pinfo', '%system')


# In[15]:


data.plot.bar(y="High")


# In[ ]:




