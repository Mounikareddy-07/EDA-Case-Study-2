#!/usr/bin/env python
# coding: utf-8

# In[ ]:


dataset : https://drive.google.com/file/d/1WS9bWjqJw1aid5euZyfF7BW_rul8Zjvv/view


# In[2]:


# Importing the standard libraries

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv("vgsales.csv")


# In[5]:


# no of rows and columns in a dataset
df.shape


# In[6]:


# print names of all the columns
df.columns


# In[ ]:


--> This dataset has been collected from vgchartz.com and combined into one dataset.
--> This data was automatically collected from many places/websites using web scraping techniques.
    And all collected data was organized into one table or data set.
--> This dataset is probably about video games,including details like:
    * game name
    * platform
    * genre 
    * publisher
    * sales
    * release year, etc.
--> In data analysis project this description tells us "where the data came from and how it was collected".


# In[8]:


# print sample 10 rows from data
df.sample(10, random_state = 5)
# here, the number (5) usually doesn't have a special meaning. it just acts like a SEED to control randomness.
# and here, random_state is used to get the same output everytime you run the code.


# In[9]:


df.head()


# In[ ]:


--> The meaning of each column in the dataset.
    This is called a data dictionary or column description.
--> Here's the meaning in simple words:

1. Rank           Position of the game based on global sales
2. Name           Name/title of the video game
3. Platform       Gaming console used to play the game
4. Year           Release year of the game
5. Genre          Type/category of game. (action,sports,racing,etc.)
6. Publisher      Company that published the game
7. NA_Sales       Sales in North America
8. EU_Sales       Sales in Europe
9. JP_Sales       Sales in Japan
10. Other_Sales   Sales in remaining countries
11. Global_Sales  Total worldwide sales


# In[10]:


df.info()


# In[11]:


# Check for duplicate values
df.duplicated().sum()


# In[12]:


# Check for null values
df.isnull().sum()


# In[15]:


# Checks each row in the year column
# TRUE -> Year is MISSING
# FALSE -> Year exists
df["Year"].isna()


# In[14]:


# it returns only the rows where the year column has missing values.
df[df["Year"].isna()]


# In[16]:


# fill the null values with 0 which indicates that the value is actually missing
# year . it is integer col so we can fill with 0
df["Year"] = df["Year"].fillna(0)


# In[17]:


df.isnull().sum()


# In[18]:


df["Publisher"] = df["Publisher"].fillna("Unknown")
# There were already some Values with Unknown publisher
# so to maintain the consistency we have replaced the rest of null values
# as well with Unknown . because the publisher column is a object type column.


# In[19]:


df.isnull().sum()


# In[20]:


df.info()


# In[ ]:


Different ways to change data types in pandas
_____________________________________________

1. astype() --> Used to convert a column from one data type to another data type.
                we just need to be sure that the values inside the column are convertible. else it will raise an error
2. pd.to_numeric() --> used specifically to convert values into numeric data type ( int or float)
                       if the values present inside the column are int then the the col will be converted into int else float.


# In[ ]:


--> " " --> can't be directly converted into integer
--> to_numeric is having a parameter known as errors = 'coerce' which can handle such noise string Values
--> it will convert them to NAN values


# In[21]:


df["Year"] = df["Year"].astype(int)


# In[22]:


df['Year']


# In[23]:


df['Year'].value_counts()


# In[ ]:


# Check if for 2020 is the data not collected properly or actually there were less releases.


# In[ ]:


# dropna --> drop NaN
# df.drop(index, inplace = True)
# inplace = True means to make the changes in original dataset.


# In[24]:


index_to_drop = df[df['Year'] == 2020].index
print(index_to_drop)


# In[28]:


df.drop(index_to_drop, inplace = True)


# In[29]:


df['Year'].value_counts()


# In[30]:


df['Year']


# In[31]:


# This returns all rows where the YEAR value is != 0. i.e, Rows having year = 0 are removed. Remaining rows are shown
df[df['Year'] != 0]


# In[33]:


# This does 2 things. filter rows where year != 0.and select only the year column.
df[df['Year'] != 0]['Year']


# In[34]:


# find the minimum year value
df[df['Year'] != 0]['Year'].min()


# In[ ]:


--> we have got the data from 1980 to 2017


# In[35]:


# How many unique platforms and publishers we are having?
df['Platform'].nunique()


# In[36]:


df['Publisher'].nunique()


# In[37]:


# Which platform and publisher had the earliest and the latest release as per our data?
earliest = df[df['Year'] == 1980]
print(earliest)


# In[38]:


earliest['Platform'].nunique()


# In[39]:


earliest['Platform'].unique()


# In[40]:


earliest['Publisher'].nunique()


# In[41]:


earliest['Publisher'].unique()


# In[43]:


latest = df[df['Year'] == 2017]
print(latest)


# In[44]:


# Which is the platform with most game releases?
df['Platform'].value_counts().idxmax()


# In[45]:


# Which publisher has made the most games?
df['Publisher'].value_counts().idxmax()


# In[47]:


# Which are the top 10 best-selling games globally?
top_games = df.sort_values("Global_Sales", ascending = False).head(10)
print(top_games)


# In[51]:


plt.figure(figsize = (8,6))
sns.barplot(x="Global_Sales", y="Name", data=top_games)
plt.title("Top 10 best selling games Globally")
plt.show()


# In[52]:


# Which genre is most popular globally?
genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending = False)
print(genre_sales)


# In[54]:


type(genre_sales)


# In[53]:


plt.figure(figsize = (8,6))
sns.barplot(x=genre_sales.values, y= genre_sales.index)
plt.title("Most popular genres as per the Global Sales")
plt.show()


# In[55]:


# Which publisher has the highest Global sales?
publisher_sales = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False)
print(publisher_sales)


# In[57]:


top_publisher_sales = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10)
print(top_publisher_sales)


# In[60]:


plt.figure(figsize = (8,6))
sns.barplot(x = top_publisher_sales.values, y=top_publisher_sales.index)
plt.title("Top 10 publishers as per the Global_Sales")
plt.show()


# In[ ]:


Create a column by adding all the sales of you na,eu,jp and other sales and compare it with global sales
get_ipython().run_line_magic('pinfo', 'values')

---
np.allclose(1.00034, 1.000367) -- True
- deep copy and shallow copy (view)-- flatten and ravel numpy


# In[61]:


# Which region contributes most to global sales?
region_sales  = df[["NA_Sales","EU_Sales","JP_Sales","Other_Sales"]].sum()
print(region_sales)


# In[63]:


import plotly.express as px
fig = px.pie(values = region_sales.values, names =region_sales.index, title = "Sales distribution by region" )
fig.show()


# In[ ]:


--> trend analysis -- line chart -- time(year)


# In[ ]:


# Chart that shows the trend of global over the time period.


# In[64]:


df1 = df[df['Year'] != 0]


# In[65]:


yearly_sales = df1.groupby('Year')['Global_Sales'].sum().reset_index()
yearly_sales


# In[66]:


fig = px.line(
    yearly_sales,
    x = 'Year',
    y='Global_Sales',
    title = 'Yearly Sales Trend',
    markers = True
)

fig.show()

