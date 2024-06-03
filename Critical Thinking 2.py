meal_price = float(input())

tip = meal_price * 0.18

sales_tax = meal_price * 0.07

print("Meal Price is ", f'${meal_price:.2f}')

print("Tip is", f'${tip:.2f}')

print("Sales Tax is", f'${sales_tax:.2f}')

print("Total Price is", f'${meal_price + tip + sales_tax:.2f}')
