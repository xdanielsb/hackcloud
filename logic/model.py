# from keras.preprocessing.image import load_img
import numpy as np
import tensorflow as tf
from keras.applications.vgg16 import (VGG16, decode_predictions,
                                      preprocess_input)
from keras.preprocessing.image import img_to_array


def preprocess_and_decode(img, isb64, new_shape=[224, 224]):
    if isb64:
        img = tf.io.decode_base64(img)
        img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.resize(img, new_shape, method=tf.image.ResizeMethod.BILINEAR)
    return img


def classify(image, isb64=False):
    # image = load_img("./" + url, target_size=(224, 224))
    image = preprocess_and_decode(image, isb64)
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    img = np.copy(image)
    label = decode_predictions(VGG16().predict(preprocess_input(img)))
    return label[0][0]


if __name__ == "__main__":
    # example
    ans = classify("dog.png")
    print(ans)
