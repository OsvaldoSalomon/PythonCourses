# file=open("myfile.txt","w")
# file.write("Hello\n")
# file.write("Welcome to file handling in Python!")
# file.write(str(1000))
# file.close()

# file=open("E:/osvaldo/PythonExercises/venv/myfile.txt","r")
# filedata=file.readline()
# print(filedata)
# filedata=file.readline()
# print(filedata)
# file.close()

# file=open("E:/osvaldo/PythonExercises/venv/myfile.txt","r")
# s=file.read()
# nums=s.split()
# sum = 0
# for elem in nums:
#     sum=sum+int(elem)
# print(sum)
# file.close()

# file=open("E:/osvaldo/PythonExercises/venv/myfile.txt","w")
# print(file.tell())
# file.seek(1,0)
# file.write(" World")
# file.close()

import os
import os.path

# os.mkdir("MyFolder")
# os.rmdir("MyFolder")
# os.rename("myfile.txt","MyFile.txt")
# os.remove("MyFile.txt")

print(os.getcwd())


