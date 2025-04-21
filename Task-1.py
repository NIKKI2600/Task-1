#!/usr/bin/env python
# coding: utf-8

# import numpy as np

# In[11]:


data= pd.read_csv("C:/Users/nikhi/OneDrive/Desktop/netflix_titles.csv")
print(data)


# In[15]:


missing_values = data.isnull().sum()
print(missing_values)


# In[18]:


data.head()


# In[25]:


print("shape:", data.shape)
print("\nColumn Info:")
data.info()
print("\nMissing Values:")
print(data.isnull().sum())


# In[32]:


data =data.dropna(subset=['title'])
data['country'] = data['country'].fillna('Unkown')
data['cast'] = data['cast'].fillna('Not Specified')
data['director'] = data['director'].fillna('Not Specified')
data['rating'] = data['rating'].fillna('Not Specified')
data['date_added'] = data['date_added'].fillna('01-Jan-1900')


# In[34]:


data = data.drop_duplicates()


# In[37]:


data['type'] = data['type'].str.strip().str.lower()
data['country'] = data['country'].str.strip().str.title() 


# In[39]:


data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')


# In[41]:


data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')


# In[44]:


print(data.dtypes)


data['release_year'] = data['release_year'].astype('int')


# In[47]:


data.to_csv("C:/Users/nikhi/OneDrive/Desktop/netflix_titles.csv", index=False)

