
raw_dict = {
	"1": "One",
	"5": "Five",
	"3": "Three",
	"4": "Four",
	"2": "Two",
}

# Sort by key

for key in sorted(raw_dict):
    print("{key}: {value}".format(key=key, value=raw_dict[key]))


# Sort by value

for key, value in sorted(raw_dict, key=lambda k,v: (v,k)):
    print("{key}: {value}".format(key=key, value=value))