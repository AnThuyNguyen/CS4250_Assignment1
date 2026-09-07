#-------------------------------------------------------------------------
# AUTHOR: Thuy An Nguyen
# FILENAME: index.py
# SPECIFICATION: This program reads a collection of documents, applies normalization and lemmatization, and builds an inverted index. like assignment 1 question 7 but in code
# FOR: CS 4250 - Assignment #1
# TIME SPENT: 1 hour - I started late
#-------------------------------------------------------------------------

# Importing Python libraries
import pandas as pd

# Reading the document collection
data = pd.read_csv("collection.csv")

# Defining the dictionary used for lemmatization
# --> add your Python code here
lemmas = ?
lemmas = {
    "running": "run",
    "jumps": "jump",
    "easily": "easy",
    "fairly": "fair"
}

# Creating the data structure that will store the inverted index
invertedIndex = {}

# Processing each document in the collection
for i, row in data.iterrows():

    docID = row["Document"]
    text = row["Text"]

    # Applying surface-level normalization
    # --> add your Python code here


    # Tokenizing the document
    # --> add your Python code here


    # Applying lemmatization
    # --> add your Python code here


    # Building the inverted index
    # --> add your Python code here


# Printing the inverted index with terms ordered alphabetically
# Expected format:
# term1 : ['Doc1', 'Doc2']
# term2 : ['Doc3']
# --> add your Python code here