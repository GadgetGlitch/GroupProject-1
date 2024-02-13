#!/usr/bin/env python
# coding: utf-8

# # Many Ways for Python to Scan and Read Data

# In[ ]:


import ipywidgets as widgets
from IPython.display import display
import pandas as pd
from docx import Document
import fitz  # PyMuPDF
import requests
from bs4 import BeautifulSoup


# # Import Syllubus File or URL Button

# In[6]:


# Processing functions for file upload
def process_file_upload(change):
    uploaded_files = change['new']
    for name, file_info in uploaded_files.items():
        # Detect file type and process accordingly
        if name.endswith('.xlsx') or name.endswith('.xls'):
            df = pd.read_excel(file_info['content'])
            print(df.head())  # Example of processing Excel file
        elif name.endswith('.pdf'):
            doc = fitz.open(stream=file_info['content'], filetype="pdf")
            text = ""
            for page in doc:
                text += page.get_text()
            print(text)  # Example of processing PDF file
        elif name.endswith('.docx'):
            doc = Document(file_info['content'])
            text = ""
            for para in doc.paragraphs:
                text += para.text + '\n'
            print(text)  # Example of processing Word document
        else:
            print(f"Unsupported file type: {name}")

# Function to scrape and process HTML from URL
def scrape_and_process_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.get_text())  # Example of processing HTML content

# Create the file upload widget
file_upload = widgets.FileUpload(
    accept='.xlsx, .xls, .pdf, .docx',  # Specify acceptable file types
    multiple=True,  # Allow multiple files to be selected
    description='Upload Files'
)
file_upload.observe(process_file_upload, names='value')

# Text label with supported file types
file_types_label = widgets.Label('Supported file types: Docs (Word), PDF, Excel')

# URL input and submission setup
url_input = widgets.Text(placeholder='Enter URL here', description='URL:')
submit_button = widgets.Button(description='Submit URL', button_style='', tooltip='Click to submit the URL')
def submit_url(b):
    url = url_input.value
    if url:  # Check if the URL is not empty
        scrape_and_process_html(url)
    else:
        print("Please enter a URL.")
submit_button.on_click(submit_url)

# Organizing the layout
upload_box = widgets.VBox([file_types_label, file_upload])
url_box = widgets.VBox([url_input, submit_button])
main_box = widgets.VBox([upload_box, url_box])

# Displaying the entire layout
display(main_box)


