import random


class Engine(object):

    restaurants = ["Laut", "Chipotle", "Eataly", "Sophie's Cuban", "Chop't", "Potbelly's"]

    def __init__(self, person):
        self.history = []
        self.person = person

    def recommend(self):
        random.shuffle(self.restaurants)
        for choice in self.restaurants:
            if choice not in self.history[-2:]:
                self.history.append(choice)
                return "{} should go to {} for lunch.".format(
                    self.person, choice)
