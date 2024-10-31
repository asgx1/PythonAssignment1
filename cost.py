
cost = 50
amount_due = cost
accepted_coins = [25, 10, 5]
while amount_due > 0:
    print(f"Amount due: {amount_due} cents")
    coin = int(input("Insert coin (25, 10, or 5): "))
    if coin in accepted_coins:
        amount_due -= coin
    else:
        print("Invalid coin.")

change = abs(amount_due)
print(f"Change owed: {change} cents")
