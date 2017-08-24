# -*- coding: utf-8 -*-

import json

path = 'example.json'

# Reading JSON file
with open(path, 'r') as f:
    data = json.loads(f.read())

    # Get value for key "a"
    a_value = data["object"]["a"]

    # Insert value on the beginning of "array"
    data["array"].insert(0, a_value)

# Write changed data back into JSON file
with open(path, 'w') as f:   
    f.write(json.dumps(data, sort_keys=True, indent=4))

"""
Модуль pickle работает с бинарными данными и предназначен для сериализации/десериализации
объектов Python, в то время как JSON - это текстовый формат данных.
JSON файлы могут быть прочитаны людьми, а также широко используются в разных языковых экосистемах.
Модуль pickle может быть использован при работе с файлами если они будут использоваться только 
средствами Python, в таком случае производительность работы с данными будет выше.
Модуль json предпочтительнее использовать если необходима работа непосредственно с JSON файлами,
которые затем необходимо читать или редактировать людям, а также которые могут быть использованы
вне экосистемы Python.
"""
