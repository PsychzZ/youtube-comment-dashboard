import pickle

model = pickle.load(open('finalized_model.sav', 'rb'))  # Loading the trained model
vectorizer = pickle.load(open('vectorizer.sav', 'rb'))  # Loading the vectorizer



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

    return {
        'positive_count': positive_count,
        'negative_count': negative_count,
        'neutral_count': neutral_count
    }