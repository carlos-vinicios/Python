from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import decode_predictions,preprocess_input
from keras.preprocessing import image
import numpy as np

model = VGG16(weights='imagenet')

img_path = 'elephant.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
#x = x.reshape((1, x.shape[0], x.shape[1], x.shape[2]))
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

features = model.predict(x)

label = decode_predictions(features)
#label = label[0][0]

#print('%s (%.2f%%)' % (label[1], label[2]*100))
#print(decode_predictions(features, top=3)[0])

print(label)