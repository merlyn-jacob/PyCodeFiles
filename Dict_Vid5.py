#dictionary = key:value
student = {'name': 'John', 'age': 25, 'courses':['Math', 'CompSci']}
print(student)

#access a key - key in square bracket
print(student['name'])

#if you try to access a key that does not exist, it throws a key error. If you intead need it to say None or some default value instead of key error, use get() method
print(student.get('phone'))

print(student.get('phone', 'Not found')) #to get a custom value as return

#modify a value
student['phone'] = '555-5555'
print(student)

#modify multiple values in one go - use update method, takes a dict as input
student.update({'name':'Jane', 'age':26, 'phone': '555-5556'})
print(student)

#delete a value
del student['age']
print(student)

popped = student.pop('name')
print(student)
print(popped)

student = {'name': 'John', 'age': 25, 'courses':['Math', 'CompSci']}
print(student)

#iterating through dict
print(len(student))

print(student.keys())
print(student.values())
print(student.items())

for key,value in student.items():
    print(key,value)
