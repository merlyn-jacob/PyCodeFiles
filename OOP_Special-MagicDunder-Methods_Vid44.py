#dunder methods are __repr__ , __str__. These special methods help in changing some builtin behaviours and operations
#dunder here means double underscore
# repr is an unambigous represenation of the object. Used for developers for debugging, logging etc..
# str is a readable representation of the object and is meant to be used for end-users

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1) #this does not print out the object as is created above, instead gives an ambiguous output like - <__main__.Employee object at 0x000002A76BEEFFD0>

#this can be changed by creating a dunder repr method to define how the object should be printed out as we desire

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1) #now this prints out the object as created - Employee(Corey, Schafer, 50000)

#when we add dunder str method, and print(emp_1), it will print give str output over repr output
#repr output is a fallback if str is not defined. So, as min, repr needs to be defined 

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1) #this pritns out str output over repr output

#we can stil call out repr outputs and str outputs if needed

print(repr(emp_1)) #or print(emp_1.__repr__())
print(str(emp_1)) #or print(emp_1.__str__())

#dunder methods can also be used for arithmetic operations

#say we want to find out combined salary of employees by just adding the instances together
#normally of we do print(emp_1 + emp_2), this will throw error.
#but if we define a dunder method for adding the pay, above will work

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)
    
    def __add__(self,other): #here self is one emp instance and other is other emp instance
        return self.pay + other.pay

    #similarly if we want to find out length of an employee's full name just by using len(instance/object)
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2)
print(len(emp_1))

# so basically we can define outputs we want from just the object via special methods (dunder) 

#reference doc - https://docs.python.org/3/reference/datamodel.html#special-method-names



