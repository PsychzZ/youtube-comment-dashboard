import random as random
import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score


# Get Data
data = pd.read_csv("cleaned_training_data.csv",encoding="ISO-8859-1")


# Split Data in X and Y
X = data['stemmed_content'].values
Y = data['target'].values



# Split Data in train-and testData
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, stratify=Y, random_state=2)


# see the shape of the data
print(X.shape, X_train.shape, X_test.shape)

vectorizer = TfidfVectorizer()


# Vectorize the Data (convert the text data to numbers) astype('U') is used to convert the data to Unicode
X_train = vectorizer.fit_transform(X_train.astype('U'))
X_test = vectorizer.transform(X_test.astype('U'))

# Train the Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)


# MODEL EVALUATION


# Accuracy score on the train data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)
# accuracy score on the train data 80.03%

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)
# accuracy score on the test data 77.7%

#Industry Standard for accuracy score is 70% - 80% so we need to improve the model

print("Accuracy score of the training data : ", training_data_accuracy)

print("Accuracy score of the test data : ", test_data_accuracy)


filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

'''
# Split Data in train-and testData and split both into comments and targets
rawTrainData = data[:20000]
trainDataTargets = []
trainDataComments = []
rawTestData = data[20000:24000]
testDataTargets = []
testDataComments = []

for i in rawTrainData:
    trainDataTargets.append(i.__getitem__(0))
    trainDataComments.append(i.__getitem__(1))

for i in rawTestData:
    testDataTargets.append(i.__getitem__(0))
    testDataComments.append(i.__getitem__(1))

print("TEST ")
print(trainDataComments)
# Put every comment in lowercase so every same Word has the same token
def standardization(input_data):
    lowercase = tf.strings.lower(input_data)
    return lowercase


# Create for every Word in the comments a token (Vectorization)
# So we're creating a vocabulary
vectorize_layer = keras.layers.TextVectorization(
    standardize = standardization,
   output_mode = 'int'
)
print("MEGA TEST ")
print(trainDataComments[0:5])
vectorize_layer.adapt(trainDataComments)

# Connect the vectorized comments with the fitting targets
def vectorize_text(text, label):
    print("TEXT: ", text)
    text = tf.expand_dims(text, -1)
    return [label, vectorize_layer(text)]

trainData = [vectorize_text(a, b) for a,b in zip(trainDataComments, trainDataTargets)]
testData = [vectorize_text(a,b) for a,b in zip(testDataComments, testDataTargets)]

# Creating the Model (neural network)
model = keras.Sequential([
    # Embedding takes the integer-encoded reviews and looks up an embedding vector for each word-index
    # It maps the words in our vocabulary on a vector in a continuous space
    # similar words have a similar vector
    # input_dim is the zize of the vocabulary
    # output_dim is the length of the vector for every Word 
    keras.layers.Embedding(
        input_dim=len(vectorize_layer.get_vocabulary()),
        output_dim=100
        ),
    # Dropout reduces overfitting. Overfitting is when the Model fits to strong with the trainData.
    # So it can not work well with new Data
    # It deactivates a random number of neurons to reduce it(our case: 20%)      
    keras.layers.Dropout(0.2),
    # GlobalAveragePooling1D returns a fixed-length output vector for each example by averaging over the sequence dimension
    # So it allows to handle input of variable length
    keras.layers.GlobalAveragePooling1D(),
    keras.layers.Dropout(0.2),
    # Lies selbst durch
    keras.layers.Dense(1, activation='sigmoid')
])
# Summarize the Model to have a better view on the Model for e.g. checking it  

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Create Loss-Function and Optimizer
'''