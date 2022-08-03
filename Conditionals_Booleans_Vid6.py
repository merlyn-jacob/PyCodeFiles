#conditionals - what Python evaluates as true or false
#if elif else
language = 'Python'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

language = 'JavaScript'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

#and,or,not

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad creds')


user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad creds')

user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin page')
else:
    print('Bad creds')


user = 'Admin'
logged_in = False

if not logged_in:
    print('Please log in')
else:
    print('Welcome')

#object identity = is. This compares if two or more object's IDs are the same or not.
a = [1,2,3]
b = [1,2,3]

print(a == b) #will return true

print(a is b) #will return false
# this is because == will check for values and is will check for IDs of the objects

print(id(a))
print(id(b))

a = [1,2,3]
b = a

print(a is b)
print(id(a))
print(id(b))

# Values that are by default evaluated to False:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping (dict). For example, {}.

condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = []
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = {}
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

 






















