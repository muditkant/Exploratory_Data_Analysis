#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import os 
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


# In[109]:


#merging all the csv files into 1 file


# In[227]:


path = "/Users/muditkant/Desktop/Machine Learning/problem solving/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data"
files = [file for file in os.listdir(path) if not file.startswith('.')] # Ignore hidden files

all_months_data = pd.DataFrame()

for file in files:
    current_data = pd.read_csv(path+"/"+file)
    all_months_data = pd.concat([all_months_data, current_data])
    
all_months_data.to_csv("all_data1.csv", index=False)


# In[228]:


df = pd.read_csv("/Users/muditkant/Downloads/Pandas-Data-Science-Tasks-master/SalesAnalysis/Output/all_data.csv")
df.head()


# In[229]:


#checking for null values


# In[230]:


df.isnull().values.any()


# In[231]:


df = df.dropna()


# In[232]:


#checking for null values


# In[233]:


df.isnull().values.any()


# In[234]:


temp = df[df["Order Date"].str[:2] == "Or"]
temp.head()


# In[235]:


#order date consits of gibberish data
#removing gibberish values


# In[236]:


df = df[df["Order Date"].str[:2] != "Or"]
df.head()


# In[237]:


df["Month"] = df["Order Date"].str[:2]
df.head()


# In[238]:


#converting month values into int


# In[239]:


df["Month"] = df["Month"].astype('int32')
df.head()


# In[240]:


## Q1: Sales associated with each order


# In[241]:


#converting Quantity Ordered and Price Each into numeric int 


# In[242]:


df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"])
df["Price Each"] = pd.to_numeric(df["Price Each"])


# In[243]:


df["Sales"] = df["Quantity Ordered"] * df["Price Each"]
df.head()


# In[246]:


#Best month for sales and revenue generated


# In[247]:


graph = df.groupby("Month").sum()
graph


# In[248]:


#visualizing using matplotlib


# In[267]:


months = range(1,13)
plt.bar(months,graph["Sales"])
plt.xticks(months)
plt.ylabel('Sales in $ ->')
plt.xlabel("Months ->")
plt.show()


# In[268]:


#Which city has best sales


# In[280]:


df.head()


# In[281]:


#Making seperate column for city and extracting value


# In[295]:


def state(address):
    return address.split(",")[2].split(" ")[1]
    
df["City"] = df["Purchase Address"].apply(lambda x: x.split(',')[1] + " " + state(x))


# In[318]:


df.head()


# In[319]:


#Q2: Best sales in which city


# In[320]:


result = df.groupby("City").sum()
result


# In[312]:


#visualizing using matplotlib


# In[333]:


cities = df['City'].unique()
plt.bar(cities,result["Sales"])
plt.xticks(cities,rotation = "vertical")
plt.ylabel('Sales in $ ->')
plt.xlabel("name ->")
plt.show()


# In[334]:


# In city colums it shows San Francisco CA bes sales
# While in visulalization it shows, austin TX


# In[335]:


## Need to search why this happened.


# In[336]:


## X data and Y data needs to be in same order. That's why it's causing 


# In[344]:


cities = [city for city, df in df.groupby(['City'])]
plt.bar(cities,result["Sales"])
plt.xticks(cities,rotation = "vertical")
plt.ylabel('Sales in $ ->')
plt.xlabel("name ->")
plt.show()


# In[345]:


#Q3: Best Time for advertisements.


# In[346]:


df.head()


# In[361]:


df["Order Date"] = pd.to_datetime(df["Order Date"])


# In[366]:


df["Hour"] = df["Order Date"].dt.hour
df["Minutes"] = df["Order Date"].dt.minute
df.head()


# In[364]:


#visualizing using matplotlib


# In[374]:


Hour = [Hour for Hour, df in df.groupby(['Hour'])]
plt.plot(Hour, df.groupby(['Hour']).count())
plt.xticks(Hour)
plt.xlabel("24 hr when order's are placed - hours")
plt.ylabel("Order's placed")
plt.grid()
plt.show()


# In[375]:


#delivering advertisements just before Peak hours of sale: 11 - 12 & 18 - 19 hrs


# In[376]:


#Q4: What are the most often products sold in a groupof 2 or 3? 


# In[383]:


df.head(20)


# In[384]:


#Order's have duplicate order ID:


# In[387]:


df = df[df['Order ID'].duplicated(keep=False)]
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df2 = df[['Order ID', 'Grouped']].drop_duplicates()


# In[388]:


from itertools import combinations
from collections import Counter


# In[393]:


count = Counter()

for row in df2['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 1)))

for key,value in count.most_common(10):
    print(key, value)


# In[392]:


# Q5: What product was sold the most and why


# In[394]:


product_group = df.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

keys = [pair for pair, df in product_group]
plt.bar(keys, quantity_ordered)
plt.xticks(keys, rotation='vertical', size=8)
plt.show()


# In[399]:


prices = df.groupby('Product').mean()['Price Each']
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(keys, quantity_ordered, color='g')
ax2.plot(keys, prices, color='b')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered')
ax2.set_ylabel('Price ($)')
ax1.set_xticklabels(keys, rotation='vertical',)

fig.show()


# In[ ]:




