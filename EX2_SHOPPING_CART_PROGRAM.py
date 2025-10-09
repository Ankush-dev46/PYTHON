print("*****SHOPPING CART******")

items = input("ENTER A ITEM YOU WANT BUY:")
quantity = int(input("ENTER THE NUMBER OF QUNTITY YOU WANT TO BUY:"))
prize = float(input("THE PRICE IS $:"))

total = quantity * prize

print(f"THE PRIZE OF {items} IS ${prize},And the quantity is {quantity}")
print(f"HERE GOES THE TOTAL ${total}")