import sys
import os
import re

# print(os.getcwd())
# os.chdir("E:/osvaldo/PythonExercises/02SecondCourse/Assignments/Section06/project_files")
# print(os.getcwd())

directory_containing_files = sys.argv[1]
words_to_aggregate = sys.argv[2:]

# Expected Output:
# {"there": n, "Michael": n, "running": n}

words_and_counts = {}

for word in words_to_aggregate:
    count = 0
    for path, folder_names, file_names in os.walk(directory_containing_files):
        for file_name in file_names:
            file = os.path.join(path, file_name)
            with open(file, "r") as a_file:
                for line in a_file:
                    if re.search(word, line):
                        word_list = re.findall(word, line)
                        count += len(word_list)

    words_and_counts[word] = count

print(words_and_counts)
