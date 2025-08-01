#!/usr/bin/env python
# coding: utf-8

# In[10]:


import importlib
import sea_level_predictor  # or your exact filename, no `.py`

importlib.reload(sea_level_predictor)


# In[12]:


import unittest
unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[13]:


import os
os.listdir()


# In[14]:


import unittest
import test_module

suite = unittest.TestLoader().loadTestsFromModule(test_module)
unittest.TextTestRunner(verbosity=2).run(suite)


# In[ ]:




