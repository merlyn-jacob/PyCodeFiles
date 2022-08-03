#functions - intructions packaged together to perform a task
#create a function using def

def hello_func():
    pass #pass keyword can be used when you do not want to define anything in your function

def hello_func():
    print('Hello Function')

hello_func() #here because print is used in function, the function need not be executed with a print func seperately. It just prints put the output

def hello_func():
    return 'Hello Function'

print(hello_func()) #here we need to use print to execute the function. Return produces the output equal to the data type of the output. We can use other functions in conjunction with the created fucntion if we use return. Other funcitons will apply on the executed returned output as per the data type.

print(hello_func().upper())

def hello_func(greeting):
    return '{} Function.'.format(greeting)

print(hello_func('Hi'))

def hello_func(greeting, name = 'You'):
    return '{} {}'.format(greeting,name) #one required parameter (positional arguments) + one that has a default value if the paramter is not fulfilled (keyword arguments)

print(hello_func('Hi'))

print(hello_func('Hi', name = 'Cory')) #can also bypass default value

#*args and **kwargs - args used when arbitrary number of positional arguments need to be passed and kwargs is for passing arbitrary number of keyword arguments

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age=22)

#create a seperate list and dict of postional and keyword arguments and pass it in the function
courses = ['Math', 'Art']
info = {'name':'John', 'age':22}

student_info(courses, info) #this will give output as positional argument - all in one line

#to unpack the values as list and dict, use asterisk
student_info(*courses, **info)

#example code
#Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years.""" #this is a docstring to document what the function does

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2017))
print(days_in_month(2017,2))








