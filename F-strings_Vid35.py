first_name = 'Mary'
second_name = 'Jane'

#conventional way
sentence = "My name is {} {}".format(first_name,second_name)
print(sentence)

#f-string way
sentence = f"My name is {first_name} {second_name}"
print(sentence)

#can use other functions with f-string
sentence = f"My name is {first_name.upper()} {second_name.upper()}"
print(sentence)

#using f-string for dict values
person = {'name': 'Jane', 'age': 23}
sentence = f"My name is {person['name']} and I am {person['age']} years old"
print(sentence)

#other examples of using f-string
calculation = f"4 multiplied by 11 is {4 * 11}"
print(calculation)

for i in range (1,11):
    sentence = f"The value is {i}"
    print(sentence)

#if you want the numbers to be preceded by 0 
for i in range(1,11):
    sentence = f"The value is {i:02}" #0 is the preceding 0 and 2 is the number of digits
    print(sentence)

#floating numbers. If you want a specific number of decimal points
pi = 3.14159265

sentence = f"Pi value is {pi:.4f}" #4 is the number of decimal points and f denotes floating point
print(sentence)

#with datetime
from datetime import datetime

birthday = datetime(1992, 1, 1)

sentence = f"Jane's birthday is on {birthday:%B %d, %Y}"
print(sentence)