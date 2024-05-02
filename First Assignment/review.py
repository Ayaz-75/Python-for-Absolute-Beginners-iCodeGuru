# '''1. Write a program to find the maximum between two numbers.'''
# n1 = float(input("Enter number 1: "))
# n2 = float(input("Enter number 2: "))

# if n1 > n2:
#     print(f"{n1} is greater than {n2}")
# else:
#     print(n2, " is greater than ", n1)


''' 2. Write a program to find the maximum between three numbers.'''

# n1 = float(input("enter n1: "))
# n2 = float(input("enter n2: "))
# n3 = float(input("enter n3: "))

# if n1 > n2 and n1 > n3:
#     print(n1, " is maximun")

# elif n2 > n1 and n2 > n3:
#     print(n2, " is maximum")

# else:
#     print(n3, " is maximum")


'''3. Write a program to check whether a number is negative, positive or
zero.'''

# number = float(input("enter number: "))
# if number < 0:
#     print(number, " is negative")

# elif number > 0:
#     print(number, " is positive")

# else:
#     print("number is zero")


'''4. Write a program to check whether a number is divisible by 5 and 11 or
not.'''

# number = float(input("enter number: "))

# if number % 5 == 0 and number % 11 == 0:
#     print(number, " is divisible by both 5 and 11")

# else:
#     print(number, " is not divisible by both 5 and 11")


# 6. Write a program to check whether a year is leaping year or not.

year = int(input("Enter year: "))

if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, " is leap year")
else:
    print(year, " is not leap year")


