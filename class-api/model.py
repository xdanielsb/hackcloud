from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.resnet import preprocess_input, decode_predictions, ResNet50


def classify(url):
    image = load_img("./" + url, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    label = decode_predictions(ResNet50().predict(preprocess_input(image)))
    label = label[0][0]
    return label


if __name__ == "__main__":
    # example
    ans = classify("balloon.jpg")
    print(ans)
