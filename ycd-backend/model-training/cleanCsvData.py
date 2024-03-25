import re
import pandas as pd
import numpy as np
from nltk import download
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

download('stopwords')

columns_names = ["target", "text"] 

twitter_data = pd.read_csv("training-data.csv", usecols=columns_names, encoding="ISO-8859-1")

columns2_names = ["text", "target"]

corrected_columns = ["target", "text"]

twitter2_data = pd.read_csv("Twitter_Data.csv", names=columns2_names, encoding="ISO-8859-1",skiprows=1)

twitter2_data = twitter2_data.reindex(columns=corrected_columns)
#check if Columns are named correctly
print(twitter2_data.head())

twitter2_data.replace({'target': {1:2}}, inplace=True)
twitter2_data.replace({'target': {0:1}}, inplace=True)
twitter2_data.replace({'target': {-1:0}}, inplace=True)

#check if there are any missing values 
print(twitter2_data.isnull().sum())

twitter2_data.dropna(inplace=True)
#check the distribution of the target variable
print(twitter2_data['target'].value_counts())

twitter_data = pd.concat([twitter_data, twitter2_data], ignore_index=True)

#check if Columns are named correctly
print(twitter_data.head())

#check if there are any missing values
print(twitter_data.isnull().sum())

#check the distribution of the target variable
print(twitter_data['target'].value_counts())

# Replace target variable 4 with 1
twitter_data.replace({'target': {4:2}}, inplace=True)

#Stemming Data so group same words together (e.g. "actor", "acting", "acted" -> "act")
port_Stem = PorterStemmer()

def stemming(text):
    # Remove all non-letters
    stemmed_content = re.sub('[^a-zA-Z]',' ', text)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    # Remove stopwords and stem the words
    stemmed_content = [port_Stem.stem(word) for word in stemmed_content if not word in stopwords.words("english")]
    # Join the words back into one string separated by space
    stemmed_content = ' '.join(stemmed_content)

    return stemmed_content


# Apply the function to the data takes 30-50 Minutes
twitter_data['stemmed_content'] = twitter_data['text'].apply(stemming)

print(twitter_data.memory_usage().sum() / 1024**2) # Check the memory usage of the dataframe

twitter_data.to_csv("cleaned_training_data.csv", index=False, columns=['target', 'stemmed_content'])