print("Hello World!")
print("Next line")

first_name = "Osvaldo "
last_name = "Salomon"

name = first_name + last_name
print(name)

adult = False
num = 24
decimal = 24.2
word = "Word"

collection = [adult, num, decimal, word]

for i in collection:
    data_type = type(i)
    print(data_type)

answer = (10.999 + 3) * (9 - 4.75)
print(answer)

sentence = "I'm coming \nhome"
print(sentence)

sentence2 = "This is a sentence"
print(sentence2[-3])
print(sentence2[0:4])

sentence3 = "abcdefg"
print(sentence3[0:7])
print(sentence3[0:7:2])
print(sentence3[3:])