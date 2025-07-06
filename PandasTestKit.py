import pandas as pd
import pymongo
from pymongo import MongoClient

#
notebook = [{"Title": "Devil may Cry 5",
             "Series": "DMC",
             "Type": "Game",
             "Rating": "89/100"
             }]

notebook = pd.DataFrame(notebook)
notebook.to_json('Games.json')

note = pd.read_json("Games.json")
print(note["Title"][0])

print(pd.read_sql_query("Select Title From Games.json"))

#
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['Hospital']
collection = db['Doctor']

query = {'Dcnic': '1222222222222'}

data = list(collection.find(query))

client.close()

data_frame = pd.DataFrame(data)

print(data_frame['Dcnic'])

#
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['Hospital']
collection = db['Doctor']

# Data to be inserted as a dictionary
doctor_data = {
    'name': 'John Doe',
    'specialty': 'Cardiology',
    'experience': 10
}

# Query to check if the doctor already exists in the collection
query = {'name': doctor_data['name']}

# Update data if the doctor already exists, otherwise insert a new document
result = collection.update_one(query, {'$set': doctor_data}, upsert=True)
print("Modified count:", result.modified_count)

client.close()

try:
    notebook = pd.read_csv("Games.csv")
    print(notebook)
except FileNotFoundError:
    import csv

    data = [['Title', 'Series', 'Type', 'Rating']]

    file_path = 'Games.csv'

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)

        for row in data:
            writer.writerow(row)

    print("CSV file created successfully.")

# How do you read a CSV file into a pandas DataFrame?
notebook = pd.read_csv("video_games.csv")

# How can you load data from an Excel file into a DataFrame?
excel_book = pd.read_excel("Financial Sample.xlsx")
print(excel_book)

# What are the basic methods to view:
# the first few rows,
print(notebook.head())
# last few rows,
print(notebook.tail())
# and random rows of a DataFrame?
print(notebook.sample(5))

# How can you check the number of rows and columns in a DataFrame?
print(notebook.shape)

# How can you add a new column to a DataFrame based on calculations from existing columns?
# Like Dictionaries
print(notebook)

# What is the purpose of the describe() function, and how is it useful?
print(notebook.describe(percentiles=None, include=None, exclude=None))
# The method describe() in the context of dataframes usually refers to a statistical summary of the numerical columns
# in the dataframe. It provides various descriptive statistics that give you a quick overview of the distribution and
# central tendencies of the data. It is typically available in libraries like Pandas (Python) or similar data
# manipulation libraries.
# Stats Summary:
# Count: The number of non-null values in the column.
# Mean: The arithmetic mean (average) of the values in the column.
# Standard Deviation (std): A measure of the amount of variation or dispersion in the values.
# Minimum (min): The minimum value in the column.
# 25th Percentile (25%): The value below which 25% of the data falls.
# 50th Percentile (50%): The median value, which separates the lower and upper halves of the data.
# 75th Percentile (75%): The value below which 75% of the data falls.
# Maximum (max): The maximum value in the column.

# How do you select a specific column from a DataFrame?
print(notebook.loc[notebook["Title"] == "Dragon Ball Z: Shin Budokai - Another Road"])

# How can you access rows based on their index or label?
print(notebook.loc[0])
print(notebook.loc[notebook["Title"] == "Spider-Man 2"])

# What is the difference between
# loc and
print(notebook.loc[:, 'Title'])
# iloc in pandas?
print(notebook.iloc[:, 4])


# How do you filter rows based on certain conditions?
#                     ['Title']    'Title'      '^(Title|Features.Handheld?)'     0 or 1
print(notebook.filter(items=None, like=None, regex='^(Title|Metadata.Genres)', axis=None))

# What function would you use to load data from a SQL database into a DataFrame?
print(pd.DataFrame(list(MongoClient('mongodb://localhost:27017')['Hospital']['Person'].find(
    {'specialty': 'Software Engineering'}))))
# # Connect to the MongoDB server (replace 'mongodb://localhost:27017' with your connection string)
# client = MongoClient('mongodb://localhost:27017')
# # Select the database and the collection from which you want to fetch data
# db = client['Hospital']
# collection = db['Doctor']
# # Query to fetch doctors with specialty 'Cardiology'
# query = {'specialty': 'Cardiology'}
# # Fetch data from MongoDB collection into a list of dictionaries
# data = list(collection.find(query))
# # Load data into a DataFrame using pandas DataFrame() constructor
# df = pd.DataFrame(data)
# # Close the MongoDB connection (optional, but recommended)
# client.close()
# import sqlite3  # Replace 'sqlite3' with the appropriate SQL database library for your database.
# # Establish a connection to your SQL database.
# # For example, using SQLite:
# connection = sqlite3.connect('path_to_your_database.db')
# # Replace the SQL query below with your desired SQL query to retrieve the data from the database.
# query = "SELECT * FROM your_table_name WHERE specialty = 'Software Engineering';"
# # Use pandas.read_sql() to load the data from the database into a DataFrame.
# data_frame = pd.read_sql(query, connection)
# # Close the database connection when you're done.
# connection.close()
# # Now you have the data in a pandas DataFrame (data_frame) and can perform operations on it.
# print(data_frame)

# What is the function to get a concise summary of a DataFrame's columns?
print(notebook.columns)
print(notebook.info)  # ??

#  Filters and displays rows with titles containing "Final Fantasy," showing their genres and online features.
notebook = pd.read_csv("video_games.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# How do you select a single column from a DataFrame?
# How can you select multiple columns from a DataFrame?
# What is the correct way to filter rows based on a condition in a DataFrame?
print(notebook.loc[notebook["Title"].str.contains("Final Fantasy"), ["Title", "Metadata.Genres", "Features.Online?"]])

# Count number of null values per column
print(notebook.isnull().sum())

# Drop rows containing any missing value
notebook_cleaned_rows = notebook.dropna()

# Drop columns containing any missing value
notebook_cleaned_columns = notebook.dropna(axis=1)

# Fill missing values with the mean of the column
notebook_filled_mean = notebook.fillna(notebook.mean())

# Fill missing values with a constant (e.g., 0)
notebook_filled_zero = notebook.fillna(0)

# Forward-fill missing values
notebook_forward_filled = notebook.fillna(method='ffill')

# Backward-fill missing values
notebook_backward_filled = notebook.fillna(method='bfill')

# Linear interpolation for missing values
# Interpolation can be used when dealing with ordered data, such as time series,
# to estimate missing values based on existing values.
notebook_interpolated = notebook.interpolate(method='linear')

# Drop rows where 'column_name' has missing values
notebook_dropped_rows = notebook.dropna(subset=['column_name'])

# Step 2: Drop duplicates and modify the original DataFrame
notebook.drop_duplicates(keep='last', inplace=True)

# Step 3: Drop rows with missing values and modify the original DataFrame
notebook.dropna(subset="Metadata.Publishers", inplace=True)

# Step 4: Check for missing values (optional)
print(notebook.isnull().sum())

# How do you rename columns in a DataFrame?
notebook.rename(columns={"Title": "Titles"}, inplace=True)
print(notebook.columns)
