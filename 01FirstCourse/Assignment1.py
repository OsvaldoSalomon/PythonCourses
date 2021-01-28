#First Exercise
print('First Exercise')
tempCelsius = int(input("Enter the temperature in Celsius: "))
tempFahrenheit = ((tempCelsius * 9/5) + 32)
print("The temperature in Fahrenheit is", tempFahrenheit)

#Second Exercise
print('\nSecond Exercise')
x = 5
print(x)
x *= 2
print(x)
x -= 1
print(x)

#Third Exercise
print('\nThird Exercise')
import math
radiusCircle = int(input("Enter the radius of the circle: "))
result = (radiusCircle**2)* math.pi
print('The area of the circle is', result)

#Fourth Exercise
print('\nFourth Exercise')
mark1 = int(input("Enter the first mark: "))
mark2 = int(input("Enter the second mark: "))
mark3 = int(input("Enter the third mark: "))
mark4 = int(input("Enter the fourth mark: "))
mark5 = int(input("Enter the fifth mark: "))

average = (mark1+mark2+mark3+mark4+mark5)/5

print('The average is:', average)


