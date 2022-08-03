courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

print(len(courses))

print(courses[0:2])

#add a value to the end of the list
courses.append('Art')
print(courses)

#add value in a specific position
courses.insert(1, 'Art')
print(courses)

#add another list to existing list
courses_2 = ['Art', 'Education']

courses.insert(1, courses_2) #this will insert the list as is inside the existing list
print(courses)

print(courses[1])

courses.extend(courses_2) #this will add the content of the list to the end of the existing list
print(courses)

#remove values
courses.remove('Art')
print(courses)

courses.remove(['Art', 'Education'])
print(courses)

courses.pop() #by default it will remove the last value
print(courses)

popped = courses.pop()
print(popped)

courses.pop()
print(courses)

#to reverse the order of the list
courses.reverse()
print(courses)

#to sort the list. Default is ascending
courses.sort()
print(courses)

courses.sort(reverse = True) #for descending order
print(courses)

#sort does changes inplace. If dont want changes inplace, use sorted() function
sorted_courses = sorted(courses)
print(sorted_courses)

nums = [2,5,3,1,4]

print(min(nums))
print(max(nums))
print(sum(nums))

#to find index of a value
print(courses.index('CompSci'))

#to find out is a value exists in a list
print('Art' in courses)
print('Math' in courses)

#to iterate through each value in the list
for i in courses:
    print(i)

#to iterate through each value and also get the index of each value
for index, course in enumerate(courses):
    print(index, course)

for index,course in enumerate(courses, start=1):
    print(index,course)

#to convert a list into comma seperated or any other symbol seperated string
courses_str = ', '.join(courses)
print(courses_str)

courses_str = ' - '.join(courses)
print(courses_str)

#convert the seperated string back to list
new_list = courses_str.split(' - ')
print(new_list)

# Tuples
# Lists - Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


# Tuples - Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' this will throw error as tuples cannot be modified

# Sets - only holds unique values. Each time you print out a set, the order of the values keep changing
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

#to find out common values in both sets
print(cs_courses.intersection(art_courses))

#to find out uncommon values in both sets
print(cs_courses.difference(art_courses))




























