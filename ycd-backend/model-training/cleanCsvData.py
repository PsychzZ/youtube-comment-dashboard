import re
import pandas as pd
import numpy as np
from nltk import download
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

download('stopwords')

columns_names = ["target", "id", "date", "flag", "user", "text"] 

twitter_data = pd.read_csv("training-data.csv", names=columns_names, encoding="ISO-8859-1")

#check if Columns are named correctly
print(twitter_data.head())

#check if there are any missing values
print(twitter_data.isnull().sum())

#check the distribution of the target variable
print(twitter_data['target'].value_counts())

# Replace target variable 4 with 1
twitter_data.replace({'target': {4:1}}, inplace=True)

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

twitter_data.to_csv("cleaned_training_data.csv", index=False)