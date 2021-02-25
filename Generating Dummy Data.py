#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install Faker


# In[24]:


# pip install PyMySQL


# In[8]:


from sqlalchemy import create_engine
import pymysql


# In[2]:


from faker import Faker 
import json            # To create a json file                 
import numpy as np
import datetime
import pandas as pd
import random


# In[3]:


fake = Faker() 


# In[14]:


def create_data(x): 
  
    # dictionary 
    ecommerce_data ={} 
    for i in range(0, x): 
        ecommerce_data[i]={} 
        ecommerce_data[i]['Order No.']= i+1 
        products=['Duvet Cover','Colverts & Quilts','Flat Sheets','Pillow Cases','Candles & Home Fragrances','Serveware','Dog Beds','Bath Rugh and Tub Mats','Towels','Throws','Frames','Scarves']
        ecommerce_data[i]['Product_name']= random.choice(products) 
        start_date = datetime.date(year=2020, month=1, day=1)
        end_date=datetime.date(year=2020, month=12, day=31)
        ecommerce_data[i]['Date']= fake.date_between(start_date=start_date, end_date=end_date) 
        ecommerce_data[i]['Price']= fake.random_int(min=1600,max=3000)
        ecommerce_data[i]['Shipping Cost'] = fake.random_int(min=10,max=100)
        ecommerce_data[i]['Cost'] = fake.random_int(min=50,max=1500)
        
        state_name = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
        ecommerce_data[i]['State']=random.choice(state_name)
        
    return ecommerce_data


# In[29]:


ecommerce_data = create_data(3000)
ecommerce_df=pd.DataFrame.from_dict(ecommerce_data).T


# In[30]:


ecommerce_df.head(20)


# In[27]:


ecommerce_df.info


# ### Connecting with MySQL DB

# In[16]:


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root')


# In[17]:


my_cursor = connection.cursor()


# In[18]:


# my_cursor.execute("CREATE DATABASE ecommerce_database")


# In[19]:


engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="root",
                               db="ecommerce_database"))


# In[20]:


ecommerce_df.to_sql('ecommerce_table', con = engine, if_exists = 'replace', chunksize = 3000)


# In[ ]:




