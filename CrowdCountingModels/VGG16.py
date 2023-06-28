from keras.applications.vgg16 import VGG16, preprocess_input
from keras.utils import img_to_array, load_img

import numpy as np

vgg_model = VGG16(weights='imagenet', include_top=False)


def extract_features(img_path):
    img = load_img(str(img_path), target_size=(224, 224))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = vgg_model.predict(x)
    return features
