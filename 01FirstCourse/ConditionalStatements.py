# ------------- if statement
# value = input("Enter the value: ")
# if(value >= "0" and value <= "9"):
#     print("Digit =", value)
# if(value == " "):
#     print("Space")
# print("Goodbye")

# -------------- if / else statement
# num = int(input("Enter the number: "))
# if(num % 2 == 0):
#     print("Even")
# else:
#     print("Odd")

# -------------- if / elif statement
# num = int(input("Enter a number: "))
# if(num == 1):
#     print("Sunday")
# elif(num == 2):
#     print("Monday")
# elif(num == 3):
#     print("Tuesday")
# elif(num == 4):
#     print("Wednesday")
# elif(num == 5):
#     print("Thursday")
# elif(num == 6):
#     print("Friday")
# elif(num == 7):
#     print("Saturday")
# else:
#     print("Invalid number")

# -----------------------
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
choice = int(input("Enter your choice: "))
if(choice == 1):
    sum = num1+num2
    print("Sum =", sum)
elif(choice == 2):
    subt = num1-num2
    print("Subtraction =", subt)
elif(choice == 3):
    mult = num1*num2
    print("Multiplication =", mult)
elif(choice == 4):
    if(num2 == 0):
        print("Division not valid")
    else:
        div = num1//num2
        print("Division =", div)
else:
    print("Not a valid number.")













