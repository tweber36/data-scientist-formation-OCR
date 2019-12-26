import sys
import cv2
import pickle

import numpy as np

from keras.models import load_model

def main(image_path):
    model = load_model('tl_fine_tuning_120')

    img = cv2.imread(image_path)
    img = cv2.resize(img, (100, 100))
    img = np.reshape(img, (-1, 100, 100, 3)) / 255

    with open('classes_encoding_120', 'rb') as f:
        classes_labels = pickle.load(f)

    print(f"\n\nPredicted breed: {classes_labels[model.predict_classes(img)[0]]}")

if len(sys.argv) > 1:
    main(sys.argv[1])
