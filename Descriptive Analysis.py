#!/usr/bin/env python
# coding: utf-8

# In[48]:


#import all the required libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

income_df= pd.read_csv('Inc_Exp_Data.csv')


# In[49]:


#find the first 5 rows

income_df.head()


# In[50]:


#find the total row and columns

income_df.shape


# In[51]:


#analyse the data
income_df.info()


# In[52]:


income_df.describe().T


# In[53]:


income_df.isna().any()


# In[54]:


#what is the average household monthly expense

income_df['Mthly_HH_Expense'].mean()


# In[55]:


#what is the median household monthly expense
income_df["Mthly_HH_Expense"].median()


# In[56]:


#What is the Monthly Expense for most of the Households?
income_df["Mthly_HH_Expense"].mode()


# In[57]:


#Plot the Histogram to count the Highest qualified member
income_df["Highest_Qualified_Member"].value_counts().plot(kind="bar")


# In[58]:


#Calculate IQR(difference between 75% and 25% quartile)
income_df.plot(x="Mthly_HH_Income",y="Mthly_HH_Expense")

IQR= income_df['Mthly_HH_Expense'].quantile(0.75)-income_df['Mthly_HH_Expense'].quantile(0.25)
IQR


# In[64]:


#Calculate Standard Deviation for first 4 columns
pd.DataFrame(income_df.iloc[:,0:5].std().to_frame())


# In[69]:


#Calculate Variance for first 3 columns
pd.DataFrame(income_df.iloc[:,0:4].var()).T


# In[78]:


#Calculate the count of Highest qualified member
income_df["Highest_Qualified_Member"].value_counts().T.to_frame()


# In[80]:


#Plot the Histogram to count the No_of_Earning_Members
income_df["No_of_Earning_Members"].value_counts().plot(kind='bar')


# In[81]:


#Suppose you have option to invest in Stock A or Stock B. The stocks • have different expected returns and standard deviations. The expected return of Stock A is 15% and Stock B is 10%. Standard Deviation of the returns of these stocks is 10% and 5% respectively.

cv=10/15
cv


# In[82]:


CV=5/10
CV


# In[ ]:




