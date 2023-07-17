filename = 'number.txt'
numbers = []
with open(filename) as file:
    for line in file:
        numbers.append(int(line))

    result = sum(numbers) / len(numbers)
    print(result)
