# Importing necessary libraries
import pandas as pd  # For data manipulation and analysis
from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.feature_extraction.text import TfidfVectorizer  # For feature extraction
from sklearn.linear_model import LogisticRegression  # For logistic regression model
from sklearn.metrics import accuracy_score  # For evaluating model accuracy
import pickle  # For saving the trained model

# Load Data
data = pd.read_csv("cleaned_training_data.csv", encoding="ISO-8859-1")  # Reading data from CSV file

# Splitting into training and test data
X = data['stemmed_content'].values  # Extracting features
Y = data['target'].values  # Extracting target
# Splitting data into training and testing sets, with 25% data reserved for testing, stratified to maintain class distribution
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, stratify=Y, random_state=3)

# Feature Engineering: Use n-Grams
vectorizer = TfidfVectorizer(ngram_range=(1, 2), lowercase=True)  # Initializing TF-IDF vectorizer with unigrams and bigrams
X_train_vec = vectorizer.fit_transform(X_train.astype('U'))  # Transforming training text data into TF-IDF features
X_test_vec = vectorizer.transform(X_test.astype('U'))  # Transforming testing text data into TF-IDF features

# Train a Logistic Regression Classifier
logistic_model = LogisticRegression(max_iter=1000)  # Initializing logistic regression model with 1000 iterations
logistic_model.fit(X_train_vec, Y_train)  # Training the logistic regression model using training data

# Evaluation of the model on the test data
Y_pred = logistic_model.predict(X_test_vec)  # Predicting target labels for testing data
accuracy = accuracy_score(Y_test, Y_pred)  # Calculating accuracy of the model
print("Accuracy Score: ", accuracy)  # Printing the accuracy score

# Save the model
filename = 'finalized_logistic_model.sav'  # Defining filename for saving the trained model
pickle.dump(logistic_model, open(filename, 'wb'))  # Serializing and saving the trained model to a file


# Final Accuracy Score: 0.790835 so 79.08% accuracy