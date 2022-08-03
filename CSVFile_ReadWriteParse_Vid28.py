#read a csv file

import csv
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #print(csv_reader) this will not print out the contents
    for line in csv_reader:
        print(line) #this prints out a list of each row

#since output is a list, you can print out specific indexes - 0 is first, 1 is last name, 2 is email

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line[2]) #prints all email addresses

#to exclude the column header, use next()

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    for line in csv_reader:
        print(line[2])

#to write into another file

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t') #\t is tab

        for line in csv_reader:
            csv_writer.writerow(line)

#to read the newly written file, note = mention delimiter as tab else it will not seperate as tab


with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for line in csv_reader:
        print(line)

#use DictReader instead of regular reader. DictReader gives a dict key:value format
#easy to parse, just have to mention the key

with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')
    for line in csv_reader:
        print(line)
        
with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')
    for line in csv_reader:
        print(line['email'])

#using DictWriter - note : need to create a seperate variable that holds the column names

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first name', 'last name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter = '\t')

        csv_writer.writeheader() #to ensure headers are added

        for line in csv_reader:
            csv_writer.writerow(line)

#to remove any field name when writing to a file, remove it from fieldnames and add a code in for loop
            
#fieldnames = ['first name', 'last name']

#for line in csv_reader:
    #del line['email']
    #print(line)

            
            





























