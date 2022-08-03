#Classes allow us to logically group our data and functions in a way that is easy to reuse and also easy to build upon if need be
#a class has a constructor (__init__) that defines the attributes of the class
#self is the instance (object) you create for the class
#self.argument is the instance variable defined in the constructor, so any instance you create wil automatically have the attributes of the class
#functions defined inside a class are called methods

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@companyname.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1 = Employee('Jane', 'Doe', 30000)
emp_2 = Employee('John','Dave', 35000)

print(emp_2.fullname())

print(emp_2.first)
