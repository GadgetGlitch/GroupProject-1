#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import tkinter as tk
from tkinter import simpledialog
import ipywidgets as widgets
from IPython.display import display, clear_output
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


# In[13]:


# Initialize the geolocator
geolocator = Nominatim(user_agent="geoapp")


# In[7]:


file_path = r"C:\Users\annak\CAS-502 Computation\GroupProject-1\GP1 Dataset_ Assignments.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')


# In[8]:


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
            
# Convert user input and known cities to lowercase for case-insensitive comparison
if city.lower() in (known_city.lower() for known_city in known_cities):
    print(f"Correct input received: {city}")
    # Rest of the code remains the same

from fuzzywuzzy import process

def get_correction_or_feedback(input_city):
    # Use fuzzy matching to find the closest city name from known_cities
    closest_match, match_score = process.extractOne(input_city, known_cities)
    if match_score > 80:  # You can adjust the threshold based on your needs
        return closest_match
    return None

    # Optionally, print or return the course-city dictionary
    print(course_city_dict)
    return course_city_dict

# Your provided file path
file_path = r"C:\Users\annak\CAS-502 Computation\GroupProject-1\GP1 Dataset_ Assignments.csv"

# Call the function with your file path
generate_course_city_widget(file_path)


# In[9]:


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


# # Test Course_TMZ Function
# For this set up a test plan was devised. the code was copied and error messages added to feedback to the user.
# First, we'll enhance the function to handle various types of incorrect inputs. This version will include basic error handling for misspelled cities and incorrect input types (like states or time zones). For simplicity, we'll simulate the process of asking for city names and handling errors without integrating the full CSV processing logic here.

# # Test 1 - Validation
# Objective: Confirm the function works correctly with typical, expected inputs.
# Real Test Approach: Manually input a series of correct city names corresponding to the courses. This test can be structured to include a variety of city names that are spelled correctly and represent a realistic distribution of time zones.
# Consideration: Ensure that the cities chosen cover different time zones to validate that the function accurately assigns the correct CRS_TZ values.

# In[14]:


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


# # Results Test 1
# When user inputs everything correctly as it was inputted as expected by the code.

# # Test 2 - Invalidation Test
# Objective: Test how the function handles invalid inputs, such as incorrect city names or unexpected types of input (e.g., time zones or states instead of cities).
# Real Test Approach: Create a test where you manually input:
# A state name instead of a city.
# An exact time zone abbreviation (e.g., MST, PST).
# Common misspellings for city names.
# Consideration: This test checks the function's error handling and its ability to prompt for re-entry or correct invalid inputs.

# In[15]:


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


# # Resutls Test 2
# The code is super sensitive to lower and uppercase spellings of cities. The third attempt was a misspelling of Tempe and it was an acual place. Therefore it didn't see it as an error, but there was no way for the user to correct it as its location and timezone would or could be different and make the tool useless. After this, confirmation code was suggested. 

# In[ ]:


def confirm_location(city_name, geocoded_address):
    return messagebox.askyesno("Confirm Location",
                                f"Did you mean: '{geocoded_address}' for '{city_name}'?")

# In your main function, after geocoding the city:
is_valid, formatted_address = validate_city(city)
if is_valid:
    user_confirmed = confirm_location(city, formatted_address)
    if user_confirmed:
        # Proceed with using the geocoded address
    else:
        # Prompt for input again or allow corrections


# # Test 3 - Boundary Conditions Test
# Objective: Examine how the function behaves under extreme or minimal conditions.
# Real Test Approach: For this, consider two scenarios:
# Minimal Input Scenario: Run the function with just one course in the CSV to see if it can handle minimal data.
# Stress Test Scenario: If feasible, test with a large number of courses (potentially automating the input process for practicality) to see how the function performs under load. For a real input scenario, this might involve preparing a CSV with a large dataset beforehand and then manually entering cities to see if performance degrades or errors occur.

# In[ ]:


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


# # Reslults Test 3
# The current code doesnt allow errors as it will continue to pop up the same window until you enter it correctly. This means it will not allow you to exit, cancel or find out what is wrong. This however does minimize the boarndaries of the code. to counteract this it can be recommended to allow users to gain abililty to make errors and get feedback to those errors. 

# In[ ]:


#Allow users to exit the popup window
city = simpledialog.askstring("Input", f"Enter the city for the course {course}:")
if city is None:  # User pressed cancel or closed the dialog
    print("User cancelled the operation.")
    break  # Exit the loop or handle cancellation appropriately


# In[ ]:


#Let users enter a blank space and return an invalid entry message
if not city.strip():  # Check if the input is empty or whitespace
    messagebox.showwarning("Invalid Input", "City name cannot be empty. Please enter a valid city name.")
    continue  # Prompt the user again

