# -*- coding: utf-8 -*-

raw_dict = {
	"1": "One",
	"5": "Five",
	"3": "Three",
	"4": "Four",
	"2": "Two",
}

# Sort by key
print("Sort by key:")
for key in sorted(raw_dict):
    print("{key}: {value}".format(key=key, value=raw_dict[key]))

# Sort by value
print("Sort by value:")
for x in sorted(raw_dict.items(), key=lambda x: x[1]):
    print("{key}: {value}".format(key=x[0], value=x[1]))

"""
Словарь в Python - это неупорядоченная структура данных, в связи с этим нельзя отсортировать словарь как таковой,
но можно отсортировать хранимые им данные для организации/упорядочивания перед их выводом/обработкой.
"""
