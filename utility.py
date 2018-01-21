import cv2
import numpy as np
from socket import timeout
from urllib.error import HTTPError, URLError
import urllib.request
from tensorflow.python.client import device_lib

def check_devices():
    for _ in device_lib.list_local_devices():
        print("Device List")
        print("\t", _.device_type)
        print("\t\tname:", _.name)
        print("\t\tmemory_limit:", _.memory_limit)

def download(url, image_path, TIMEOUT=10):
    """
    Throws HTTPError, URLError or Timeout.
    Response is a byte object. 
    Hence, file open in wb mode.
    """
    response = urllib.request.urlopen(url, timeout=TIMEOUT).read()
    file = open(image_path, 'wb')
    file.write(response)
    file.close()

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
        
def image_location(img_id, parent_dir, img_ext='.jpg'):
    return parent_dir + "/" + img_id +  img_ext