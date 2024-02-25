#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import tkinter as tk
from tkinter import simpledialog
import ipywidgets as widgets


# In[2]:


file_path = r"C:\Users\annak\CAS-502 Computation\GroupProject-1\GP1 Dataset_ Assignments.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')


# In[10]:


import pandas as pd
import tkinter as tk
from tkinter import simpledialog

def generate_course_city_widget(file_path):
    # Load CSV
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    
    # Extract unique course names
    unique_courses = df['COURSE'].unique()
    
    # Create a Tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Dictionary to store course-city pairs
    course_city_dict = {}
    
    # Ask the user for the city of each unique course
    for course in unique_courses:
        city = simpledialog.askstring("Input", f"Enter the city for the course {course}:")
        if city:  # Ensure a city was entered
            course_city_dict[course] = city
    
    # Optionally, print or return the course-city dictionary
    print(course_city_dict)
    return course_city_dict

# Your provided file path
file_path = r"C:\Users\annak\CAS-502 Computation\GroupProject-1\GP1 Dataset_ Assignments.csv"

# Call the function with your file path
generate_course_city_widget(file_path)


# In[15]:


import pandas as pd

# Assuming df is your DataFrame after reading the CSV
file_path = r"C:\Users\annak\CAS-502 Computation\GroupProject-1\GP1 Dataset_ Assignments.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Corrected course-city mapping
course_city_dict = {
    'CAS502': 'Tempe',
    'ORG7074': 'Pasadena',
    'RES3500': 'Pasadena'  # Corrected the typo here
}

# City to time zone mapping
# Note: This is a simplified mapping. Real-world applications should use a more accurate method.
city_time_zone_dict = {
    'Tempe': 'MST',
    'Pasadena': 'PT'
}

# Map courses to cities, then cities to time zones
df['CRS_TZ'] = df['COURSE'].map(course_city_dict).map(city_time_zone_dict)

# Find the position of the 'DATE' column
date_column_position = df.columns.get_loc('DATE')

# Insert the 'CRS_TZ' column right after the 'DATE' column
# Ensure 'CRS_TZ' is not already in the DataFrame to avoid duplication
if 'CRS_TZ' in df:
    # If 'CRS_TZ' already exists, drop it first to avoid errors
    df.drop('CRS_TZ', axis=1, inplace=True)

# Create a new DataFrame with 'CRS_TZ' in the desired position
df = df.reindex(columns=df.columns.tolist()[:date_column_position+1] + ['CRS_TZ'] + df.columns.tolist()[date_column_position+1:-1])

# Save the updated DataFrame back to a CSV, without the 'City' column
df.to_csv(file_path.replace('.csv', '_updated.csv'), index=False)

print("CSV file has been updated with the CRS_TZ column right after the DATE column.")
print(df.head())


# In[ ]:




