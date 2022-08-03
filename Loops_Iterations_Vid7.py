#for loop - break, continue

nums = [1,2,3,4,5]

for num in nums:
    print(num)
#if you want to stop the iteration after finding a particular value

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

#if you want to continue with the iterating even after finding the particular value
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

#loop inside loop - inner loop completes then goes to outer
for num in nums:
    for letter in 'abc':
        print(num, letter)

#iterating through a range - in range, last value is not inclusive
for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

#while loops - it goes on forever so its imp to have a code that breaks out of the loop
x = 0

#while x < 10:
    #print(x) - this is a never ending loop. Need to add a code that breaks it

while x < 10:
    print(x)
    x += 1

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

#if you are stuck in a never ending loop, use ctrl+C to stop it
