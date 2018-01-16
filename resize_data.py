import cv2
import os
from tqdm import tqdm

import config
from utility import *

for _ in tqdm(os.listdir(config.TRAIN_IMAGES_DIR)):
    _ = config.TRAIN_IMAGES_DIR + "/" + _
    img = image_resize(_)
    image_write(img, _.replace(config.TRAIN_IMAGES_DIR, config.RESIZED_TRAIN_DIR))
    
for _ in tqdm(os.listdir(config.TEST_IMAGES_DIR)):
    _ = config.TEST_IMAGES_DIR + "/" + _
    img = image_resize(_)
    image_write(img, _.replace(config.TEST_IMAGES_DIR, config.RESIZED_TEST_DIR))
    
for _ in tqdm(os.listdir(config.VALID_IMAGES_DIR)):
    _ = config.VALID_IMAGES_DIR + "/" + _
    img = image_resize(_)
    image_write(img, _.replace(config.VALID_IMAGES_DIR, config.RESIZED_VALID_DIR))