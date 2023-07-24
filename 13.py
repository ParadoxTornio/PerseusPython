def bigger_num(num):
    result = []
    counter = 0
    for i in num:
        result.append(int(i))
        counter += 1
    result.sort(reverse=True)
    print(result)


bigger_num('12345')
