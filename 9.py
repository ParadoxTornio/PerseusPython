def temperature_converter(temperature, f_c):
    if f_c == "c":
        print(round((temperature * 9 / 5 + 32), 3))
    elif f_c == "f":
        print(round((temperature - 32 * 5 / 9), 3))


temperature_converter(1, 'c')
