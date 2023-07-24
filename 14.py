def summa(n):
    result = 0
    for i in n:
        if result >= 0:
            result += i
            if result == 0:
                break
    return result


print(summa([1, 4, 6, -11, 5]))
