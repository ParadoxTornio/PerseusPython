l_t = [2, 3, 7, 9, 10, 4, 12, 29, 19, 15, 97]
result = []


def is_prime(number):
    if number == 2 or number == 3 or number == 7:
        return True
    if (number % 2 == 0
            or number % 3 == 0
            or number % 4 == 0
            or number % 5 == 0
            or number % 6 == 0
            or number % 6 == 0
            or number % 7 == 0
            or number % 8 == 0
            or number % 9 == 0):
        return False
    else:
        return True


for i in l_t:
    if is_prime(i):
        result.append(i)
print(result)
