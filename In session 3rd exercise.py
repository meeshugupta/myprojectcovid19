#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Function to calculate Infection Fatality rate of Maharashtra
def ifr (deaths,infected):
    ifr=(deaths/infected)*100
    print("the IFR={}%" .format(ifr))


# In[20]:


ifr(8671,108082)


# In[21]:


#Function to calculate crude mortality rate of Maharashtra- as CMR based on total death divided by total population and if we do total death divided by total infected then it is IFr

def cmr (deaths, population):
    cmr=(deaths/population)*100
    print("the CMR is={}%".format(cmr))


# In[17]:


cmr(8671,112374333)


# In[ ]:




