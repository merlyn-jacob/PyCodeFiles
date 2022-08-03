import my_module as mm #you can directly import if the module you created is in the same directory a

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math') #have to use mm.function name everywheree as we have imported the whole module
print(index)

#we can also import specific function from module

from my_module import find_index, test
courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math') #here no need to type mm.func as we have imported the specific func itself
print(index)
print(test)

#python checks through a list of directories to find the module we are trying to import
#this list is called sys.path

import sys
print(sys.path)

#this list has the current directory we are working on, list of dir in python path env. variable, std. libraries, site packages

#if you try to import a module not in the same directory as you are runnign script, then it throws a ModuleNotFound error
#for this, you can add the directory where the module resides to sys.path and then import module

#import sys
#sys.path.append('add here new directory path')

#above method is not preferable as you are hardcoding it each time and would need to change each time in different places when needed
#instead, add the directory path in env.variable
#doubt - i created a new path under user variables for myjc. And when importing in cmd, it works but it does not work in an editor (IDLE that i use). So do we add the editor path to env variables??

#some commonly used modules in standard libraries - math, datetime, calendar

import math

rads = math.radians(90)
print(rads)

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2017))

import os
print(os.getcwd())

#to find out the location of any modules (py files), use __file__

print(os.__file__)




