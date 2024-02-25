#!/usr/bin/env python
# coding: utf-8

# # Install necessary packages and libraries

# In[1]:


# Run the following installs only once

#!pip install geopy
#!pip install tzwhere
#!pip install timezonefinder
#!pip install pytz
#!pip install --upgrade pymupdf
#!pip install python-docx


# In[2]:


#Code for widgets from https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Layout.html
#This program obtains a list of assignments from a csv file and reproduces the information in a go-table format.
#It also has two interactive widgets from ipywidgets that are used to mark one or more assignments as complete.

# Setup and Imports
import pandas as pd
import pytz
import plotly.graph_objects as go
import pandas as pd
import ipywidgets as widgets
import datetime
import ipywidgets as widgets
#import fitz  # PyMuPDF for PDF files
#import requests
#import re  # For regular expressions
#import openpyxl  # For .xlsx files
#import xlrd  # For .xls files
#from docx import Document
#from bs4 import BeautifulSoup
#from IPython.display import display
#from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder


# # Define variables

# In[3]:


# Initialize Nominatim and TimezoneFinder
#geolocator = Nominatim(user_agent="geocity")
#tf = TimezoneFinder()


# # Define Functions

# In[4]:


#Function for timezone
def get_timezone_from_city(city):
    location = geolocator.geocode(city)
    if location:
        timezone_str = tf.timezone_at(lat=location.latitude, lng=location.longitude)
        return timezone_str
    return None

# Function to standardize city names
def standardize_city_name(city):
    city = city.lower()
    if city in ["saranda", "sarande"]:
        return "Sarandë, Albania"
    return city

#Function for predeadline
def get_predeadline(deadline, buffer_days=1):
    """Subtract buffer days from deadline date to get the pre-deadline date."""
    return deadline - datetime.timedelta(days=buffer_days)


# In[5]:


#Place holder for functions to read different file types like Document, PDF etc. 
#Issues #10 & 14


# # Load CSV and convert DATE column to datetimes

# In[6]:


#file_path = "GP1 Dataset_ Assignments.csv"
#df = pd.read_csv(file_path, encoding='ISO-8859-1')

#df['DATE'] = pd.to_datetime(df['DATE'])

#dfs = []
#timezones = set(df['TIMEZONE'])
#for i in timezones:
#    df1 = df.loc[df['TIMEZONE'] == i].copy()
#    df1['DATE'] = df['DATE'].dt.tz_localize(i)
#    df1['DATE'] = df1['DATE'] + datetime.timedelta(hours=23,minutes=59)
#    dfs.append(df1)
    
#df_merged = pd.concat([dfs[0],dfs[1]])
#df_merged.sort_index(inplace=True)
#df = df_merged


# # Ask the user for their city

# In[7]:


#user_city = standardize_city_name(input("Enter the city you are in: "))
#user_timezone = get_timezone_from_city(user_city)
#print(user_timezone)


# # Convert due dates to the user's local timezone and calculate for pre-deadline dates

# In[10]:


#if user_timezone:
#    user_tz = pytz.timezone(user_timezone)
#else:
#    user_tz = datetime.datetime.now().astimezone().tzinfo

#df['LOCAL_DUE_DATE'] = df['DATE'].apply(lambda x: x.astimezone(user_tz))
#df['PREDEADLINE'] = df['LOCAL_DUE_DATE'].apply(lambda x: get_predeadline(x))

# Define the order of the columns, including the new PREDEADLINE column
#column_order = ['ITEM#', 'COURSE', 'ASSIGNMENT NAME', 'DESCRIPTION', 'DATE', 'LOCAL_DUE_DATE', 'PREDEADLINE', 'DONE']

# Reorder the DataFrame according to the defined column order
#df = df[column_order]

# Print the DataFrame to check the results
#print(df.head())


# # Main App

# In[11]:


#Add a column for determining font color
#df['Colors'] = ['nil'] * len(df)
#for index,row in df.iterrows():
#    if row['DONE'] == 'Y':
#        df.at[index,'Colors'] = 'red' #if task is complete, turn font color 'red'
#    else:
#        df.at[index,'Colors'] = 'black' #if task is incomplete, keep font color 'black'
        
#Add a column for determining background color 
#df['Background'] = 'white'


#Create a list of Assignments to be used as list source for the drop down list widget
#a_list = list(df['ASSIGNMENT NAME'])
#a_list.insert(0,'None')

