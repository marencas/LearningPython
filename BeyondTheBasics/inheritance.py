# a little lesson on inheritance.
#
# in the following example i will be creating a parent class and two sub classes. the parent class will be
# called Animal and the sub classes will be Dog and Cat. the idea is to see how inheritance works by setting
# an attribute in the parent class that can be used in the child classes.
#
# the Animal class will contain the __init__ method which will be used to construct the object and it has a
# a parameter that can be used to set the animals name. this __init__ method will be shared with the subclasses
# therefore when creating a Dog object even though the Dog class does not have an __init__ method itself
# it can use the one from Animal. the Animal class will also have the eat method that will also be shared
# by the sub classes.
class Animal(object):
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print "{} is eating {}.".format(self.name, food)

class Dog(Animal):
    def fetch(self, thing):
        print "{} goes after the {}!".format(self.name, thing)

class Cat(Animal):
    def swatString(self):
        print "{} shreds the string!".format(self.name)

myDog = Dog("Rover")
myCat = Cat("Garfield")

myDog.fetch("socks")
myCat.swatString()
myCat.eat("kitten food")
myDog.eat("kibbles and bits")