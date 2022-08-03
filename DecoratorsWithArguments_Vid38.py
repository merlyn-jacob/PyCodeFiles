#create decorators with parameters that accept arguments
#Accepting arguments allows us to add even more functionality to our decorators

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper(*args, **kwargs):
            print(prefix, "Executed before,", original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, "Executed after,", original_function.__name__, '\n')
            return result
        return wrapper
    return decorator_function


@prefix_decorator('Log:')
def display(name, age):
    print("Name is {} and I am {} years old".format(name,age))

display('Jane', 22)