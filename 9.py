def temperature_converter(temperature, f_c):
    if f_c == "c":
        print(temperature * 9 / 5 + 32)
    elif f_c == "f":
        print(temperature - 32 * 5 / 9)


temperature_converter(1, 'c')
