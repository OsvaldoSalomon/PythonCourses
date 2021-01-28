import json

with open('dictionaryBand.txt') as f:
    data = f.read()

dictionaryFromFile = json.loads(data)
print(dictionaryFromFile)


def invert(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for item in val:
            if item not in inverse:
                inverse[item] = [key]
            else:
                inverse[item].append(key)
    return inverse


inverted_band = invert(dictionaryFromFile)
print(inverted_band)

file_handler = open('inverse_dictionary.txt', 'w')
file_handler.write(str(inverted_band))
file_handler.close()
