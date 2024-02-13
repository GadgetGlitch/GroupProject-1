#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Code for widgets from https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Layout.html
#This program obtains a list of assignments from a csv file and reproduces the information in a go-table format.
#It also has two interactive widgets from ipywidgets that are used to mark one or more assignments as complete.

import plotly.graph_objects as go
import pandas as pd
import ipywidgets as widgets
import datetime


# In[2]:


#Function for predeadline


# In[3]:


#Read csv data and data to a new column titled 'Colors'
df = pd.read_csv('GP1 Dataset_ Assignments_PreDeadline.csv')

#Add a column for determining font color
df['Colors'] = 'nil'
for index,row in df.iterrows():
    if row['DONE'] == 'Y':
        df.at[index,'Colors'] = 'red'
    else:
        df.at[index,'Colors'] = 'black'
        
#Add a column for determining background color and fontsize
df['Background'] = 'white'
df['Fontsize'] = 11

#Create a list of Assignments to be used a list source for the drop down list widget
a_list = list(df['ASSIGNMENT NAME'])
a_list.insert(0,'None')

#Pressing the button marks an assginment as complete
button = widgets.Button(description="Mark As Complete")
text = widgets.Dropdown(
    options=a_list,
    value=a_list[0],
    description='Assignment Name:',
    disabled=False,
)

#define the outputs
output = widgets.Output()

#Define actions to be performed on button click
#@output.capture()
def on_button_clicked(b):
    with output:
        output.clear_output()
        a_name = text.value #obtain value of the drop down list
        
        if a_name == 'None':
            
            
            df.sort_values(by=['DONE', 'DATE'], inplace=True, ascending=[True,True])
            df.reset_index(drop=True, inplace=True)
            next_date = df.at[0,'DATE']
            
            df.at[0,'Background'] = 'yellow'
            df.at[0,'Fontsize'] = 14
            
            for i in [1,2]:
                if df.at[i,'DATE'] == next_date:
                    df.at[i,'Background'] = 'yellow'
                    df.at[i,'Fontsize'] = 14
        
        if a_name != 'None': #if value is 'None', no action is taken
            
            # identify the relevant assignment from database.
            #It is assumed here that there are no duplicate assignment names
            index_req = df.index[df['ASSIGNMENT NAME'] == a_name].to_list() 
            
            #Mark the identified assignment as complete and sort the table based on Status followed by Date.
            df.at[index_req[0],'DONE'] = 'Y'
            df.at[index_req[0],'Colors'] = 'red'
            df.at[index_req[0],'Background'] = 'white' #reset background
            df.at[index_req[0],'Fontsize'] = 11 #reset fontsize
            
            df.sort_values(by=['DONE', 'DATE'], inplace=True, ascending=[True,True])
            
            #show the upcoming assignments in yellow background and larger font
            #select assignments having the same dates. Select max. upto 3 assignments
            next_date = df.at[index_req[0]+1,'DATE']
            df.at[index_req[0]+1,'Background'] = 'yellow'
            df.at[index_req[0]+1,'Fontsize'] = 14
            
            for i in [2,3]:
                if df.at[index_req[0]+i,'DATE'] == next_date:
                    df.at[index_req[0]+i,'Background'] = 'yellow'
                    df.at[index_req[0]+i,'Fontsize'] = 14
            
            
        #update drop down list
        a_list = list(df['ASSIGNMENT NAME'])
        a_list.insert(0,'None')
        text.options = a_list
        
        #write the updated database to a csv file
        df.to_csv('GP1 Dataset_ Assignments_PreDeadline.csv',columns=['DATE','PREDEADLINE','WK#','COURSE','ASSIGNMENT NAME','DESCRIPTION','DONE'])
        
        #define the go-table
        fig = go.Figure(data=[go.Table(header=dict(
        values=["Date", "Predeadline","Week Number","Course","Assignment Name","Description","Done"],
        line_color='white', fill_color='white',
        align='center', font=dict(color='blue', size=14)
        ),
        cells=dict(
        values=[df['DATE'],df['PREDEADLINE'],df['WK#'],df['COURSE'],df['ASSIGNMENT NAME'],df['DESCRIPTION'],df['DONE']],
        #line_color=[df.Colors], 
        fill_color=[df.Background],
        align='center', font=dict(color= [df.Colors], size=11)
         ))
        ])
        
        #show the go-table
        fig.update_layout(width=1050, height=1000)
        fig.show()
        


button.on_click(on_button_clicked)
list_button = widgets.HBox([text,button])
print("To initiate, select 'None' from the dropdown list and press the button 'Mark As Complete'")
widgets.VBox([list_button,output])

