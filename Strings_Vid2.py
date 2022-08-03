print ('Hello World')

message = 'Hello World'
print(message)

message = "Bobby's world"
print(message)

message = """Bobby's world was a good
cartoon in 1990's"""
print(message)

message = 'Hello World'
print(message)

#upper and lowercase
print(message.upper())

print(message.lower())

#length of the string
print(len(message))

print(message.count('Hello')) #count will give the count of the inputted string in teh entire message variable

print(message.count('l'))  

#indexing - starts with 0, also has negative indexing wherein last character starts with -1
print(message[0])

print(message[0:6]) #second index is not inclusive of the value you enter so it should be length-1

print(message[:5])

print(message[6:])

print(message[-1])

print(message[-5:])

#find index of the string
print(message.find('World'))

#replace strings
new_message = message.replace('World','Universe')
print(new_message) #replace does not make replacements inplace

#to concat strings
#using +

greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + '. Welcome!'
print(message)

#using format
message = '{}, {}. Welcome!'.format(greeting,name)
print(message)

#using f string
message = f'{greeting}, {name.upper()}. Welcome!'
print(message) #using this allows you to code inside the placeholder as shown above wherein you can use functions on teh variables depending on how the desired output is

#to find out the methods/functions that can be used on an object/variable
print(dir(name))

#to find info on how to use methods/functions,their description etc.. in general on an object
print(help(str))

#to find info on how to use specific methods/functions,their description etc..on an object
print(help(str.lower))









