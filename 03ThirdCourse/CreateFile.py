new_file = open("E:/osvaldo/PythonExercises/03ThirdCourse/newfile.txt", "w")

new_file.write("This is a great day for science!")

new_file.close()

new_file = open("E:/osvaldo/PythonExercises/03ThirdCourse/newfile.txt", "w")
new_file.writelines(["Cisco", "Juniper", "HP"])
new_file.close()

new_file = open("E:/osvaldo/PythonExercises/03ThirdCourse/newfile.txt", "a")
new_file.writelines("This string was appended")
print(new_file.read())
new_file.close()


print(new_file.closed)

with open("E:/osvaldo/PythonExercises/03ThirdCourse/newfile.txt", "w") as f:
    f.write("Hello file!")


