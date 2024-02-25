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


# In[16]:


import tkinter as tk
from tkinter import simpledialog
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Initialize the geolocator
geolocator = Nominatim(user_agent="geoapp")

def validate_city(city_name):
    try:
        location = geolocator.geocode(city_name)
        if location:
            print(f"Input '{city_name}' is valid. Location: {location.latitude}, {location.longitude}")
            return True, location.address  # Return True and the formatted address
        else:
            print(f"Input '{city_name}' could not be validated.")
            return False, None
    except GeocoderTimedOut:
        print("Geocoding service timed out.")
        return False, None

def ask_for_cities_and_handle_errors(courses):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    course_city_dict = {}

    for course in courses:
        while True:
            city = simpledialog.askstring("Input", f"Enter the city for the course {course}:")
            is_valid, formatted_address = validate_city(city)
            if is_valid:
                # If the city is valid, map the course to the formatted address and break the loop
                course_city_dict[course] = formatted_address
                break
            else:
                # If the input is invalid, show an error message and prompt again
                print(f"Invalid input received: '{city}'. Please enter a valid city name.")

    # After collecting all inputs, print the final mapping
    print("\nFinal course-city mapping:")
    for course, city in course_city_dict.items():
        print(f"{course}: {city}")

# Example courses
courses = ['CAS502', 'ORG7074', 'RES3500']

ask_for_cities_and_handle_errors(courses)


# In[17]:


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




