countries = ("Spain", "Italy", "India", "England", "Germany","america","america")
temp = list(countries)
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)
# count
# the count method use to count the number of time occur 
print(countries.count("america"))