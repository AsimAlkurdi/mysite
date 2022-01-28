#!/usr/bin/python

import glob
import os
import pickle
from PIL import Image
from feature import feature

fe = feature()

for img_path in sorted(glob.glob('../media/img/*.jpg')):
    print(img_path)
    img = Image.open(img_path)
    feature = fe.ekstraksi(img)
    path_ciri = '../media/ciri/' + os.path.splitext(os.path.basename(img_path))[0] + '.pkl'
    pickle.dump(feature, open(path_ciri, 'wb'))
