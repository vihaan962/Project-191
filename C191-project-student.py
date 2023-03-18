#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name : ")
print("This is a CSV of more than 200 rows which has Covide data.")
print("The task is to find out top 5 the countries who are least affected by covid")
print("Another task is to find out top 5 the countries who has the maximum number of deaths")
print("Another task is to find out top 5 the countries who has the maximum number of active cases")


# In[3]:


#Covide Data 
import  numpy as np
import pandas as pd
from matplotlib import pyplot as plt


dataframe = pd.read_csv('covid19.csv')
df = dataframe.dropna()
sorted_df = df.sort_values(by=['total_cases'])
sorted_df


# In[10]:


#Task 1 
#Sort the data as per total number of cases
lowest_cases = sorted_df['total_cases'].head(5)
lowest_country = sorted_df['country'].head(5)
print('lowest_cases')
print('lowest_country')
plt.xlabel('country')
plt.xticks(rotation="vertical")
plt.ylabel('Number of cases')
plt.bar(lowest_country,lowest_cases,width = 0.4,color=("red","cyan","yellow","blue","brown"))


# In[4]:


#Task 2
#Get top 5 countries who has the least number of cases and plot a bar graph
sorted_deaths = df.sort_values(by=['total_deaths'])
sorted_deaths


# In[11]:


#Task 3
#Sort the data as per total number of deaths
highest_deaths = sorted_deaths['total_cases'].head(5)
highest_deaths_country = sorted_deaths['country'].head(5)
print('highest_deaths')
print('highest_deaths_country')
plt.xlabel('country')
plt.xticks(rotation="vertical")
plt.ylabel('Number of cases')
plt.bar(highest_deaths_country,highest_deaths,width = 0.4,color=("red","cyan","yellow","blue","brown"))


# In[5]:


#Task 4
#Get top 5 countries who has the maximum number of deaths and plot a bar graph

sorted_cases = df.sort_values(by=['active_cases'])
sorted_cases


# In[13]:


#Task 5
#Sort the data as per active cases
highest_active_cases = sorted_deaths['active_cases'].head(5)
highest_active_country = sorted_deaths['country'].head(5)
print('highest_active_cases')
print('highest_active_cases_country')
plt.xlabel('country')
plt.xticks(rotation="vertical")
plt.ylabel('Number of cases')
plt.bar(highest_active_country,highest_active_cases,width = 0.4,color=("red","cyan","yellow","blue","brown"))


# In[6]:


#Task 6
#Get top 5 countries who has the maximum number of active cases and plot a bar graph


# In[ ]:





# In[ ]:




