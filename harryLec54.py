
def my_decorator(func):
    def wrapper():
        print("Starting function")
        func()
    return wrapper


@my_decorator
def greet():
    print("Hello Python!")


greet()
def greet():
    print("Hello!")

greet = my_decorator(greet)

print(greet())