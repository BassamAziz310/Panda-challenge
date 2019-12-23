#!/usr/bin/env python
# coding: utf-8

# In[191]:


import pandas as pd
import numpy as np


# In[192]:


csv_path = ("Resources/purchase_data.csv")
read_csv = pd.read_csv(csv_path)


# In[193]:


df = pd.DataFrame(read_csv)


# In[194]:


df.head()


# In[ ]:






# In[195]:


count_list = df["SN"].value_counts()


# In[196]:


count_list.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[216]:


print("Total Number of Users: ")

total_players = df['SN'].nunique()

print(total_players)


# In[198]:


#print("Number of Unique Items: ")

unique_items = df['Item Name'].nunique()


# In[199]:


#print("Average purchase price: ")

purchase_price = df['Price'].mean()

#print(purchase_price)


# In[200]:


#print("Total number of purchases: ")

df['Item Name'].count()


# In[201]:


#print("Total Revenue: ")

total_revenue = df['Price'].sum()

#print(total_revenue)


# In[202]:


gender_count = df.groupby(['Gender']).count() 

gender_count.head()

del gender_count['Price'] 

del gender_count['Item Name']

del gender_count['Item ID']

del gender_count['Age']

del gender_count['SN']

gender_count.head()


# In[217]:


male_percentage = 484/576*100


# In[218]:


female_percentage = 81/576*100


# In[219]:


other_percentage = 11/576*100


# In[220]:


gender_dict = [{"Percentage": male_percentage, "Gender ": "Male"}, 
               {"Percentage": female_percentage, "Gender ": "Female"},
               {"Percentage": other_percentage, "Gender ": "Other"},
              ]

df_gender = pd.DataFrame(gender_dict)
df_gender


# In[207]:


#I need to adjust the count by user


# In[208]:


gender_dict = [{"Number of Unique Items": unique_items, "Average Purchase Price ": "$" + str(purchase_price), "Total Revenue ": "$" + str(total_revenue) }]

df_gender = pd.DataFrame(gender_dict)
df_gender


# In[209]:


df.describe()


# In[210]:


#creating bins

bins = [0, 10, 14, 19, 24, 29, 34, 39, 40]

#creating labels

group_names = ['<10', '10-14','15-19', '20-24', '25-29', '30-34', '35-39', '40+']


# In[211]:


df["Age Ranges"] = pd.cut(df['Age'], bins, labels=group_names)

df


# In[222]:


tender_count = df.groupby(["Age Ranges"]).count()

tender_count.head()

del tender_count['Price'] 

del tender_count['SN'] 

del tender_count['Purchase ID'] 

del tender_count['Item ID'] 

del tender_count['Item Name'] 

del tender_count['Gender'] 








tender_count.head()


# In[230]:


#show me the whole thing you piece of shit what the fuck


# In[240]:


tender_count.rename(columns = {'Age':'Purchase Count'}, inplace = True)


# In[237]:


tender_count.head()


# In[242]:


#CHANNNNNNGE IT TO "PURCAHSE COUNT" PLEEEEASSSE


# In[ ]:




