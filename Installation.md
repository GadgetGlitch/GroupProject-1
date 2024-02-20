# Installation Instructions for Class Assessment Tracker
## Version 1.0 
**Date:** 24/02/2024

**Author(s):**
Team GroupProject-1
Pradeesh, Mike K, and Annaka

This project is designed for the platform Jupyter Notebook in the language of Python. 
There are several packages that are needed to be installed and imported before the notbook will run.
Based on the context of a Jupyter Notebook-based class assessment tracker, here's how you might fill in 
the components of the installation document tailored to this specific application. This example assumes
the tracker is a Jupyter Notebook designed to help instructors or students track and assess class assignments 
and grades.

## Introduction
This document provides detailed instructions for installing and setting up the Class Assessment Tracker
on your system. It covers the installation process, including prerequisites, step-by-step setup instructions, 
and verification of a successful installation. This guide is intended for instructors and students using 
[specific operating systems, e.g., Windows, macOS, Linux] for educational assessment purposes.

## Prerequisites
- A computer with internet access.
- Python 3.6 or newer installed.
- Jupyter Notebook or JupyterLab installed.
- Basic familiarity with running Jupyter Notebooks.

## Preparation
1. Ensure Python and Jupyter Notebook are installed on your system. Visit [Python's official site](https://www.python.org/downloads/) 
and [Jupyter's installation guide](https://jupyter.org/install) for instructions.
2. Download the Class Assessment Tracker notebook file from [repository link or location].

## Dependencies
Before installing the Class Assessment Tracker, ensure you have the following packages and libraries installed. 
These dependencies are crucial for the functionality of the tracker:

## Instalations and Imports
- **pandas:** A powerful data analysis and manipulation library for Python. Used for handling and 
analyzing data sets within the tracker. Install via pip with `!pip install pandas`.
- **pytz:** Provides timezone calculations for Python. Essential for handling time data that may span
multiple time zones. Install via pip with `!pip install pytz`.
- **plotly:** An interactive graphing library for Python. Used for creating dynamic, interactive 
visualizations within the tracker. Install via pip with `!pip install plotly`.
- **ipywidgets:** Provides interactive HTML widgets for Jupyter notebooks. Used to create interactive user 
interfaces within the tracker. Install via pip with `!pip install ipywidgets`.
- **datetime:** A standard library module for manipulating dates and times. Used extensively for date 
calculations and formatting.
- **fitz (PyMuPDF):** A library to work with PDF files, including reading text and metadata. Used for
processing PDF-based assignment submissions or resources. Install via pip with `!pip install pymupdf`.
- **requests:** A simple HTTP library for Python. Used for making HTTP requests to download data or 
interact with web services. Install via pip with `!pip install requests`.
- **re (Regular Expressions):** A standard library module for string searching and manipulation 
using regular expressions. Used for text processing and data extraction tasks.
- **openpyxl:** A library for reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files. Used for 
handling Excel-based data inputs or outputs. Install via pip with `!pip install openpyxl`.
- **xlrd:** A library for reading data and formatting information from Excel files (specifically .xls).
Install via pip with `!pip install xlrd`.
- **python-docx (docx):** A Python library for creating and updating Microsoft Word (.docx) files. 
Install via pip with `!pip install python-docx`.
- **BeautifulSoup (bs4):** A library for parsing HTML and XML documents. Often used for web scraping tasks.
Install via pip with `!pip install beautifulsoup4`.
- **IPython.display:** A module for displaying various types of content in IPython environments. 
Part of the IPython package and used for rich content display in Jupyter notebooks.
- **geopy:** A Python client for several popular geocoding web services. Used for geocoding addresses
and validating city names. Install via pip with `!pip install geopy`.
- **TimezoneFinder:** A fast, lightweight library for looking up the timezone for any point on earth 
(using latitude and longitude). Install via pip with `!pip install timezonefinder`.

## Command Line Installation Process
1. Open your terminal (or Command Prompt/PowerShell in Windows).
2. Navigate to the directory where you downloaded the Class Assessment Tracker notebook.
3. Launch Jupyter Notebook or JupyterLab by typing `jupyter notebook` or `jupyter lab` and pressing Enter.

## Configuration and Setup
1. In the Jupyter interface, locate and open the Class Assessment Tracker notebook.
2. Follow the instructions within the notebook to configure it for your class or assessment criteria.

## Verification
Ensure that the notebook runs without errors:
1. Try executing all cells (In Jupyter Notebook, you can use the "Run All" feature under the "Cell" menu).
2. Verify that the tracker allows for inputting and calculating grades as expected.

## Troubleshooting
- **Issue:** Jupyter Notebook does not launch.
  - **Solution:** Check that Python and Jupyter are correctly installed and accessible from your command line or terminal.
- **Issue:** Errors when running the notebook.
  - **Solution:** Ensure all required Python packages are installed by running `pip install -r requirements.txt` 
  (if a requirements file was provided).

## Additional Resources
- [Jupyter Notebook User Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)
- [Python 3 Documentation](https://docs.python.org/3/)

## Glossary
**Jupyter Notebook:** An open-source web application that allows you to create and share documents 
that contain live code, equations, visualizations, and narrative text.

## Contact Information
For further assistance, please contact Team GroupProject-1.

## Revision History
- **24/02/2024** Initial release of the installation instructions for Class Assessment Tracker version 1.0.

