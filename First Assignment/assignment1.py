# -----------------------IF-ELSE EXERCISE----------------------- #

'''1. Write a program to find the maximum between two numbers.'''

# n1 = int(input("Enter 1st number: "))
# n2 = int(input("Enter 2nd number: "))

# if n1 > n2:
#     print(f"{n1} is greater than {n2}")
# else:
#     print(f"{n2} is greater than {n1}")


''' 2. Write a program to find the maximum between three numbers.'''

# n1 = int(input("Enter 1st number: "))
# n2 = int(input("Enter 2nd number: "))
# n3 = int(input("Enter 3rd number: "))

# if n1 > n2 and n1 > n3:
#     print(f"{n1} is greater than {n2} and {n3}")

# elif n2 > n1 and n2 > n3:
#     print(f"{n2} is greater than {n1} and {n3}")

# else:
#     print(f"{n3} is greater than {n1} and {n2}")

''' 3. Write a program to check whether a number is negative, positive or zero.'''
# n = int(input("Enter number: "))
# if n < 0:
#     print(f"number {n} is negative")
# elif n == 0:
#     print(f"number is zero")
# else:
#     print(f"number {n} is positive")


''' 4. Write a program to check whether a number is divisible by 5 and 11 or not.'''

# n = int(input("Enter number: "))
# if n % 5 == 0 and n % 11 == 0:
#     print(f"{n} is divisible by 5 and 11")
# elif n % 5 == 0 and n % 11 != 0:
#     print(f"{n} is not divisible by 5 but not divisible by 11")
# elif n % 5 != 0 and n % 11 == 0:
#     print(f"{n} is not divisible by 11 but not divisible by 5")
# else:
#     print(f"{n} is neither divisible by 5 nor 11")


''' 5. Write a program to check whether a number is even or odd.'''
# n = int(input("Enter number: "))
# if n > 0:
#     if n % 2 == 0:
#         print(f"{n} is positive even")
#     else:
#         print(f"{n} is positive odd")

# else:
#     if n % 2 == 0:
#         print(f"{n} is negative even")
#     else:
#         print(f"{n} is negative odd")

''' 6. Write a program to check whether a year is leaping year or not.'''
# year = int(input("Enter the year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not a leap year")


''' 7. Write a program to input any alphabet and check whether it is vowel or consonant.'''
# # Input an alphabet from the user
# alphabet = input("Enter an alphabet: ")

# # Check if the input is a single alphabet
# if len(alphabet) == 1:
#     alphabet = alphabet.lower()
#     if alphabet in ['a', 'e', 'i', 'o', 'u']:
#         print(f"The alphabet '{alphabet}' is a vowel.")
#     else:
#         print(f"The alphabet '{alphabet}' is a consonant.")
# else:
#     print("Please enter a single alphabet.")

''' 8. Write a program to check whether a character is uppercase or lowercase alphabet.'''
# char = input("Enter a character: ")

# if len(char) == 1:
#     if char >= 'A' and  char <= 'Z':
#         print(f"The character '{char}' is an uppercase alphabet.")
#     elif char >= 'a' and char <= 'z':
#         print(f"The character '{char}' is a lowercase alphabet.")
#     else:
#         print(f"The character '{char}' is not an alphabet.")
# else:
#     print("Please enter a single character.")

''' 9. Write a program to input the week number and print weekday.'''
# week_num = int(input("Enter the week number: "))
# if 1 <= week_num <= 7:
#     if week_num == 1:
#         print("Monday")
#     elif week_num == 2:
#         print("Tuesday")
#     elif week_num == 3:
#         print("Wednesday")
#     elif week_num == 4:
#         print("Thursday")
#     elif week_num == 5:
#         print("Friday")
#     elif week_num == 6:
#         print("Saturday")
#     elif week_num == 7:
#         print("Sunday")
# else:
#     print("Invalid week number. Please enter a number between 1 and 7.")


''' 10. Write a program to input the month number and print the number of days in that month.'''
# month_num = int(input("Enter the month number (1-12): "))

# if month_num == 2:
#     print("28 or 29 days (leap year)")
# elif month_num in [4, 6, 9, 11]:
#     print("30 days")
# else:
#     print("31 days")


''' 11. Write a program to count a minimum number of notes in a given amount.'''

# amount = int(input("Enter the amount: "))
# notes = 0

# if amount >= 2000:
#     notes += amount // 2000
#     amount %= 2000
# if amount >= 500:
#     notes += amount // 500
#     amount %= 500
# if amount >= 100:
#     notes += amount // 100
#     amount %= 100
# if amount >= 50:
#     notes += amount // 50
#     amount %= 50
# if amount >= 10:
#     notes += amount // 10
#     amount %= 10

# print("Minimum number of notes:", notes)


''' 12. Write a program to input marks of five subjects Physics, Chemistry,
Biology, Mathematics, and Computer. Calculate percentage and grade
according to the following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
'''

# physics = int(input("Enter Physics marks: "))
# chemistry = int(input("Enter Chemistry marks: "))
# biology = int(input("Enter Biology marks: "))
# mathematics = int(input("Enter Mathematics marks: "))
# computer = int(input("Enter Computer marks: "))

# total_marks = 500
# obtained_marks = physics + chemistry + biology + mathematics + computer
# percentage = (obtained_marks / total_marks) * 100

# if percentage >= 90:
#     grade = 'A'
# elif percentage >= 80:
#     grade = 'B'
# elif percentage >= 70:
#     grade = 'C'
# elif percentage >= 60:
#     grade = 'D'
# elif percentage >= 40:
#     grade = 'E'
# else:
#     grade = 'F'

# print("Percentage:", percentage)
# print("Grade:", grade)


'''13. Write a program to input the basic salary of an employee and calculate
its Gross salary according to the following:
Basic Salary <= 10000 : HRA = 20%, DA = 80%
Basic Salary <= 20000 : HRA = 25%, DA = 90%
Basic Salary > 20000 : HRA = 30%, DA = 95%'''

# basic_salary = float(input("Enter the basic salary: "))

# if basic_salary <= 10000:
#     hra = 0.20 * basic_salary
#     da = 0.80 * basic_salary
# elif basic_salary <= 20000:
#     hra = 0.25 * basic_salary
#     da = 0.90 * basic_salary
# else:
#     hra = 0.30 * basic_salary
#     da = 0.95 * basic_salary

# gross_salary = basic_salary + hra + da
# print("Gross salary:", gross_salary)


'''14. Write a program to input electricity unit charges and calculate total
electricity bill according to the given condition:
For the first 50 units Rs. 0.50/unit
For the next 100 units Rs. 0.75/unit
For the next 100 units Rs. 1.20/unit
For units above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill'''

# units = int(input("Enter the electricity units: "))
# surcharge = 0

# if units <= 50:
#     bill = units * 0.50
# elif units <= 150:
#     bill = 50 * 0.50 + (units - 50) * 0.75
# elif units <= 250:
#     bill = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20
# else:
#     bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50

# surcharge = 0.20 * bill
# total_bill = bill + surcharge
# print("Total electricity bill:", total_bill)
