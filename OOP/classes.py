

class Animal(object):
    """
    Classes are encapsulated collections of
    attributes (variables) and functions (methods).
    This one represents an Animal.
    """

    # Class variables
    num_legs = 4
    trait = "wild"

    def __init__(self, name):
        """
        The __init__ method runs whenever an instance is created of the class.
        Animal("Spot") -> instance of Animal named Spot
        """
        # Instance variables
        self.age = 0
        self.name = name

    def have_birthday(self):
        """
        This is a custom method, which increments the age instance variable by 1.
        """
        self.age += 1

    def talk(self):
        """
        This can be overridden in subclasses, but let's have a default.
        """
        print "Grr"


class Dog(Animal):

    trait = "friendly"

    def talk(self):
        print "Bark!!"
