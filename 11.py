# class Human:
#     def __init__(self, name, age, height, weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#     def __str__(self):
#         return f'name:{self.name}, age:{self.age}, height:{self.height}, weight:{self.weight}'
#
#     def training(self, hours):
#         self.weight -= hours * 0.1
#
#     def get_name_lower(self):
#         return self.name.lower()
#
#
# human = Human('Perseus', 11, 153, 40)
# human.training(10)
# print(human)
# print(human.get_name_lower())

class Word:
    def __init__(self, word):
        self.word = word

    def get_upper(self):
        return self.word.upper()

    def get_lower(self):
        return self.word.lower()

    def get_letter_count(self, letter):
        counter = 0
        for i in self.word:
            if i == letter:
                counter += 1
        return counter


word = Word('letter')
print(word.get_letter_count('l'))
