#variable scope - allows us to understand where our variables can be seen from within our program and also what values these variables hold. It also helps with debugging, because scope is a common problem when errors are thrown.
#LEGB - Local, Enclosing, Global, Built-in

#global - variables defined in the main program

x = 'global x'

#local - variables defined within a function

def test():
    y = 'local y'
    print(y)

test() #will print y value

def test():
    y = 'local y'
    #print(y)
    print(x)

test() #will print out global x value. This is because python tries to find of the variable is in local, if not then in enclosing, if not then in global

def test():
    y = 'local y'
    #print(y)
    print(x)

#print(y) #will throw error. if you print out a local variable outside the func, it will throw error as python cannot find it in local, enclosing, global or built-in

def test():
    x = 'local x'
    #print(y)
    print(x)

test() #local x
print(x) #global x

#update global with local
def test():
    global x #add this code
    x = 'local x'
    #print(y)
    print(x)

test() #local x
print(x) #local x

#define a variable as a argument
def test(z):
    print(z)

test('local z')

#built-in - names preassigned in python

m= min([5,4,2,6,1])
print(m)

#see all built-in functions

#import builtins
#print(dir(builtins))

#python allows you to create your own functions using built-in names and overwrites it so need to be careful there

#enclosing

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()

#above prints out inner x and outer x

def outer():
    x = 'outer x'

    def inner():
        #x = 'inner x'
        print(x)

    inner()
    print(x)

outer() #this prints out outer x as it first checks for local within the inner func, does not find then checks within enclosing func (that is the puter func) and prints out outer x

#on the other hand, below throws error as it first checks for local within inner func, finds it, prints it and then for outer x it does not find any local variable defined and since it does not have any func enclosing outer, it throws error so the entire code throws error

def outer():
    #x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()

#can change the local value of the enclosing variable using nonlocal keyword. DOnt use global keyword as that will affect variable at program level

def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()

x = 'global x'
def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)

def outer():
    x = 'outer x'

    def inner():
        #x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)

def outer():
    #x = 'outer x'

    def inner():
        #x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)















    
