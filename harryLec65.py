
# Parent class
class Father:

    def father_skill(self):
        print("Father knows cooking")


# Child class inherits Father
class Son(Father):

    def son_skill(self):
        print("Son knows coding")


# Creating child class object
obj = Son()

# Calling parent class method
obj.father_skill()

# Calling child class method
obj.son_skill()
