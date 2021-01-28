my_file = open("E:/osvaldo/PythonExercises/03ThirdCourse/routers.txt", "r")

print(my_file.read())
print(" ------------ ")
my_file.seek(0)
print(my_file.read(5))
print(" ------------ ")
my_file.seek(0)
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

print(" ------------ ")
my_file.seek(0)

for line in my_file.readlines():
    if line.startswith("A"):
        print(line)

