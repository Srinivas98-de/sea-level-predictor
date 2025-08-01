#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


# In[18]:


df = pd.read_csv(r'c:/users/srinivas/Data_Analysis_Project 5/epa-sea-level.csv')


# In[19]:


df


# In[20]:


df = df[df['CSIRO Adjusted Sea Level'].notna()]
df = df[['Year', 'CSIRO Adjusted Sea Level']]
df.head()


# In[22]:


draw_plot()
    
df = pd.read_csv('epa-sea-level.csv')

    #scatter plot
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    #first line of best fit 
res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
x_all = np.arange(df['Year'].min(), 2051)
y_all = res_all.intercept + res_all.slope * x_all
plt.plot(x_all, y_all, 'r', label='Fit: All Data')

    #second line of best fit (from year 2000 onward)
df_2000 = df[df['Year'] >= 2000]
res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
x_2000 = np.arange(2000, 2051)
y_2000 = res_2000.intercept + res_2000.slope * x_2000
plt.plot(x_2000, y_2000, 'g', label='Fit: 2000 onwards')

    #labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

    #return data for testing 
plt.savefig('sea_level_plot.png')


# In[ ]:





# In[ ]:




