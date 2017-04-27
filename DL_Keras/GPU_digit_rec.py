#!/usr/bin/env python3
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.misc import imread
#This is simply a linear stack of neural network layers, and it's perfect for the type of feed-forward CNN we're building in this tutorial.
from keras.models import Sequential
# These are the layers that are used in almost any neural network:
from keras.layers import Dense, Dropout, Activation, Flatten
#These are the convolutional layers that will help us efficiently train on image data:
from keras.layers import Convolution2D, MaxPooling2D
#helpful utilities
from keras.utils import np_utils

np.random.seed(123) #For reproducability with the tutorial.

root_dir = os.path.abspath('./')
data_dir = os.path.join(root_dir, 'data')
sub_dir = os.path.join(root_dir, 'sub')

# check for existence
os.path.exists(root_dir)
os.path.exists(data_dir)

train = pd.read_csv(os.path.join(data_dir, 'Train', 'train.csv'))
test = pd.read_csv(os.path.join(data_dir, 'Test_AV.csv'))
print(train.head())

#Using the Analytics Vidhya tutorial for a few inputs to parse the train / test data sets.
rng = np.random.RandomState(123)
img_name = rng.choice(train.filename)
filepath = os.path.join(data_dir, 'Train', 'Images', 'train', img_name)

img = imread(filepath, flatten=True)
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()
print(train.shape)
print(img.shape)

temp1 = []
for img_name in train.filename:
 image_path = os.path.join(data_dir, 'Train', 'Images', 'train', img_name)
 img = imread(image_path, flatten=True)
 img = img.astype('float32')
 temp1.append(img)

train_x = np.stack(temp1)

temp2 = []
for img_name in test.filename:
 image_path = os.path.join(data_dir, 'Train', 'Images', 'test', img_name)
 img = imread(image_path, flatten=True)
 img = img.astype('float32')
 temp2.append(img)

test_x = np.stack(temp2)
print(train_x.shape)

train_x = train_x.reshape(train_x.shape[0], 1, 28, 28)
test_x = test_x.reshape(test_x.shape[0], 1, 28, 28)
print(train_x.shape)

train_x /= 255
test_x /= 255

train_y = train.label
#At this stage, I need to split the train data into a train set and a cross-validation set. I'm going to use a 75/25
#split, what the hell. The original Keras tutorial I followed had a 60,000 digit training set, as well as a labeled
#test set. Here, my test set is not labeled - aka that's what I am classifying!

split_size = int(train_x.shape[0] * 0.75)
train_x, cross_val_x = train_x[:split_size], train_x[split_size:]
train_y, cross_val_y = train_y[:split_size], train_y[split_size:]
# Next up is to reshape the labels to categorical data, with the quick and easy .to_categorical function
train_Y = np_utils.to_categorical(train_y, 10)
cross_val_Y = np_utils.to_categorical(cross_val_y, 10) #notice we went to capital Y's for this change
print(train_Y.shape)
print(cross_val_Y.shape)
#Declare a sequential model format
model = Sequential()
#Declare the input layer
model.add(Convolution2D(32,3,3, activation='relu', input_shape=(1,28,28), dim_ordering='th'))
#input shape corresponds to the shape of one sample, depth, width, height
print(model.output_shape) #we get (None,-1,26,32) tutorial shows (None,32,26,26)
#adding layers to our model like building lego
model.add(Convolution2D(32,3,3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
#Dropout layer is a method of regularization (prevents over-fitting)
#Now add fully connected Dense layers
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))
#Hard part is over - now we need to compile model and define loss function
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(train_x, train_Y, batch_size=32, nb_epoch=10, verbose=0)
#Finally, we evaluate this model on the test set, generating a score
score = model.evaluate(cross_val_x, cross_val_Y, verbose=0)

print(score)

predictions = model.predict_classes(test_x)

img_name = rng.choice(test.filename)
filepath = os.path.join(data_dir, 'Train', 'Images', 'test', img_name)

img = imread(filepath, flatten=True)

test_index = int(img_name.split('.')[0]) - 49000
print ("Prediction is: ", predictions[test_index])
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()

d = {'filename': test.filename, 'label':predictions}
submit_file = pd.DataFrame(d)
submit_file.to_csv('CN_submit_GPU.csv', index=False)
