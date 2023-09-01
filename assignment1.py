#!/usr/bin/env python3

# Exercise 1.

my_float_value = 9.82

my_float_value = str(my_float_value)

print(type(my_float_value))

my_float_value = int(round(float(my_float_value), 0))

# Exercise 2.

try:
    int("hello")
except Exception as e:
    print(f"When you cast a text string to a number you get the error: '{e}'")

# Exercise 3.

year = int(input("Enter current year: "))
age = int(input("What age will you be at the end of this year? "))
dob = year - age
print(f"You were born in the year {dob}")


# Exercise 4.

# print("2000"+18)
# raises an error as you cannot concatonate a number too a string

# Exercise 5.
prices = {
    "mars_bars": 1,
    "coke": 1.5,
    "crisps": 0.8,
    "tea": 2,
    "bread": 3.5
}

bill = {
    "mars_bars": 5,
    "coke": 4,
    "crisps": 3,
    "tea": 2,
    "bread": 1
}

total = 0
for i in bill:
    total += prices[i]*bill[i]

print(f'your total bill is : €{total:.2f}')

# Exercise 6.
number1 = int(input("Enter first number: "))
number2 = input("Enter second number: ")
number2 = int(number2)

total = number1 + number2
print(f'{number1} + {number2} = {total}')


# Exercise 7.

far_to_cel = lambda far: (far-32)*(5/9)

far = float(input("Enter a temperature in Fahrenheit"))

cel = far_to_cel(far)

print(f'{far}°F = {cel}°C')


