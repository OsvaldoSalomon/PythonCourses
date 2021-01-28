for i in range(5):
    try:
        print(i / 0)
    except ZeroDivisionError as e:
        print(e, "--> Division by 0 is not allowed, sorry!")

print(" ------------ ")

for i in range(5):
    try:
        print(i / 1)
    except ZeroDivisionError as e:
        print(e, "--> Division by 0 is not allowed, sorry!")
    print("The rest of the code...")

print(" ---------- ")

try:
    print(4 / 0)
except ZeroDivisionError:
    print("Division by 0 is just wrong!")
except NameError:
    print("Name error detected!")
except ValueError:
    print("Wrong value!")
finally:
    print("I don't care, I'm getting printed either way!")
