#!/usr/bin/env python
# coding: utf-8

# In[2]:


def test_personal_city_input(city):
    # Validity test: Check if the city is a string
    if not isinstance(city, str):
        print("Validity test failed: City must be a string.")
        return False

    # Invalidity test: Check if the city is empty
    if city.strip() == "":
        print("Invalidity test failed: City cannot be empty.")
        return False

    # Boundary test: Check if the city is within a certain length range
    if len(city) < 3 or len(city) > 50:
        print("Boundary test failed: City length must be between 3 and 50 characters.")
        return False

    # All tests passed
    print("All tests passed.")
    return True

# Test cases
test_personal_city_input("New York")  # Valid input
test_personal_city_input("")          # Invalid input (empty)
test_personal_city_input("Los Angeles")  # Boundary input (length = 11)
test_personal_city_input(123)         # Invalid input (not a string)


# In[ ]:




