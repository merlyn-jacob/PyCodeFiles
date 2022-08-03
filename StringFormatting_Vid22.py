person = {'name': 'Jenn', 'age': 23}

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old'
print(sentence)

sentence = 'My name is {} and I am {} years old.'.format(person['name'],person['age'])
print(sentence)

#or

sentence = 'My name is {0[name]} and I am {0[age]} years old'.format(person)
print(sentence)

#can do with a list too

l = ['Jenn', 23]

sentence = 'My name is {0[0]} and I am {0[1]} years old'.format(l)
print(sentence) #first 0 is index of the list/dict we pass in format. Other numbers are indexes of values in the list/dict

#can access attributes as well when formatting a string. Use .attribute
class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old'.format(p1)
print(sentence)

#can use keywords to format string

sentence = 'My name is {name} and I am {age} years old'.format(name = 'Jenn', age = 23)
print(sentence)

#can format a string with dict values as below as well
person = {'name': 'Jenn', 'age': 23}
sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)

#format string with numbers

for i in range(1,11):
    sentence = 'The value is {}.'.format(i)
    print(sentence)

#if you need to change the numbers to two or three digits when printing out, add : and the number of digits in the placeholder
for i in range (1,11):
    sentence = 'The value is {:02}.'.format(i)
    print(sentence)

for i in range (1,11):
    sentence = 'The value is {:03}.'.format(i)
    print(sentence)

#to print out specific decimal numbers, use :.<number of decimals>f inside the placeholder
pi = 3.14159265
sentence = 'Pi is equal to {:.3f}.'.format(pi)
print(sentence)

#to print put comma seperated numbers, use :, inside placeholder
sentence = '1 MB is equal to {:,}'.format(1000**2)
print(sentence)

#to print put decimals with above
sentence = '1MB is equal to {:,.2f}'.format(1000**2)
print(sentence)

#print out dates in specific formats

import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30 ,45)

sentence = '{:%B %d, %Y}'.format(my_date) #get details on which keywords to use for the date format in datetime documentation
print(sentence)

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year.'.format(my_date)
print(sentence)
#we add 0 because we are passing only one value in format and we have more than one placeholders.
#So its imp to add 0 index to indicate that it needs to use that one value for all placeholders.







