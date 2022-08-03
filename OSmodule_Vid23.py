#The os module allows us to access functionality of the underlying operating system.
#So we can perform tasks such as: navigate the file system, obtain file information, rename files,
#search directory trees, fetch environment variables, and many other operations.

import os

#print(dir(os)) this gives list of all attributes and methods we have access to within os module

#get current working directory
print(os.getcwd())

#to change the directory
#print(os.chdir('<name of the dir>))

#to list down files and folders in current directory
print(os.listdir())

#to create a new folder in current directory
os.mkdir('Test')

#to create a new folder and a sub folder within at the same time in current directory
os.makedirs('Test2/SubTest2')


