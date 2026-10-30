# 1. Default Arguments
# Explanation: A parameter with a predefined value that is used when no argument is provided.
def greet(name="Guest"):
    print("Hello", name)

greet()        # Hello Guest
greet("Amit")  # Hello Amit
# 2. Keyword Arguments
# hame randomly bhi likke to chalas bas tikko nav galnu 
# Explanation: Arguments passed using parameter names, so the order does not matter.
def student(name, age):
    print(name, age)

student(age=20, name="Amit")
# Amit 20
# 3.Required Arguments
# Explanation: Arguments that must be provided when calling a function because they have no default value.
def add(a, b):
    print(a + b)

add(10, 20)  # 30
# add(10)    # Error: missing argument
# 4. Variable-Length Arguments
# Explanation: Arguments that allow a function to accept any number of values using *args or **kwargs.

# Using *args: Accepts multiple positional arguments.
def add(*numbers):
    print(sum(numbers))

add(10, 20, 30)  # 60
# Using **kwargs: Accepts multiple keyword arguments as a dictionary
def info(**details):
    print(details)

info(name="Amit", age=20)
# {'name': 'Amit', 'age': 20}
# what is positional arguments 
# Positional arguments are values passed to a function according to their position (order).
def student(name, age):
    print(name)
    print(age)

student("Amit", 20)