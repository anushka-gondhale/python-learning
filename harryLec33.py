# Deep Explanation: This method updates the current dictionary 
# with elements from another dictionary object or from an iterable of key-value pairs.
ep1 = {122: 45, 123: 89, 567: 69}
ep2 = {222: 67, 567: 90}

ep1.update(ep2)
# 222: 67 is added because it didn't exist.
# 567: 69 becomes 567: 90 because it already existed.
print(ep1) # Output: {122: 45, 123: 89, 567: 90, 222: 67}
# • clear()
	# • Deep Explanation: Removes all the items from the dictionary completely. It does not delete the dictionary variable from memory; it simply wipes it clean, leaving you with an empty dictionary {}.
ep1 = {122: 45, 123: 89}
ep1.clear()
print(ep1) # Output: {}
# • pop()
	# • Deep Explanation: Removes the key-value pair matching the specific key you pass inside the parentheses and returns the value of that deleted key.
	# • Edge Case: If the key you try to pop does not exist, Python will throw a KeyError.
info = {'name': 'Karan', 'age': 19, 'eligible': True}
popped_value = info.pop('age') 
print(popped_value) # Output: 19
print(info)         # Output: {'name': 'Karan', 'eligible': True}
# • popitem()
	# • Deep Explanation: Removes and returns the last key-value pair that was inserted into the dictionary as a tuple format (key, value).
	# • Note: In older Python versions (before 3.7), dictionaries were completely unordered, 
# so popitem() would remove a random item. Now, it always removes the very last one.
info = {'name': 'Karan', 'age': 19, 'eligible': True}
last_item = info.popitem()
print(last_item) # Output: ('eligible', True)
print(info)      # Output: {'name': 'Karan', 'age': 19} 
# • Deep Explanation: del is a structural keyword in Python, not a dictionary method. 
# You can use it to target two distinct behaviors:
# 1. Delete a specific key-value pair: del info['age']
# 2. Delete the entire dictionary variable from system memory: del info. 
# If you try to print the dictionary after doing this, Python crashes with a NameError because the variable no longer exists.
info = {'name': 'Karan', 'age': 19}
del info['age'] # Deletes just the age key

del info 
# print(info) # Throws NameError: name 'info' is not defined
# • get()
# • Deep Explanation: Used to access the value of a key safely.
info = {'name': 'Karan', 'age': 19}
print(info.get('salary'))         # Output: None (Safe!)
# print(info['salary'])           # Crashes the program with KeyError!
print(info.get('salary', 25000)) # Output: 25000 (Returns custom fallback if missing)
