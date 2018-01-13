import json
import config
from urllib.request import urlretrieve
from tqdm import tqdm
import sys

input_params = sys.argv

def prompt():
    print("All required parameters not passed.")
    print("Execute using the following format:")
    print("python downloader.py {TRAIN_IMAGES|TEST_IMAGES|VALID_IMAGES|ALL} {start_at_index} {end_before_index}")

try:
    assert len(input_params) == 4
except:
    prompt()
    exit(0)

name = input_params[1]
start_at = input_params[2]
end_before = input_params[3]

# reference: https://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file
log_file = open(config.LOG_DIR + "/" + name + "_" + start_at + "_" + end_before + ".log", 'w') 
print("Logging to file: ", config.LOG_DIR + "/" + name + "_" + start_at + "_" + end_before + ".log")

def close_conn():
    log_file.close()

position = {
    'TRAIN_IMAGES': 0,
    'TEST_IMAGES' : 1,
    'VALID_IMAGES': 2
}

download_configuration = [
    {
        'name' : 'TRAIN_IMAGES',
        'json' : config.TRAIN_DATA_FILE,
        'dir'  : config.TRAIN_IMAGES_DIR
    },
    {
        'name' : 'TEST_IMAGES',
        'json' : config.TEST_DATA_FILE,
        'dir'  : config.TEST_IMAGES_DIR
    },
    {
        'name' : 'VALID_IMAGES',
        'json' : config.VALID_DATA_FILE,
        'dir'  : config.VALID_IMAGES_DIR
    }
]

if name == 'ALL':
    selected_config = download_configuration
elif name in position:
    selected_config = [download_configuration[position[name]]]
else:
    close_conn()
    prompt()
    exit(1)

for _ in selected_config:
    print("Downloading: ", _['name'], ' from ', start_at, ' to ', end_before)
    data = json.load(open(_['json']))
    for image in tqdm(data['images'][int(start_at): int(end_before)]):
        FOUND = False
        for url in image['url']:
            try:
                # reference: http://stackabuse.com/download-files-with-python/
                urlretrieve(url, _['dir'] + "/" + image['imageId'] + ".jpg")
                FOUND = True
                break
            except:
                continue
        if not FOUND:
            log_file.write("NOT FOUND: " + image['imageId'] + "\n")

close_conn()
