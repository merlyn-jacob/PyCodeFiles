#regular methods are methods defined inside a class that take only instance (self) as argument
#Class methods are methods that automatically take the class as the first argument. 
#Class methods can also be used as alternative constructors.
#you can convert a regular method to a class method using @classmethod decorator

from datetime import datetime


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount): #takes class as argument
        cls.raise_amt = amount

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.raise_amt)
print(emp_2.raise_amt)
print(Employee.raise_amt)

Employee.set_raise_amt(1.05)

print(emp_1.raise_amt)
print(emp_2.raise_amt)
print(Employee.raise_amt)

#using clas methods as alternative constructors
#if there is a scenario wherein the employees details are received as strings, and in order to create those employee records using class,
#we would have to parse the string each time and then create those records using class as below:

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)

#instead of doing above (parsing everytime manually), we can create a class method that defines parsing function and
#use that method directly on the string variable so it creates the employee record directly

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount): #takes class as argument
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_2.email)
print(new_emp_2.pay)

#static methods are methods that do not take a class or instance as argument
#static method has some logical connection to the class but does not depend on the class or instance 
#create a static method using @staticmethod decorator

#use case - you need to find if a particular date is a weekday or not

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount): #takes class as argument
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:  #monday stands for weekday number 0 and sunday is 6
            return False
        return True

import datetime
my_date = datetime.date(2022, 7, 23)

print(Employee.is_workday(my_date))


