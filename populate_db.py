import pandas as pd
from models import db, Assignment  # Ensure you have defined these in your models
from config import DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up the database engine and session
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Read the dataset (update the file path if needed)
df = pd.read_csv("Datasets/assignments.csv")

# Iterate over the dataset and add each assignment to the database
for _, row in df.iterrows():
    assignment = Assignment(
        title=row["title"],
        description=row["description"],
        due_date=row["due_date"]
        # add other fields as necessary
    )
    session.add(assignment)

session.commit()
print("Database populated successfully!")
