#open a file in the same directory.
#if not in the same dir, then the dir path needs to be given in the open()

#two ways

#1
f = open('test.txt', 'r') #r for read, w for write, r+ for read and write, a for append
print(f.name)
print(f.mode)
f.close()
#in this way, always end the code with .close(). (find out reason)


#2 - context manager - allows to work within the block of code,
#and when you move out of that block, it will automatically close the file

with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
#this reads all the content at once. this leads to running out of memory
#so we can either use readlines() or readline()


with open('test.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents) #prints a list of all lines
    

with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='') #will read one line at a time. end keyword with '' to remove extra lines



#if file is huge, cant use above
#intead use for loop within contxt manager

with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='') #this does not read all contents at once so no memory issue

#printing by specific character limits
with open('test.txt', 'r') as f:
    f_contents = f.read(100)#100 characters
    print(f_contents, end='')

    f_contents = f.read(100) #prints next 100 characters
    print(f_contents, end='')

###Iterating through small chunks without hardcoding:

with open('test.txt', 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents)
        f_contents = f.read(size_to_read)
    

#to know the position of the character

with open('test.txt', 'r') as f:
    f_contents = f.read(10)
    print(f.tell())

#to change the position of the character from where to read - .seek()
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0) #this starts back at the beginning instead of continuing to read

    f_contents = f.read(size_to_read)
    print(f_contents, end='')


#write files

#this creates a file if it not already present
with open('test2.txt', 'w') as f:
    pass 

#this overwrites the contents of the file
with open('test2.txt', 'w') as f:
    f.write('Test')

    f.write('Test') #this adds Test word next to Test

with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('Test') #this overwrites first test

with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R') #this overwrites just the first letter of Test to Rest

#copy contents into anotehr file

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

#copy image - add b after r and w - b stands for binary mode

#with open('test.jpg', 'rb') as rf:
    #with open('test_copy.jpg', 'wb') as wf:
        #for line in rf:
            #wf.write(line)




    
























        
    






















        
    


    
