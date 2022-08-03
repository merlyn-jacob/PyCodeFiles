

#conventional way
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result

my_nums = square_numbers([1,2,3,4,5])
print(my_nums)

#use generator - yield is the keyword

def square_numbers(nums):
    for i in nums:
        yield i*i

my_nums = square_numbers([1,2,3,4,5])
print(my_nums) #this will not give the list as output. generators (yield) do not hold the entire result in memory, it gives output one at a time

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

#instead of using next so many times, can use for loop

for num in my_nums:
    print(num)

#can use list comprehension to get a generator object

my_nums = (x*x for x in [1,2,3,4,5])
for num in my_nums:
    print(num)

#print(list(my_nums)) this is to convert the generator object to list but you will lose out on generator advantages

#generators results in performance boost in terms of memory and execution time.
#it does not hold all values in memory. This is relevant when there are millions of items to iterate through
#example below to compare a conventional list output and generator

import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))

def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

t1 = time.clock()
people = people_list(1000000)
#t2 = time.clock()

#t1 = time.clock()
#people = people_generator(1000000)
#t2 = time.clock()

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
print('Took {} Seconds'.format(t2-t1))

