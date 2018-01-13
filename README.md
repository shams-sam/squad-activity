# squad-activity

### JSON Details
```
TRAIN_DATA      -> ['license', 'images', 'info', 'annotations']
        DIRECTDICT:  3 license  -> ['id', 'url', 'name']
        LISTOFDICT:  42029 images       -> ['imageId', 'url']
        DIRECTDICT:  6 info     -> ['dateCreated', 'url', 'year', 'description', 'version', 'contributor']
        LISTOFDICT:  62088 annotations  -> ['labelId', 'imageId', 'taskId']
TEST_DATA       -> ['images']
        LISTOFDICT:  33726 images       -> ['imageId', 'url']
VALID_DATA      -> ['images', 'info', 'license', 'annotations']
        LISTOFDICT:  8432 images        -> ['imageId', 'url']
        DIRECTDICT:  6 info     -> ['dateCreated', 'url', 'year', 'description', 'version', 'contributor']
        DIRECTDICT:  3 license  -> ['id', 'url', 'name']
        LISTOFDICT:  12406 annotations  -> ['imageId', 'labelId', 'taskId']
```
