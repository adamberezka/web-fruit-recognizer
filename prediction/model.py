import cv2
import numpy
import tensorflow as tf

class FruitModel:

    def __init__(self):
        self.model = self.load_model()
        with open('./model/class_names.txt') as file:
            self.class_names = [line.rstrip() for line in file]

    @staticmethod
    def load_model():
        fruits_model = tf.keras.models.load_model('./model/model.h5')
        return fruits_model

    def predict(self, image_path):
        image = cv2.imread(image_path)
        image = cv2.resize(image, (100, 100))
        data = numpy.ndarray(shape=(1, 100, 100, 3), dtype=numpy.int)
        image_array = numpy.asarray(image)
        data[0] = image_array
        y_pred = self.model.predict(data, 1)
        return self.class_names[numpy.argmax(y_pred)]
