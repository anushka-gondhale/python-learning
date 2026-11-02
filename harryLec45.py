# file handling 
# f=open("learningbranch.txt")
# print(type(f))
# print(f.read())
# print(f.read(5))
# print(f.readline())
# f.close()
#readline()function use to read a one line of a file
f=open("learningbranch.txt","r")
print(f.readline())
# print(f.read(5)) 
#to read a file line by line using a for loop
for i in f:
    print(i)
#hamke ek line free mein aawas kaike boleto tha par file mein jawa liksan tiko har line par by default 
# \n ye ras to tika baad print ko curson hetlyang jas to yau kari tha par ik line 
