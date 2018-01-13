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

### TASK Details

```
{'taskInfo': [
          {'taskId': '1', 'taskName': 'shoe:gender'},
          {'taskId': '2', 'taskName': 'shoe:age'},
          {'taskId': '3', 'taskName': 'shoe:color'},
          {'taskId': '4', 'taskName': 'shoe:up height'},
          {'taskId': '5', 'taskName': 'dress:decoration'},
          {'taskId': '6', 'taskName': 'dress:color'},
          {'taskId': '7', 'taskName': 'dress:material'},
          {'taskId': '8', 'taskName': 'dress:silhouette'},
          {'taskId': '9', 'taskName': 'shoe:type'},
          {'taskId': '10', 'taskName': 'shoe:closure type'},
          {'taskId': '11', 'taskName': 'pants:color'},
          {'taskId': '12', 'taskName': 'dress:length'},
          {'taskId': '13', 'taskName': 'outerwear:type'},
          {'taskId': '14', 'taskName': 'dress:occasion'},
          {'taskId': '15', 'taskName': 'outerwear:gender'},
          {'taskId': '16', 'taskName': 'shoe:toe shape'},
          {'taskId': '17', 'taskName': 'outerwear:color'},
          {'taskId': '18', 'taskName': 'shoe:heel type'},
          {'taskId': '19', 'taskName': 'outerwear:collar'},
          {'taskId': '20', 'taskName': 'outerwear:age'},
          {'taskId': '21', 'taskName': 'outerwear:material'},
          {'taskId': '22', 'taskName': 'pants:fit'},
          {'taskId': '23', 'taskName': 'pants:type'},
          {'taskId': '24', 'taskName': 'pants:decoration'},
          {'taskId': '25', 'taskName': 'pants:pattern'},
          {'taskId': '26', 'taskName': 'pants:material'},
          {'taskId': '27', 'taskName': 'outerwear:length'},
          {'taskId': '28', 'taskName': 'outerwear:sleeve length'},
          {'taskId': '29', 'taskName': 'dress:age'},
          {'taskId': '30', 'taskName': 'shoe:decoration'},
          {'taskId': '31', 'taskName': 'pants:age'},
          {'taskId': '32', 'taskName': 'pants:gender'},
          {'taskId': '33', 'taskName': 'outerwear:pattern'},
          {'taskId': '34', 'taskName': 'shoe:flat type'},
          {'taskId': '35', 'taskName': 'dress:sleeve length'},
          {'taskId': '36', 'taskName': 'shoe:material'},
          {'taskId': '37', 'taskName': 'dress:pattern'},
          {'taskId': '38', 'taskName': 'dress:collar'},
          {'taskId': '39', 'taskName': 'outerwear:closure type'},
          {'taskId': '40', 'taskName': 'dress:gender'},
          {'taskId': '41', 'taskName': 'shoe:back counter type'},
          {'taskId': '42', 'taskName': 'shoe:pump type'},
          {'taskId': '43', 'taskName': 'pants:rise type'},
          {'taskId': '44', 'taskName': 'pants:length'},
          {'taskId': '45', 'taskName': 'shoe:boot type'}
  ]
}
```
