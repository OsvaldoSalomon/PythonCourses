# my_file = open('E:/osvaldo/PythonExercises/02SecondCourse/sample')
#
# content = my_file.read()
# print(content)
#
# my_file.seek(0)
# print("---------------")
#
# data = my_file.read()
# # print(data)
#
# my_file.seek(0)
# content_list = my_file.readlines()
# print(content_list)
#
# print("---------------")

# To append a file use:

with open('/02SecondCourse\\sample', mode='a') as my_file:
    my_file.write("\nTHIS IS MY SENTENCE")

my_appended_file = open('/02SecondCourse/sample')
print(my_appended_file.read())

# To overwrite or write another file use:

with open('/02SecondCourse\\sample2', mode='w') as my_file:
    my_file.write("\nTHIS IS MY SENTENCE")

my_appended_file = open('/02SecondCourse/sample')
print(my_appended_file.read())

# To overwrite or write and then read another file use:

with open('/02SecondCourse\\sample2', mode='w+') as my_file:
    my_file.write("\nTHIS IS MY SENTENCE")

my_appended_file = open('/02SecondCourse/sample')
print(my_appended_file.read())

# To read a file use:

with open('/02SecondCourse\\sample2', mode='r') as my_file:
    my_file.write("\nTHIS IS MY SENTENCE")

my_appended_file = open('/02SecondCourse/sample')
print(my_appended_file.read())

# To read and write to a file use:

with open('/02SecondCourse\\sample2', mode='r+') as my_file:
    my_file.write("\nHello there")

my_appended_file = open('/02SecondCourse/sample')
print(my_appended_file.read())