#Pressing the button marks an assginment as complete. Instantiate button and dropdown object.
#button = widgets.Button(description="Mark As Complete")
#text = widgets.Dropdown(
#    options=a_list,
#    value=a_list[0],
#    description='Assignment Name:',
#    disabled=False,
#)

#define the outputs
#output = widgets.Output()

#Define actions to be performed on button click
#def on_button_clicked(b):
#    with output:
#        output.clear_output()
#        a_name = text.value #obtain value of the drop down list
#        
#        if a_name == 'None':
#            
#            df.sort_values(by=['DONE', 'DATE'], inplace=True, ascending=[True,True])
#            df.reset_index(drop=True, inplace=True)
#            next_date = df.at[0,'DATE']
            
#            df.at[0,'Background'] = 'yellow'
            
#            for i in [1,2]:
#                if df.at[i,'DATE'] == next_date:
#                    df.at[i,'Background'] = 'yellow'
        
#        if a_name != 'None': 
            
#            # identify the relevant assignment from database.
#            #It is assumed here that there are no duplicate assignment names
#            index_req = df.index[df['ASSIGNMENT NAME'] == a_name].to_list() 
            
#            #Mark the identified assignment as complete and sort the table based on Status followed by Date.
#            df.at[index_req[0],'DONE'] = 'Y'
#            df.at[index_req[0],'Colors'] = 'red'
#            df.at[index_req[0],'Background'] = 'white' #reset background
            
#            df.sort_values(by=['DONE', 'DATE'], inplace=True, ascending=[True,True])
            
#            #show the upcoming assignments in yellow background and larger font
#            #select assignments having the same dates. Select max. upto 3 assignments
#            next_date = df.at[index_req[0]+1,'DATE']
#            df.at[index_req[0]+1,'Background'] = 'yellow'
            
#            for i in [2,3]:
#                if df.at[index_req[0]+i,'DATE'] == next_date:
#                    df.at[index_req[0]+i,'Background'] = 'yellow'
            
#        #update drop down list
#        a_list = list(df['ASSIGNMENT NAME'])
#        a_list.insert(0,'None')
#        text.options = a_list
        
#        #create a copy of df for writing it to csv file
#        df_copy_1 = df.copy()
#        df_copy_1['DATE'] = df_copy_1['DATE'].apply(lambda x: x.strftime("%m/%d/%y"))
#        
#        #write the updated database to a csv file
#        df_copy_1.to_csv('GP1 Dataset_ Assignments.csv',columns=['ITEM#','DATE','WK#','COURSE','ASSIGNMENT NAME','DESCRIPTION','DONE','TIMEZONE'])
        
#        #create a copy of df for updating go table
#        df_copy_2 = df.copy()
        
#        #Update Date and Time format
#        df_copy_2['DATE'] = df_copy_2['DATE'].apply(lambda x: x.strftime("%m/%d/%Y, %H:%M:%S"))
#        df_copy_2['LOCAL_DUE_DATE'] = df_copy_2['LOCAL_DUE_DATE'].apply(lambda x: x.strftime("%m/%d/%Y, %H:%M:%S"))
#        df_copy_2['PREDEADLINE'] = df_copy_2['PREDEADLINE'].apply(lambda x: x.strftime("%m/%d/%Y, %H:%M:%S"))
        
#        #define the go-table
#        fig = go.Figure(data=[go.Table(
        
#        columnwidth = [50,80,150,150,150,150,150,80],
        
#        header=dict(
#        values=["ITEM", "COURSE","ASSIGNMENT NAME","DESCRIPTION","DATE","LOCAL_DUE_DATE","PREDEADLINE","DONE"],
#        line_color='white', fill_color='white',
#        align='center', font=dict(color='blue', size=14)
#        ),
#        cells=dict(
#        values=[df_copy_2['ITEM#'],df_copy_2['COURSE'],df_copy_2['ASSIGNMENT NAME'],df_copy_2['DESCRIPTION'],df_copy_2['DATE'],df_copy_2['LOCAL_DUE_DATE'],df_copy_2['PREDEADLINE'],df_copy_2['DONE']],
#        #line_color=[df.Colors], 
#        fill_color=[df.Background],
#        align='left', font=dict(color= [df.Colors], size=11)
#         ))
#        ])
        
#        #show the go-table
#        fig.update_layout(width=1000, height=1000)
#        fig.show()
        
#button.on_click(on_button_clicked)
#list_button = widgets.HBox([text,button])
#print("To initiate, select 'None' from the dropdown list and press the button 'Mark As Complete'")
#widgets.VBox([list_button,output])


# In[ ]:




