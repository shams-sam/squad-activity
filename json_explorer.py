import json
import config

files = {
    'TRAIN_DATA': config.TRAIN_DATA_FILE, 
    'TEST_DATA' : config.TEST_DATA_FILE, 
    'VALID_DATA': config.VALID_DATA_FILE
}

for data_type, json_file in files.items():
    data = json.load(open(json_file))
    print(data_type, "\t->", list(data.keys()))
    for key in data.keys():
        if type(data[key])==dict:
            print('\tDIRECTDICT: ', len(data[key]), key, "\t->", list(data[key].keys()))
        if type(data[key])==list:
            print('\tLISTOFDICT: ', len(data[key]), key + "\t->", list(data[key][0].keys()))
    