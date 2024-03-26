import pickle
import pandas as pd  # For data manipulation and analysis


model = pickle.load(open('finalized_model.sav', 'rb'))  # Loading the trained model
vectorizer = pickle.load(open('vectorizer.sav', 'rb'))  # Loading the vectorizer

df = pd.read_csv("cleaned_training_data.csv", encoding="ISO-8859-1")  # Reading data from CSV file

df['stemmed_content'] = df['stemmed_content'].astype('U')  # Converting the 'stemmed_content' column to string type

X = df['stemmed_content'].values  # Extracting features


def predict_comment(comments: list):
    # Preprocess the comment
    comment_vec = vectorizer.transform(comments)  # Transforming the comment into TF-IDF features

    # Predict the sentiment of the comment
    prediction = model.predict(comment_vec)  # Predicting the sentiment of the comment

    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for pred in prediction:
      if pred == 2:
        positive_count += 1
      elif pred == 0:
        negative_count += 1
      else:
        neutral_count += 1

    print("Positive comments:", positive_count)
    print("Negative comments:", negative_count)
    print("Neutral comments:", neutral_count)


if __name__ == '__main__':
    comments = X[:10]  # Selecting first 10 comments for prediction
    predict_comment(comments)