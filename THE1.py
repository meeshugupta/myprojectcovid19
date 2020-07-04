#!/usr/bin/env python
# coding: utf-8

# In[1]:


state_names=["Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadar Nagar Haveli","Dadar Nagar Haveli and Daman and Diu","Daman & Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]       #state wise list


# In[2]:


states_infected=[8,81,0,0,32,0,50,25,0,0,0,352,9,256,111,21,95,0,405,1091,162,105,1111,5,0,4,0,23,11,231,296,0,138,0,246,0,0,462,35,71]              #state wise list of infected


# In[3]:


tuple_states_recovered=(2406,172711,673,85791,168614,0,12453,37314,14,721,0,1010544,6940,705970,172637,13605,107930,38313,166272,66566,7847,337131,2223864,7005,1187,693,2843,111741,4214,117984,431649,562,1103994,93926,50222,20728,0,393201,41613,246391)    #state wise recovered with tuple


# In[4]:


tuple_states_recovered.sort() # see in tuple are immutable 


# In[5]:


state_dictionary={"Andaman and Nicobar Islands":8,"Andhra Pradesh":81,"Arunachal Pradesh":0,"Assam":0,"Bihar":32,"Chandigarh":50,"Chhattisgarh":25,"Dadar Nagar Haveli":0,"Dadar Nagar Haveli and Daman and Diu":0,"Daman & Diu":0,"Delhi":352,"Goa":9,"Gujarat":256,"Haryana":111,"Himachal Pradesh":21,"Jammu and Kashmir":95,"Jharkhand":0,"Karnataka":405,"Kerala":1091,"Ladakh":162,"Madhya Pradesh":105,"Maharashtra":1111,"Manipur":5,"Meghalaya":0,"Mizoram":4,"Nagaland":0,"Odisha":23,"Puducherry":11,"Punjab":231,"Rajasthan":296,"Sikkim":0,"Tamil Nadu":138,"Telangana":0,"Tripura":0,"Uttar Pradesh":462,"Uttarakhand":35,"West Bengal":71}   # dictionary state wise infected 


# In[6]:


state_dictionary.keys()


# In[9]:


state_dictionary.items()


# In[8]:


state_dictionary.values()


# In[10]:


state_names.sort()


# In[11]:


print(state_names)


# In[12]:


print("sorted state_names:",state_names)


# In[ ]:




