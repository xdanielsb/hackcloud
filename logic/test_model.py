import pytest
import tensorflow as tf
from model import classify, preprocess_and_decode


def test_preprocess_and_decode():
    try:
        filename = "./dog.png"
        image = tf.io.encode_base64(tf.io.read_file(filename))
        preprocess_and_decode(image, isb64=True)
    except Exception:
        pytest.fail("Unexpected Exception ..")


def test_classify():
    filename = "./dog.png"
    image = tf.io.encode_base64(tf.io.read_file(filename))
    assert classify(image, isb64=True)[1] == "vizsla"
