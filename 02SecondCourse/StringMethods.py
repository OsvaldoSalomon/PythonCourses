sentence = "this is a sentence"
print(sentence.upper())

sentence = "THIS is a Sentence"
print(sentence.lower())
print(sentence.capitalize())
print(sentence.isdigit())
print(sentence.startswith("this"))

# Formatting strings
sentence = "The sum of 5 + 10 is {0}".format(50)
print(sentence)

sentence = "The sum of {0} + {1} = {2}".format(10,15,25)
print(sentence)

sentence = "The sum of {0} + {2} = {1}".format(5,15,10)
print(sentence)

# Strings are immutable
my_var = "abcdefg"
my_var = "1" + my_var[1:]
print(my_var)