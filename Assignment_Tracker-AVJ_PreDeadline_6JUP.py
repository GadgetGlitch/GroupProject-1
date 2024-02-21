#!/usr/bin/env python
# coding: utf-8

# In[38]:
import plotly.graph_objects as go
import pandas as pd
import ipywidgets as widgets
import datetime
# In[39]:

# Only works on Annaka's Local Drive. File is located in the main branch, however. 
file_path = r"C:\Users\annak\CAS-502 Computation\GroupProject-1\GP1 Dataset_ Assignments.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')  

print(df.head()) #Print the tops of the headers of the table to see its original table set up

# In[40]:

# Function to calculate pre-deadline date
def get_predeadline(deadline, buffer_days=1):
    
    # Subtract buffer days from deadline date 
    predeadline = deadline - datetime.timedelta(days=buffer_days)  
    
    # Return predeadline date 
    return predeadline

# Takes dates of assignments and subtracts a day for a preDeadline date # Proof of Concept by one date
deadline = datetime.date(2023, 2, 15)  
predeadline = get_predeadline(deadline, buffer_days=1) 

print(predeadline) # 2023-02-13 

# In[44]:
# Getting prepared to convert all assignment deadline dates and making a column of preDeadline dates
file_path = r"C:\Users\annak\CAS-502 Computation\GroupProject-1\GP1 Dataset_ Assignments.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Convert the 'DATE' column to datetime objects
df['DATE'] = pd.to_datetime(df['DATE'], format='%m/%d/%Y')

# Function to calculate pre-deadline date
def get_predeadline(deadline, buffer_days=1):
    predeadline = deadline - datetime.timedelta(days=buffer_days)
    return predeadline

# Calculate predeadline for each date
df['PREDEADLINE'] = df['DATE'].apply(lambda x: get_predeadline(x, buffer_days=1))

# Rearrange columns to put PREDEADLINE between DATE and WK#
column_order = ['ITEM#', 'DATE', 'PREDEADLINE', 'WK#', 'COURSE', 'ASSIGNMENT NAME', 'DESCRIPTION', 'DONE']
df = df[column_order]

# Print the new table headers
print(df.head())

# In[45]:

# Prepares the original table to make room for other colummns for a new document for UI visualization.
original_file_path = r"C:\Users\annak\CAS-502 Computation\GroupProject-1\GP1 Dataset_ Assignments.csv"

# Constructing the new file path
new_file_name = "GP1 Dataset_ Assignments_PreDeadline.csv"
new_file_path = original_file_path.rsplit('\\', 1)[0] + '\\' + new_file_name

# Save the modified DataFrame to the new file
df.to_csv(new_file_path, index=False)

print(f"File saved as: {new_file_path}")


# In[43]:

#from https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Layout.html

#Calls in predeadline function
re_date = get_predeadline(deadline_date, buffer_days=2)

#Takes the prepared csv file and makes the UI 
df = pd.read_csv('GP1 Dataset_Assignment.csv')
df['Colors'] = 'nil'
for index,row in df.iterrows():
    if row['Status'] == 'Open':
        df.at[index,'Colors'] = 'black'
    else:
        df.at[index,'Colors'] = 'red'

a_list = list(df['ASSIGNMENT NAME'])
a_list.insert(0,'None')

button = widgets.Button(description="Mark As Complete")
text = widgets.Dropdown(
    options=a_list,
    value=a_list[0],
    description='Assignment Name:',
    disabled=False,
)

output = widgets.Output()


#@output.capture()
def on_button_clicked(b):
    with output:
        output.clear_output()
        a_name = text.value
        
        if a_name != 'None':
            
       
            index_req = df.index[df['ASSIGNMENT NAME'] == a_name].to_list()
        
            df.at[index_req[0],'Status'] = 'Closed'
            df.at[index_req[0],'Colors'] = 'red'
            df.sort_values(by=['Status', 'DATE'], inplace=True, ascending=[False,True])
            a_list = list(df['ASSIGNMENT NAME'])
        
        df.to_csv('testdata.csv',columns=['DATE','WEEK NUMBER','COURSE','ASSIGNMENT NAME','DESCRIPTION','Status'])
        fig = go.Figure(data=[go.Table(header=dict(
        values=["Date", "Week Number","Course","Assignment Name","Description","Status"],
        line_color='white', fill_color='white',
        align='center', font=dict(color='black', size=12)
        ),
        cells=dict(
        values=[df['DATE'], df['WEEK NUMBER'],df['COURSE'],df['ASSIGNMENT NAME'],df['DESCRIPTION'],df['Status']],
        #line_color=[df.Colors], 
        #fill_color=[df.Colors],
        align='center', font=dict(color= [df.Colors], size=11)
         ))
        ])
        fig.show()
        
fig = go.Figure(data=[go.Table(header=dict(
        values=["Date", "Week Number","Course","Assignment Name","Description","Status"],
        line_color='white', fill_color='white',
        align='center', font=dict(color='black', size=12)
          ),
        cells=dict(
        values=[df['DATE'], df['WEEK NUMBER'],df['COURSE'],df['ASSIGNMENT NAME'],df['DESCRIPTION'],df['Status']],
        #line_color=[df.Colors], 
        #fill_color=[df.Colors],
        align='center', font=dict(color= [df.Colors], size=11)
          ))
        ])

button.on_click(on_button_clicked)
list_button = widgets.HBox([text,button])
widgets.VBox([list_button,output])

# In[ ]:
