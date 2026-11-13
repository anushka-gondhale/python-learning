# Method Overriding in Python
# Method overriding means defining a method in the child class that already exists in the parent class, but with a different implementation.

# In simple words, the child class changes the behaviour of the parent's method.

# Python code with comments

# Parent class
class Father:

    # Method of parent class
    def skills(self):
        print("Father knows cooking")


# Child class inheriting Father
class Son(Father):

    # Overriding the parent's skills() method
    def skills(self):
        print("Son knows coding")


# Creating an object of the child class
obj = Son()

# Calling the method
# Python executes the child's method instead of the parent's method
obj.skills()

# Parent class
class Father:

    # Method of parent class
    def skills(self):
        print("Father knows cooking")


# Child class inheriting Father
class Son(Father):

    # Overriding the parent's skills() method
    def skills(self):
        print("Son knows coding")


# Creating an object of the child class
obj = Son()

# Calling the method
# Python executes the child's method instead of the parent's method
obj.skills()

# Parent class
class Father:

    # Method of parent class
    def skills(self):
        print("Father knows cooking")


# Child class inheriting Father
class Son(Father):

    # Overriding the parent's skills() method
    def skills(self):
        print("Son knows coding")


# Creating an object of the child class
obj = Son()

# Calling the method
# Python executes the child's method instead of the parent's method
obj.skills()
# Method overriding means the child class creates a method with the 
# same name as the parent class method, but gives it a different job.