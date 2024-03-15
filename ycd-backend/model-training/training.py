import random
import polars as pl
import tensorflow as tf
import keras


data = list(pl.read_csv("training-data.csv", has_header=False, encoding="ISO-8859-1").select(["column_1", "column_6"]).rows())

testData = random.sample(data, 1230000)
testDataTargets = []
testDataComments = []

for i in testData:
    testDataTargets.append(i.__getitem__(0))
    testDataComments.append(i.__getitem__(1))


def standardization(input_data):
    lowercase = tf.strings.lower(input_data)
    return lowercase

vectorize_layer = keras.layers.TextVectorization(
    standardize = standardization,
   output_mode = 'int'
)
vectorize_layer.adapt(testDataComments)

model = keras.Sequential([
    keras.layers.Embedding(),
    keras.layers.Dropout(),
    keras.layers.GlobalAveragePooling1D(),
    keras.layers.Dropout(),
    keras.layers.Dense()
])

model.summary()
