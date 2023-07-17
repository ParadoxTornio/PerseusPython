n = int(input())


def simple(number):
    if number == 2 or number == 3 or number == 7:
        print('простое')
    elif (number % 2 == 0
            or number % 3 == 0
            or number % 4 == 0
            or number % 5 == 0
            or number % 6 == 0
            or number % 6 == 0
            or number % 7 == 0
            or number % 8 == 0
            or number % 9 == 0):
        print('составное')
    else:
        print('простое')


while True:
    simple(n)
    n = int(input())
