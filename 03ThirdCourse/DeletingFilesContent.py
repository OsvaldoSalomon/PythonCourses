f = open("E:/osvaldo/PythonExercises/03ThirdCourse/test.txt", "r+")
print(f)
print(" ----------- ")
print(f.read())
print(" ----------- ")
f.seek(0)
print(len(f.read()))
print(" ----------- ")
f.seek(0)
f.truncate(10)
print(f.read())
f.close()