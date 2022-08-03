#the aspects of being "Pythonic".
#basically it means that you are following conventions and coding styles of the Python language in order to write clean and readable code.

#duck typing - dont care about what the object is, it should do what we code

class Duck:
    def quack(self):
        print('Quack, Quack')

    def fly(self):
        print('Flap, Flap')

class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")

#we defined two classes of Duck and Person. Both has quack and fly  methods defined

#now we instantiate an object for each class

d = Duck()
p = Person()

#now we create a function to use quack and fly methods no matter the type of object - duck or person

def quack_and_fly(thing):
    #Not Duck-Typed (Non-Pythonic) here we restrict/add checks to execute code only if its a certain obect
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print('This has to be a Duck!')

quack_and_fly(p)
quack_and_fly(d)

def quack_and_fly(thing):
    #duck-typed. this will execute the code irrespective of the type of object
    thing.quack()
    thing.fly()

quack_and_fly(p)
quack_and_fly(d)

def quack_and_fly(thing):
    #LBYL (Non-Pythonic) #asks for permissions before executing what we want
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()
    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()

quack_and_fly(p)
quack_and_fly(d)

def quack_and_fly(thing):
    #can be handled by EAFP
    try:
        thing.quack()
        thing.fly()
    except AttributeError as e:
        print(e)

quack_and_fly(p)
quack_and_fly(d)

def quack_and_fly(thing):
    #can be handled by EAFP
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

quack_and_fly(p)
quack_and_fly(d)

#more examples:

person = {'name': 'Jess', 'age': 23, 'job': 'Programmer'}

#non-pythonic
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name} and {age} years old. I work as a {job}".format(**person))
else:
    print('Missing some keys')

#pythonic
try:
    print("I'm {} and {} years old. I work as a {}".format(person['name'], person['age'], person['job']))
except KeyError as e:
    print(e)

person = {'name': 'Jess', 'age': 23}

#non-pythonic
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name} and {age} years old. I work as a {job}".format(**person))
else:
    print('Missing some keys')

#pythonic
try:
    print("I'm {} and {} years old. I work as a {}".format(person['name'], person['age'], person['job']))
except KeyError as e:
    print("Missing {} key".format(e))

my_list = [1,2,3,4,5,6]
#non-pythonic
if len(my_list) >= 6:
    print(my_list[5])
else:
    print('That index does not exist')

#pythonic
try:
    print(my_list[5])
except IndexError:
    print('That index does not exist')

my_list = [1,2,3,4,5]
#non-pythonic
if len(my_list) >= 6:
    print(my_list[5])
else:
    print('That index does not exist')

#pythonic
try:
    print(my_list[5])
except IndexError:
    print('That index does not exist')



