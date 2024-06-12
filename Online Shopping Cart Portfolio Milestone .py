class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${cost:.2f}")


print("Hello! This is the Online Shopping Cart!")
print("You will enter the details for 2 items and the total cost of the items will be calculated.")

items = {}

print("\nItem 1")
item1 = ItemToPurchase()
item1.item_name = input("Enter the item name: ")
item1.item_price = float(input("Enter the item price: "))
item1.item_quantity = int(input("Enter the item quantity: "))

items[item1.item_name] = item1

print("\nItem 2")
item2 = ItemToPurchase()
item2.item_name = input("Enter the item name: ")
item2.item_price = float(input("Enter the item price: "))
item2.item_quantity = int(input("Enter the item quantity: "))

items[item2.item_name] = item2

print("\nTOTAL COST")
for item in items.values():
    item.print_item_cost()
total_cost = sum(item.item_price * item.item_quantity for item in items.values())
print(f"Total Cost: ${total_cost:.2f}")
