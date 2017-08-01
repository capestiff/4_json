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
    "type": "FeatureCollection",
    "features": [
        {
            "geometry": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
            "type": "Feature",
            "properties": {
                "RowId": "79742784-9ef3-4543-bc98-a219a8903c18",
                "DatasetId": 1854,
                "ReleaseNumber": 2,
                "VersionNumber": 1,
                "Attributes": {
                    "TypeService": "реализация продовольственных товаров",
                    "IsNetObject": "да",
                    "AdmArea": "Западный административный округ",
                    "Name": "Ароматный Мир",
                    "District": "район Кунцево",
                    "WorkingHours": [
                        {
                            "DayOfWeek": "понедельник",
                            "Hours": "09:30-22:30"
                        },
                        {
                            "DayOfWeek": "вторник",
                            "Hours": "09:30-22:30"
                        },
                        {
                            "DayOfWeek": "среда",
                            "Hours": "09:30-22:30"
                        },
                        {
                            "DayOfWeek": "четверг",
                            "Hours": "09:30-22:30"
                        },
                        {
                            "DayOfWeek": "пятница",
                            "Hours": "09:30-22:30"
                        },
                        {
                            "DayOfWeek": "суббота",
                            "Hours": "09:30-22:30"
                        },
                        {
                            "DayOfWeek": "воскресенье",
                            "Hours": "09:30-22:30"
                        }
                    ],
                    "ClarificationOfWorkingHours": null,
                    "OperatingCompany": "Ароматный Мир",
                    "global_id": 14371450,
                    "Address": "улица Академика Павлова, дом 10",
                    "PublicPhone": [
                        {
                            "PublicPhone": "(495) 777-51-95"
                        }
                    ]
                }
            }
        },
...

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
