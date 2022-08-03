#property decorator allows us to define Class methods that we can access like attributes.
#
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

#if we set attr 'first' as another name, it changes the first name and full name but not the email
#so to tackle that, we can create a method for email as a property decorator so it does not break the code for others who use this class-
#with email as an attr. property decorator allows us to continue using email as attr

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

#now say we want to set fullname into another name and also have the first name, last name and email change accordingly,
#we can do this by first setting proerty decorator on top of fullname method so it can accessed as attr, then
#we need a seperate setter decorator for the fullname method for it take up the argument of another name

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property         #for this to be accessed as attribute
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = 'Jane Doe'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

#now say we want to delete an attribute and clean up after that, we can use deleter 

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property         #for this to be accessed as attribute
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name')
        self.first = None
        self.last = None
        

emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
