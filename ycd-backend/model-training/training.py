import random as random
import polars as pl
import tensorflow as tf
import keras

AUTOTUNE = tf.data.AUTOTUNE

# Get Data
data = list(pl.read_csv("training-data.csv", has_header=False, encoding="ISO-8859-1").select(["column_1", "column_6"]).rows())
random.shuffle(data)

# Split Data in train-and testData and split both into comments and targets
rawTrainData = data[:1230000]
trainDataTargets = []
trainDataComments = []
rawTestData = data[1230000:]
testDataTargets = []
testDataComments = []

for i in rawTrainData:
    trainDataTargets.append(i.__getitem__(0))
    trainDataComments.append(i.__getitem__(1))

for i in rawTestData:
    testDataTargets.append(i.__getitem__(0))
    testDataComments.append(i.__getitem__(1))

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
vectorize_layer.adapt(trainDataComments)

# Connect the vectorized comments with the fitting targets
def vectorize_text(text, label):
    text = tf.expand_dims(text, -1)
    return [vectorize_layer(text), label]

trainData = [vectorize_text(a, b) for a,b in zip(trainDataComments, trainDataTargets)]
testData = [vectorize_text(a,b) for a,b in zip(testDataComments, testDataTargets)]

#Create Tensorflow Datasets of the created lists 
trainDataSet = tf.data.experimental.from_list(trainData)
testDataSet = tf.data.experimental.from_list(testData)

# 'cache()' keeps data in memory after it's loaded off disk
# 'prefetch()' overlaps data preprocessing and modek execution while training
# Both make sure that I/O does not become blocking
trainDataSet = trainDataSet.cache().prefetch(buffer_size=AUTOTUNE)
testDataSet = trainDataSet.cache().prefetch(buffer_size=AUTOTUNE)

# Creating the Model (neural network)
model = keras.Sequential([
    # Embedding takes the integer-encoded reviews and looks up an embedding vector for each word-index
    # It maps the words in our vocabulary on a vector in a continuous space
    # similar words have a similar vector
    # input_dim is the zize of the vocabulary
    # output_dim is the length of the vector for every Word 
    keras.layers.Embedding(
        input_dim=len(vectorize_layer.get_vocabulary()),
        output_dim=200
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
    keras.layers.Dense(1, activation="sigmoid")
])
# Summarize the Model to have a better view on the Model for e.g. checking it  
print(model.summary())