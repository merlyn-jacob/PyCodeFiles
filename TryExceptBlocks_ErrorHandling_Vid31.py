import os
print(os.getcwd())

os.chdir(r"C:\Users\myjc\Desktop\Notes_DA\PyFiles")
print(os.getcwd())

f = open('test_file.txt')

#try except blocks are to customise the error messages we receive
#we wont want users to encounter huge error handling msgs when using the software
#so we can find out the possible lines of codes for which users encounter error and write them in try except block to get a simple error message

try:
    f = open('test_file.txt')
    var = bad_var
except FileNotFoundError:
    print('Sorry, the file does not exist')
except Exception:
    print('Sorry something went wrong')

#if no custom error messages, we can also get the main error message displayed in a simple manner

try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()         #this runs if there is no exception
finally:
    print('Exceuted successfully')         #this runs regardless of exception or not

#manually raise exception
try:
    f = open('test_file.txt')
    if f.name == 'test_file.txt':
        raise Exception
except FileNotFoundError:
    print('Sorry, the file does not exist')
except Exception:
    print('Sorry something went wrong')
else:
    print(f.read())
    f.close()
finally:
    print('Exceuted successfully')


