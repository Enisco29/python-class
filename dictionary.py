#concession stand program

menu = {
        "pizza": 3.00,
        "nachos": 4.50,
        "burger": 5.00,
        "pasta": 6.00,
        "salad": 4.00,
        "chicken": 7.00,
        "soda": 1.50
        }

cart = []
total = 0

print("----- MENU -----")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----------------") 

while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----- YOUR CART -----")
for food in cart:
    total += menu[food]
    print(food, end=" ")
        
print()
print(f"Your total is: ${total:.2f}")      