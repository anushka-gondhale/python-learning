# seek
# Using seek(), we can move that pointer to any desired position.
# f = open("learningbranch.txt", "r")

# print(f.read(5))# read 5 means 5 tak read kar 

# f.seek(5)

# print(f.read())

# f.close()
# 2. tell() method
# Definition: The tell() method is used to return the current position of the file pointer in a file.
f = open("demo.txt", "r")

print(f.tell())

f.read(5)
f.seek(5)

print(f.tell())

f.close()
#truncate method ye writing mein use atta samj hame file mein likya ki hello i am anushka 
# lekin sirf hello honu "file mein" to hame tiko size dhatko karak waaste truncate ko istmall karsan 
#ikkamein hame jo number diya tikko size less hos 