#Case scenario - how to parse a CSV file and output the data to an HTML unordered list.
#List of all patreon contributors (old and new ones) to be listed on patreon
#The list was becoming too large to maintain manually, so writing a Python script to automate this process


import csv

html_output = ''
names = []

with open('patreons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    #to skip first line of unwanted data
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f'{line['FirstName']} {line['LastName']}')

html_output += f'<p>There are currently {len(names)} public contributors. Thank you!<\p>' #+= stands for append. <p> and <\p> are html codes for adding a paragraph statement in the output file

html_output += '\n<ul>' #<ul> is the html code for adding an unordered list

for name in names:
    html_output += f'\n\t<li>{names}<\li>' #\t is tab, <li> is code for list

html_output += '\n<ul>' #closing the unordered list

print(html_output)
        
