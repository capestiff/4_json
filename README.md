# Prettify JSON

The program reads the path to the JSON file as an argument and pretty-prints the content of it. 

# Quickstart

```
#!bash

$ python pprint_json.py <path_to_file> 
```
```
$ python pprint_json.py -h
usage: pprint_json.py [-h] path_to_file

positional arguments:
  path_to_file  program reads JSON file and prints the content
```

Example of script launch on Linux, Python 3.5:

```
$ python pprint_json.py data.json

{ 
'features': [
              {'geometry': {'coordinates': [37.72775243734561,
                                            55.61668660260342],
                            'type': 'Point'},
               'properties': {'Attributes': {'Address': 'Борисовский проезд, '
                                                        'дом 40А',
                                             'AdmArea': 'Южный '
                                                        'административный '
                                                        'округ',
                                             'ClarificationOfWorkingHours': None,
                                             'District': 'район '
                                                         'Орехово-Борисово '
                                                         'Северное',
                                             'IsNetObject': 'нет',
                                             'Name': 'Разливные напитки',
                                             'OperatingCompany': None,
                                             'PublicPhone': [{'PublicPhone': '(926) '
                                                                             '281-82-60'}],
                                             'TypeService': 'реализация '
                                                            'продовольственных '
                                                            'товаров',
                                             'WorkingHours': [{'DayOfWeek': 'понедельник',
                                                               'Hours': '10:00-21:00'},
                                                              {'DayOfWeek': 'вторник',
                                                               'Hours': '10:00-21:00'},
                                                              {'DayOfWeek': 'среда',
                                                               'Hours': '10:00-21:00'},
                                                              {'DayOfWeek': 'четверг',
                                                               'Hours': '10:00-21:00'},
                                                              {'DayOfWeek': 'пятница',
                                                               'Hours': '10:00-21:00'},
                                                              {'DayOfWeek': 'суббота',
                                                               'Hours': '10:00-21:00'},
                                                              {'DayOfWeek': 'воскресенье',
                                                               'Hours': '10:00-21:00'}],
                                             'global_id': 171714979},
                              'DatasetId': 1854,
                              'ReleaseNumber': 2,
                              'RowId': '4af7d0bb-be94-40fa-aaaa-b32ebdddc967',
                              'VersionNumber': 1},
               'type': 'Feature'}
               
               ...
               
               ],               
 'type': 'FeatureCollection'}

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
