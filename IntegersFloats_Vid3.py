num = 3
print(type(num))

num = 3.1
print(type(num))

# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2 (drops decimal)
# Exponent:       3 ** 2 (to the power of)
# Modulus:        3 % 2 (to get remainder)(can also be used to check if a number is odd or even using 2. Modulus of any number with 2 will eitehr give 0 or 1 as remainder. If its 0 then even, if 1 then odd)
# Order of operations - BODMAS unless you put parenthesis around an operation

# Increment value (for any operators)
num = 1
num = num + 1
num = num * 10
#or
num += 1
num *= 10

num = -3
print(abs(num))

num = 3.75
print(round(num))
print(round(num,1)) #means round just the 1st number after decimal

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

num_1 = 3
num_2 = 2

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2) #all outputs will be boolean

num_1 = '100'
num_2 = '200'

print(num_1 + num_2) #will just concat 100 and 200 as they ae strings

num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)










