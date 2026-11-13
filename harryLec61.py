class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)
print(p.__dict__)

print(help(Person))
# __dir__ agar hame karya to tine hamke jikka mein jo method se te dekdawas matlab agar 
# class mein dir __ lagdya to tine te class par hame jikka method use kari saksan te dekdawas  
#dic method dictionary mein convert karas 
#help method tine poori information des puro kay ka bhi baram kadak ray to 
