#Named Tuples in Python are High-performance container datatypes
#more readable than regular tuples. Immutable like regular tuples

from collections import namedtuple

#define the namedtuple
Color = namedtuple('Color', ['red', 'blue', 'green'])

#pass values for that namedtuple
get_color = Color(55, 155, 255)

#call out the needed values
print(get_color.red)
print(get_color.blue)