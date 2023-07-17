spis = []


def summa():

    print(sum(spis))


while True:
    s = input()
    if s == 'stop':
        summa()
        break
    else:
        spis.append(int(s))
