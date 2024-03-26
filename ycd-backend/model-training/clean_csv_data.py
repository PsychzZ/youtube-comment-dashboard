import re
import pandas as pd
import numpy as np
from nltk import download
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

download('stopwords')

columns_names = ["text", "target"]

twitter_data = pd.read_csv("more_data.csv", names=columns_names, encoding="ISO-8859-1", skiprows=1)

corrected_columns = ["target", "text"]

twitter2_data = pd.read_csv("more_more_data.csv", names=columns_names, encoding="ISO-8859-1",skiprows=1)
twitter3_data = pd.read_csv("more_more_more_data.csv", names=columns_names, encoding="ISO-8859-1",skiprows=1)

twitter_data = twitter_data.reindex(columns=corrected_columns)
twitter2_data = twitter2_data.reindex(columns=corrected_columns)
twitter3_data = twitter3_data.reindex(columns=corrected_columns)
#check if Columns are named correctly
print(twitter2_data.head())

#check if there are any missing values 
print(twitter2_data.isnull().sum())

twitter_data.dropna(inplace=True)
twitter2_data.dropna(inplace=True)
twitter3_data.dropna(inplace=True)
#check the distribution of the target variable
print(twitter_data['target'].value_counts())
print(twitter2_data['target'].value_counts())
print(twitter3_data['target'].value_counts())

twitter_data = pd.concat([twitter_data, twitter2_data, twitter3_data], ignore_index=True)

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

cleaned_data = pd.read_csv("cleaned_training_data.csv", encoding="ISO-8859-1")

cleaned_data = pd.concat([cleaned_data, twitter_data], ignore_index=True)

cleaned_data.to_csv("cleaned_training_data.csv", index=False, columns=['target', 'stemmed_content'])