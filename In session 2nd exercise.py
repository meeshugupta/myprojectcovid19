#!/usr/bin/env python
# coding: utf-8

# In[1]:


state_list=["Jharkhand", "Maharashtra", "Kerala", "Punjab","Bihar","Rajasthan"] #state names


# In[6]:


print(state_list)


# In[14]:


state_list.sort()


# In[15]:


print("sorted state_list:",state_list) # sorted state list


# In[19]:


infected_state=[2584,186626,4753,5784,10471,18662] #state wise infected no.


# In[20]:


infected_state.sort()


# In[21]:


print("sorted infected_state:",infected_state) # sorted infected_states_cases


# In[22]:


tuple_recovered=(1983,101172,2640,4144,8020,14948) #state wise recovered case


# In[24]:


print(tuple_recovered)


# In[25]:


tuple_recovered.sort() #tuple are immutable hence no change


# In[26]:


state_dict={"Bihar":10471,"Jharkhand":2584,"kerala":4783,"Maharashtra":186626,"punjab":5784,"rajasthan":18662}


# In[28]:


state_dict.values()


# In[29]:


state_dict.keys()


# In[30]:


state_dict.items()


# In[ ]:




