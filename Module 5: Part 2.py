print("Hello, Welcome to the CSU Global Bookstore point calculator! Let's see how many points you have earned this month!")

number_of_books = int(input("How many books have you purchased this month:"))

if number_of_books <= 1: points = 0
elif number_of_books <= 3: points = 5
elif number_of_books <= 5: points = 15
elif number_of_books <= 7: points = 30
elif number_of_books >=8: points = 60

print(f"You have earned {points} points this month.")
