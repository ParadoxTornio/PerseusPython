plants = [2, 4]
zombies = [1, 3, 5, 7]

plants_attack = sum(plants)
zombies_attack = sum(zombies)

plants_counter = 0
zombies_counter = 0


def attack(def_, att_):
    global plants_counter
    global zombies_counter
    for index, value in enumerate(plants):
        try:
            if def_[index] > att_[index]:
                plants_counter += 1
            elif def_[index] == att_[index]:
                plants_counter += 0
                zombies_counter += 0
            else:
                zombies_counter += 1
        except IndexError:
            plants_counter += 1
    if plants_counter == zombies_counter and plants_attack >= zombies_attack:
        return True
    if plants_counter > zombies_counter:
        return True
    if zombies_attack > plants_attack:
        return False
    if zombies_counter > plants_counter:
        return False


print(attack(plants, zombies))
