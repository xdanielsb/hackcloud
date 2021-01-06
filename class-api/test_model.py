from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.resnet import preprocess_input, decode_predictions, ResNet50
from keras.applications.nasnet import preprocess_input, decode_predictions, NASNetMobile
import pytest

def classify(url):
    image = load_img("./" + url, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    label =  decode_predictions(NASNetMobile().predict(preprocess_input(image)))
    label = label[0][0]
    return label

@pytest.mark.timeout(10)
def test_classify():
    assert classify("balloon.jpg")[1] == "balloon"