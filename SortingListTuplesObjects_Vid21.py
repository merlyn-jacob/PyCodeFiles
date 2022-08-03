list_1 = [5,1,7,4,3,6,2,9,8]

#sort func will sort it in-place so there is no return value for this. So you cant store it in a variable

list_1.sort()
print(list_1)

#sorted method does not sort in-place so you can store it in a variable
list_1 = [5,1,7,4,3,6,2,9,8]
s_list = sorted(list_1)
print(s_list)
print(list_1)

s_list = sorted(list_1, reverse=True)
print(s_list)

#sort func cannot be used on tuple or dict. sorted can be used

tup = (5,1,7,4,3,6,2,9,8)
s_tuple = sorted(tup)
print(s_tuple)

dictionary = {'name' : 'John', 'age': 22, 'job': 'Programming'}
s_dict = sorted(dictionary)
print(s_dict) #this sorts the values alphabetically

#sort combo of negative and postive

list_2 = [-3,-2,1,-1,0,2,3]
s_list_2 = sorted(list_2)
print(s_list_2)

#to sort as absolute values
s_list_2 = sorted(list_2, key=abs)
print(s_list_2)

#sorting objects

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

#attributes in objects cannot be sorted without key. it will throw error as it wont know how to sort
#create a function that will act as the key

def e_sort(emp):
    return emp.name

s_employees = sorted(employees, key=e_sort) #this will sort based on alphabetical order of names
print(s_employees)

#similarly we can sort using age or salary. just replace the e_sort func accordingly

#def e_sort(emp)
    #return emp.age

#can also use lambda func for sorting attributes

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

s_employees = sorted(employees, key=lambda e: e.name)
print(s_employees)

#can also use a built-in func for sorting attributes

from operator import attrgetter

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

s_employees = sorted(employees, key=attrgetter('age'))
print(s_employees)































