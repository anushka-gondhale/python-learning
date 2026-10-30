letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Harry"

print(letter.format(country, name))
# An f-string (formatted string literal) is a clean, modern way to insert variables directly inside a 
# string in Python. You create one by adding the letter f or F right before the opening quotation mark.
print(f"hey i am {name} i am from {country}")