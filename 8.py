def attack(def_, att_):
    plants_counter = len(def_)
    zombies_counter = len(att_)
    plants_attack = sum(def_)
    zombies_attack = sum(att_)
    for index, value in enumerate(def_):
        try:
            if def_[index] > att_[index]:
                zombies_counter -= 1
            elif def_[index] == att_[index]:
                plants_counter -= 1
                zombies_counter -= 1
            else:
                plants_counter -= 1
        except IndexError:
            zombies_counter -= 1
    if plants_counter == zombies_counter and plants_attack >= zombies_attack:
        return True
    if plants_counter > zombies_counter:
        return True
    if zombies_attack > plants_attack:
        return False
    if zombies_counter > plants_counter:
        return False


print(attack([2, 4, 6, 8], [1, 3, 5, 7]))
print(attack([2, 4], [1, 3, 5, 7]))
print(attack([2, 4, 0, 8], [1, 3, 5, 7]))
print(attack([1, 2, 1, 1], [2, 1, 1, 1]))
