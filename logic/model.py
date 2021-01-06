from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16


def classify(url):
    image = load_img("./" + url, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    label = decode_predictions(VGG16().predict(preprocess_input(image)))
    label = label[0][0]
    return label


if __name__ == "__main__":
    # example
    ans = classify("dog.png")
    print(ans)
