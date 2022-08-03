#class variables are common attributes that apply to all instances of that class. V/S instance variables which are very specific to each instance created


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    #create a method to apply generic raise to all employee instances
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

#if we define the method as self.pay = int(self.pay * Employee.raise_amount), then we wont be able to make changes to raise amount for individual employee instance

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

Employee.raise_amount = 1.06

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount) #changes raise amount for every emp instance as raise amount is a class variable

#if we need to make changes in raise amt for specific emp instance, then it can be done as:
#this is possible because in the method we have defined as self.raise_amount instead of Employee.raise_amount

emp_1.raise_amount = 1.04

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

#to check attributes of a class or instance

print(emp_1.__dict__)
print(Employee.__dict__)

#another use case - get the number of employees 
class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1 #create this in init method as this runs each time an emp instance is created

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    #create a method to apply generic raise to all employee instances
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(Employee.num_of_emps)