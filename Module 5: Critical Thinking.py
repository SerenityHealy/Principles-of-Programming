total_rainfall = 0
total_months = 0

print("Hello, please follow the prompts to calculate the total and average rainfall for each month.")
number_of_years = int(input("Enter the number of years: "))

for year in range(1, number_of_years + 1):

    for month in range(1, 13):

        monthly_rainfall = float(input(f"Enter the inches of rainfall for year {year}, month {month}: "))

        total_rainfall = total_rainfall + monthly_rainfall
        total_months = total_months + 1

average_rainfall = total_rainfall / total_months


print(f"The total rainfall is {total_rainfall} inches")
print(f"The total months is {total_months}")
print(f"The average rainfall per month is {average_rainfall:.2f} inches")
