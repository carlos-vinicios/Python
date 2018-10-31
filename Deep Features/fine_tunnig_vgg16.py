from keras.applications.vgg16 import VGG16
from keras.datasets import load_svmlight_file
from keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.models import Model, Sequential
from keras.layers import Dense, Activation
from keras import optimizers
import numpy as np

model_vgg16 = VGG16()

#necessario criar um novo modelo sequencial para após aproveitar as camadas da VGG16, adicionando uma a uma
model = Sequential()
for layer in model_vgg16.layers:
    model.add(layer)

model.layers.pop() # retira a última dense layer contendo as 1000 classes

for layer in model.layers: #congela as camadas iniciais do modelo para que não aprendam novas caracteristicas
    layer.trainable = False

model.add(Dense(2, activation='softmax')) #adicionamos uma nova dense layer como softmax, para classificação entre melanoma e não melanoma

model.compile(optimizers.Adam(lr=0.001), loss="categorical_crossentropy", metrics=['accuracy', 'precision', 'recall', 'f1'])

#model.fit_generator(train_batches, steps_per_epoch=4, validation_data=valid_batches, validation_steps=4, epochs=5, verbose=2)