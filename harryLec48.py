f=open("file1.txt","x")
f.close()
# This tells Python:

# Create a new file named file1.txt.

# If the file does not already exist, create it successfully.

# If the file already exists, give a FileExistsError.
# os.remove() deletes files.

# os.rmdir() deletes empty folders.
import os
os.remove("file1.txt")
print("file deleted successfully")
print(os.path.exists("file1.txt"))

os.rmdir("data\day9")
os.rmdir("data")
# open() – creates or opens files.

# close() – closes files.

# os.remove() – deletes files.

# os.rmdir() – deletes empty folders.

# os.listdir() – lists files and folders.

# os.path.exists() – checks whether a file or folder exists.

