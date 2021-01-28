import os

os.walk("E:/osvaldo/PythonExercises")

for dirpath, dirnames, filenames in os.walk("E:/osvaldo/PythonExercises"):
    # print(dirpath)
    # print(dirnames)
    # print(filenames)
    # print(" -------------- ")
    pass

# Get the basename.. that's the file at the directory location given
print(os.path.basename("/02SecondCourse/myFolder/myfile.txt"))

# Get the directory name only, not the file
print(os.path.dirname("/02SecondCourse/myFolder/myfile.txt"))

# Will give directory name and basename in a tuple
print(os.path.split("/02SecondCourse/myFolder/myfile.txt"))

# Used to check if directory exists in the specified path
os.path.isdir("/02SecondCourse/myFolder/myfile.txt")

# Used to check if file exists in the specified path
os.path.isfile("/02SecondCourse/myFolder/myfile.txt")

# Check if the path exists on the computer
print(os.path.exists("/02SecondCourse/myFolder/myfile.txt"))

print(os.path.splitext("/02SecondCourse/myFolder/myfile.txt"))
