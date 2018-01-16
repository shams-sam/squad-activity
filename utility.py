import cv2
import numpy as np

def image_resize(img_path, MAX_PIXEL=299):
    img = cv2.imread(img_path)
    if type(img) != np.ndarray:
        return False
    l, w, c = img.shape
    assert l > c and w > c
    if l > w:
        l_new = MAX_PIXEL
        w_new = int(w/l*MAX_PIXEL)
    else:
        w_new = MAX_PIXEL
        l_new = int(l/w*MAX_PIXEL)
    img = cv2.resize(img, (w_new, l_new))
    
    return img

def image_write(img, path):
    if type(img)!=bool:
        cv2.imwrite(path, img)