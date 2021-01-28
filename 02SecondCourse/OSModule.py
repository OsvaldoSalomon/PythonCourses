import os

# Get current working directory
print(os.getcwd())

# Get current working directory
print(os.getcwd())

os.chdir("E:\osvaldo\PythonExercises\SecondCourse")

# Lists contents of directory
print(os.listdir())

if "myFolder" not in os.listdir():
    os.mkdir("myFolder")

if "myFolder" not in os.listdir():
    os.makedirs("myFolder/subFolder/dataFolder")

# os.chdir("E:\osvaldo\PythonExercises")

# Delete specific directory
# os.rmdir("myFolder/subFolder/dataFolder")

# Delete specific file
# os.rmdir("myFolder/subFolder/dataFolder/myfile.txt")

# Delete specific directories. This is dangerous, it removes entire directory structure.
# os.removedirs("myFolder/subFolder")

# Rename a file
os.rename("sample.txt", "renamed.txt")


