#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


# In[ ]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'


# In[ ]:


df = pd.read_csv(url, sep = '\t',low_memory = False)
df.head()


# In[ ]:


# print total records and type of variables


# In[ ]:


df.info()


# In[ ]:


#Q1: Which was the most ordered item? and How many items were ordered?


# In[ ]:


c = df.groupby("item_name").sum()
c = c.sort_values(["quantity"], ascending = False)
c.head()


# In[ ]:


#Q2: What was the most ordered item in the choice_description column?


# In[ ]:


df = df.groupby("choice_description").sum()
df = df.sort_values(["quantity"], ascending = False)
df.head(1)


# In[ ]:


#Q3: Turn the item price into a float


# In[ ]:


dollar = lambda x: float(x[1:-1])
df.item_price = df.item_price.apply(dollar)


# In[ ]:


df.head()


# In[ ]:


#Q3: How much was the revenue for the period in the dataset?


# In[ ]:


revenue = (df['quantity']* df['item_price']).sum()
print('Revenue was: ' + str(np.round(revenue,2)))


# In[ ]:


#Q4: print a data frame with only two columns item_name and item_price


# In[ ]:


df.loc[:,["item_name","item_price"]]


# In[ ]:


#Q5: delete the duplicates in item_name and quantity


# In[ ]:


filtered = df.drop_duplicates(['item_name','quantity'])
# select only the products with quantity equals to 1
one_prod = filtered[filtered.quantity == 1]
# select only the item_name and item_price columns
price_per_item = one_prod[['item_name', 'item_price']]
# sort the values from the most to more expensive
price_per_item.sort_values(by = "item_price", ascending = True)


# In[ ]:


#Q6: What was the quantity of the most expensive item ordered?


# In[ ]:


df.sort_values(["item_price"],ascending = False).head(1)


# In[ ]:


# Q7: How many times were a Veggie Salad Bowl ordered?


# In[ ]:


df = df[df.item_name == "Veggie Salad Bowl"]
count_row = df.shape[0] 
print(count_row)


# # Drinks statistics 

# In[47]:


url = "https://raw.githubusercontent.com/alcor2019/justmarkham/master/data/drinks.csv"


# In[49]:


df = pd.read_csv(url,low_memory = False)
df.head()


# In[50]:


#Q8: Which continent drinks more beer on average?


# In[51]:


x = df.groupby("continent")
x.beer_servings.mean()


# In[52]:


#Q9: For each continent print the statistics for wine consumption.


# In[53]:


df.groupby("continent").wine_servings.describe()


# In[ ]:




