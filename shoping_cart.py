food = []
price = []
total = 0

while True:
    foods = input("\nENTER THE FOOD ITEMS THAT YOU WANT ADD IN CART:")
    print("'Q' | 'q' for Exit")
    if foods == "Q" or foods == "q":
        break
    else:
        food.append(foods)
        prices = float(input("Enter the price of each item $:"))
        price.append(prices)

print()
print("***************SHOPING_CART*******************")
print()
print("THE FOODS YOUR ARE BUYING")
for x in food:
    print(x,end=",")

print("THE PRICE")
for y in price:
    print(y,end=",")

for price in price:
    total += price

print(f"\nTHE TOTAL AMOUNT IS ${total:.02f}")
print()
print("THANKS FOR COMING,SEE YOU SOON")
