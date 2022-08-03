#first class functions - refer vid https://www.youtube.com/watch?v=kr0mpwqttM0&t=0s
#closures - refer vid https://www.youtube.com/watch?v=swU3c34d2NQ&t=0s

#Decorators are a way to dynamically alter the functionality of your functions. 
#So for example, if you wanted to log information when a function is run, you could use a decorator to add this functionality without modifying the source code of your original function.

from fileinput import filename
from logging import _Level


def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

#original function:
def display():
    print('display function ran')

#log the output from original function using decorator
decorator_display = decorator_function(display)
decorator_display()

#we can skip the above loggin output codes by adding @decorator_function above the original function
#as @decorator_function essentially means display = decorator_function(display)

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('display function executed')

display()

#decorators are used to alter the functionality of original fucntion without changing anything in the original function itself
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('display function executed')

display() #here it will first print wrapper executed before... statement and then print the display func output. but it did not change the original display func codes

#if your original function takes arguments, then it needs to be mentioned in the wrapper function as well

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs): #args and kwargs allows any number of positional arguments
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display_info(name,age):
    print("display_info ran with arguments ({}, {})".format(name,age))

display_info('John', 23)

#create a class as a decorator instead of function
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):  #this acts as the wrapper function
        print("call method executed this before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display_info(name,age):
    print("display_info ran with arguments ({}, {})".format(name,age))

display_info('John',23)


#use case for decorator function - find out how many times a function has run and using which arguments and keywords

#use logging module to create the decorator func

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

@my_logger
def display_info(name,age):
    print("display_info ran with arguments ({}, {})".format(name,age))

display_info('John',23)

#use case - how long it takes for a function to run

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in {} secs".format(orig_func.__name__, t2))
        return result

    return wrapper

@my_timer
def display_info(name,age):
    print("display_info ran with arguments ({}, {})".format(name,age))

display_info('John',23)

#if we need to decorate the same function with 2 decorators
#we can stack both decorators on top of the function
#but remember to import wraps from functools
#this ensures that the original function name is not changed to wrapper (since we return wrapper for both the decorators) when we stack two decorators

from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time


@my_logger
@my_timer #this runs first
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 22)
