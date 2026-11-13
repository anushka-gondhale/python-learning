# _init__()
# When initializing an object
# __str__()
# When converting object to string, e.g. print()
# __len__()
# When using len()
class Demo:

    def __init__(self):
        print("Init called")

    def __str__(self):
        print("Str called")
        return "Hello"

    def __len__(self):
        print("Len called")
        return 5

    def __call__(self):
        print("Call called")


obj = Demo()