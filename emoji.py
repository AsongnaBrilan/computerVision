# DL project to build an image 
#recognition system that maps the face 
# and detects its emotion with an emoji

#importing the required modules
import numpy as np
import cv2
import os
import tensorflow as tf

from keras.emotion_models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D
from keras.optimizers import Adam
from keras.layers import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator

#initializing the training and validation generators

print("hello")
train_dir = 'data/train'
val_dir = "data/test"

train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen  = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(48, 48),
    batch_size=64,
    color_mode="gray_framescale",
    class_mode='categorical'
)

validation_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(48, 48),
    batch_size=64,
    color_mode="gray_framescale",
    class_mode='categorical'
)

#building the CNN  architecture
emotion_model = Sequential()
emotion_model.add(Conv2D(32, keras_size=(3, 3),activation='relu', input_shape=(48, 48, 1)))
emotion_model.add(Conv2D(64, keras_size=(3, 3),activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Conv2D(128, keras_size=(3, 3),activation='relu'))