def bigger_num(num):
    result = []
    counter = 0
    for i in num:
        result.append(i)
        result[counter] = int(result[counter])
        counter += 1
    result = sorted(result)
    result.reverse()
    print(result)


bigger_num('12345')
