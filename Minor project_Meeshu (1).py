#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib as plt
from matplotlib import pyplot as plt


# In[174]:


import matplotlib.pyplot as plt
count=["confirmed","active", "recovered","deaths"]
numbers=[102831,25449,74217,3165]
plt.plot(count,numbers)
plt.title("status_of_delhi_COVID19")
plt.ylabel("y axis")
plt.xlabel("x axis")
plt.show()


# In[175]:


import matplotlib.pyplot as plt
count=["confirmed", "active","recovered","death"]
numbers=[17700,4101,13393,276]
plt.plot(count,numbers)
plt.title("status_of_harayana_COVID19")
plt.ylabel("y axis")
plt.xlabel("x axis")
plt.show()


# In[176]:


import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

x=["confirmed", "active","recovered","death"]
y=[102831,25449,74217,3165]
x2=["confirmed", "active","recovered","death"]
y2=[17700,4101,13393,276]
plt.plot(x,y,'g',label='Delhi',linewidth=5)
plt.plot(x2,y2,'c',label='Harayana',linewidth=5)
plt.plot(count,numbers)
plt.title("status of Delhi vs Harayana COVID19")
plt.ylabel("y axis")
plt.xlabel("x axis")
plt.grid(True,color='k')
plt.legend()
plt.show()


# In[161]:


df=pd.read_csv("Delhi_june.csv")


# In[181]:


plt.plot(df['Date'],df['Confirmed'],label='Confirmed',linewidth=4)
plt.plot(df['Date'],df['Deaths'],label='Deaths',linewidth=4)
plt.plot(df['Date'],df['Cured'],label='Cured',linewidth=4)
plt.title("status_of_delhi_COVID19 as on June 2020")
plt.xticks(rotation=20)
plt.ylabel("cases")
plt.legend(loc='best')
plt.show()


# In[186]:


cases=pd.read_csv("Harayana.csv")


# In[188]:


dframe=pd.read_csv("Harayana.csv")


# In[189]:


plt.plot(dframe['Date'],dframe['Confirmed'],label='Confirmed',linewidth=4)
plt.plot(dframe['Date'],dframe['Deaths'],label='Deaths',linewidth=4)
plt.plot(dframe['Date'],dframe['Cured'],label='Cured',linewidth=4)
plt.title("status_of_harayana_COVID19 as on June 2020")
plt.xticks(rotation=20)
plt.ylabel("cases")
plt.legend(loc='best')


# In[ ]:





# In[ ]:




