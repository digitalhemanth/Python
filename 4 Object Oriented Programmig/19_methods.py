#Methods


'''
Methods are functions defined inside the body of a class.
They are used to define the behaviors of an object.
'''

class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()

#The __init__ method : 

'''
There are many method names which have special significance in Python classes.
We will see the significance of the __init__ method now.

The __init__ method is run as soon as an object of a class is instantiated (i.e. created). 
The method is useful to do any initialization (i.e. passing initial values to your object) you 
want to do with your object.

 Notice the double underscores both at the beginning and at the end of the name.
 '''
class Person_My:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person_My('Hemanth')
p.say_hi()
# The previous 2 lines can also be written as
# Person_My('Hemanth').say_hi()


