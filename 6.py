dictionary = {1: 1, 2: 2, 3: 3, 4: 4, 6: 6}

values = list(dictionary.values())

dict_ = sum(values) / len(values)

for i in dictionary:
    dictionary[i] += dict_

print(dictionary)
