plants = [2, 4, 0, 8]
zombies = [1, 3, 5, 7]

plants_attack = sum(plants)
zombies_attack = sum(zombies)

plants_counter = 0
zombies_counter = 0


def attack(def_, att_):
    global plants_counter
    global zombies_counter
    if len(zombies) == len(plants):
        if def_[0] > att_[0]:
            plants_counter += 1
        if def_[0] == att_[0]:
            plants_counter += 0
            zombies_counter += 0
        else:
            zombies_counter += 1
        if plants_counter == zombies_counter:
            if plants_attack >= zombies_attack:
                return True
        if zombies_attack > plants_attack:
            return False


print(attack(plants, zombies))
