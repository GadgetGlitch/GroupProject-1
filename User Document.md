# Assignment Tracker User Documentation

## How to Use the Assignment Tracker
The Assignment Tracker is designed to simplify the tracking of assignments within different courses taken by a student during a given time period. It is implemented as a Jupyter Notebook, offering an interactive interface for managing assignment status updates.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Opening the Tracker](#opening-the-tracker)
- [Using the Notebook](#using-the-notebook)
  - [User City Details](#user-city-details)
  - [Assignment Tracker Table](#assignment-tracker-table)
- [Exporting Data](#exporting-data)
- [Conclusion](#conclusion)

## Getting Started

### Prerequisites
Please refer Installation.md file

## Opening the Tracker
To use the Assignment Tracker:
1. Ensure you have Jupyter Notebook or JupyterLab installed on your system.
2. Run `jupyter notebook` or `jupyter lab`.
3. In the Jupyter interface, navigate to and open the Assignment Tracker notebook.  

## Using the Notebook
Once the notebook is opened, run all the cells in the notebook. This can be done by going to 'Cell' from the menu and selecting 'Run All'.

### User City Details
- **Input:** Name of the city where the user is based
- **Action:** Enter this information into designated cell under the section 'Ask the user for their city' of the notebook.

## Assignment Tracker Table
- **Action:** Scroll to the last cell of the notebook. Check that the dropdown list shows 'None'. Now click the button 'Mark As Complete'.
- The above action will display status of the Assignments as stored in the input csv file.
- The table has following headers:
  - ITEM: Shows Assignment number
  - COURSE: The Assignment is from this course
  - ASSIGNMENT NAME: Name of the Assignment
  - DESCRIPTION: Description of the Assignment
  - DATE: Due date for the assignment (as per the school's time zone)
  - LOCAL_DUE_DATE: Due date for the assignment converted to user time zone
  - PREDEADLINE: A one day buffer before LOCAL_DUE_DATE
  - DONE: Status of the Assignment. 'Y' indicates completed. 'N' indicates not completed.
- The next upcoming assignment (or upto three assignments, if all these fall on the same day) are shown in yellow highlight.
- Completed assignments are shown at the bottom of the table in 'red' font.

- **Action:** To mark an assignment as complete, select the Assignment Name from the drop down list and then click 'Mark As Complete'. The table will be refreshed. Note that updates are saved to the original file. Thus, if the tracker is closed and opened again, the table will show the latest update made to the assignment status.
- **Note:** Assignments once marked complete cannot be undone automtically through the tracker. Any such change has to be done directly within the csv file.

## Exporting Data
- **Exporting Data:** Data is autmatically exported to the csv file everytime user clicks the 'Mark As Complete' button.

## Conclusion
The Assignment Tracker aims to enhance your assignment tracking workflow. 
