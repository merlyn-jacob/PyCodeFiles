#Inheritance allows us to inherit attributes and methods from a parent class. 
# This is useful because we can create subclasses and get all of the functionality of our parents class,
# and have the ability to overwrite or add completely new functionality without affecting the parent class in anyway

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

class Developer(Employee):
    pass

dev_1 = Developer('Mary', 'Jane', 50000)
dev_2 = Developer('John', 'Doe', 60000)

print(dev_1.pay) #here we can see it prints out the pay of 50k as it inherits the attribute of employee class

dev_1.apply_raise()
print(dev_1.pay)

#now we add additional attributes to just developer class
#as per the method order resolution, python first checks if the child class has any attr. If yes, that is applicable first
#if no attr. in child class, it looks into parent class. If not there, it looks into builtins

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

class Developer(Employee):
    raise_amt = 1.10

dev_1 = Developer('Mary', 'Jane', 50000)
dev_2 = Developer('John', 'Doe', 60000)

print(dev_1.pay)

dev_1.apply_raise()
print(dev_1.pay)  #this will apply 10% raise of child class and not 4% raise of parent class

#check for method order resolution by help(class)

#if you want to add more arguments to your child class which is not needed in the parent class

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

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)   #this ensures that first,last and pay are handled as per parent class
        self.prog_lang = prog_lang

dev_1 = Developer('Mary', 'Jane', 50000, 'Python')
dev_2 = Developer('John', 'Doe', 60000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)

#create a manager child class, add argument to take in the list of employees managed by manager, methods to add and remove employees to the list

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        self.employees.append(emp)

    def remove_emp(self, emp):
        self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('---> {}'.format(emp.fullname()))


dev_1 = Developer('Mary', 'Jane', 50000, 'Python')
dev_2 = Developer('John', 'Doe', 60000, 'Java')
mgr_1 = Manager('Janet', 'Smith', 70000, [dev_1])

print(mgr_1.email)
print(mgr_1.print_emps())

mgr_1.add_emp(dev_2)
print(mgr_1.print_emps())

#some built in functions

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))

#check out subclassing of Exception module
