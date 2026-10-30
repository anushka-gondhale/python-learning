#string method 
name="!!!!harry!!!!!!"
names="anushkaAkshay"
print(name.lower())
print(name.upper())
#the meaning of () this is we are saying to python run the code 
#1.replace 
print(name.replace("harry","anushka"))
#split
str="harry,anushka,kiku"
print(str.split(","))
#capitalize
#capitalize method work as it convert first letter of string capatilize and other small if in that string
#present a captal letter
print(names.capitalize())
# center 
# center method align the string into the center according to the user parameter 
print(name.center(17))
# it also consider the word of string 
#count 
#count method is use to count the thing to identify for howmany time that thing string comes 
stud="laxmikant"
print(stud.count("t"))
# endswith
# endswith checks the value if it is true then it shows true otherwise false 
print(name.endswith("!!!"))
#find 
#find method finds the first occurance of given data and exicutes its index number if that data is not 
# present in that so it exicute minus 1
print(stud.find("t"))
print(stud.find("o"))
#isalnum
#isalnum means it exicute true if and only if there is present A-Z,a-z,0-9 element other except this 
# is present then it shows false 
print(stud.isalnum())
#isalpha 
#isalpha returns only true when A-Z,a-z present other wise shows false 
print(stud.isalpha())
#islower
#islower shows true if alll character in string is lower other wise false 
print(stud.islower())
#isspace
# isspace shows only true when the string only contain space other wise false  
str="     " 
print(str.isspace())
# istittle 
# istittle shows the true if first letter of every word consist capital letter otherwise false 
print(stud.istitle())
#swapcase
#swapcase convert the string its opposite if string letters are capital then it convert into small letter 
#small letter into capital 
print(stud.swapcase())
# startswith
# startswith shows true if that thing start with user in input
print(stud.startswith("L"))
#tittle 
#tittle convert every word first letter into capital letter 

