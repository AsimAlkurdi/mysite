import numpy as np
from keras.models import Model
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input


class feature:
    def __init__(doi):
        basis_model = VGG16(weights='imagenet')
        doi.model = Model(inputs=basis_model.input, outputs=basis_model.get_layer('fc1').output)

    def extract(doi, img):
        img = img.resize((224, 224))
        img = img.convert('RGB')
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        ciri = doi.model.predict(x)[0]
        return ciri / np.linalg.norm(ciri)
