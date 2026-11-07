class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    # @staticmethod
    def add(a, b):
        return a + b

# result = Math.add(1, 2)
# print(result) # Output: 3
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(a.add(7,2))
# Uncomment the @staticmethod decorator on line 8. This tells Python not to pass the object instance (self)
# automatically, allowing it to take exactly 2 arguments as intended.
# static method agar hame lagdya na to tine python ke bolus ki self argument consider nako karu 

