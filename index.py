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
lemmas = {
    "homes": "home",
    "sales": "sale",
    "rising": "rise",
    "increasing": "increase",
    "increases": "increase"
}

# Creating the data structure that will store the inverted index
invertedIndex = {}

# Processing each document in the collection
for i, row in data.iterrows():

    docID = row["Document"]
    text = row["Text"]

    # Applying surface-level normalization
    # --> add your Python code here
    text = text.lower()  # Converting text to lowercase
    text = ''.join(char for char in text if char.isalnum() or char.isspace())  # Removing punctuation


    # Tokenizing the document
    # --> add your Python code here
    tokens = text.split()


    # Applying lemmatization
    # --> add your Python code here
    new_tokens = []
    for token in tokens:
        new_tokens.append(lemmas.get(token, token)) #search token in lemmas, if not exist, keep it as is
    tokens = new_tokens


    # Building the inverted index
    # --> add your Python code here
    for token in tokens:
        if token not in invertedIndex: #Add token to inverted index
            invertedIndex[token] = []
        if docID not in invertedIndex[token]: #Add document ID in the token list
            invertedIndex[token].append(docID)


# Printing the inverted index with terms ordered alphabetically
# Expected format:
# term1 : ['Doc1', 'Doc2']
# term2 : ['Doc3']
# --> add your Python code here
for term in sorted(invertedIndex.keys()):
    print(f"{term} : {invertedIndex[term]}")