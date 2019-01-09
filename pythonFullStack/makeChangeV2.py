# makeChange.py
quarters = 0
dimes = 0
nickels = 0
pennies = 0
while True:
    cash = input("Please enter amount in dollars (x.xx): $")
    print(cash)
    cash = float(cash)
    cash = (cash * 100)
    cash = round(cash)
    cash = int(cash)
    if type(cash) is int:
        break
dollars = cash // 100
cash = cash % 100
if cash != 0:
    quarters = cash // 25
    cash = cash % 25
    if cash != 0:
        dimes = cash // 10
        cash = cash % 10
        if cash != 0:
            nickels = cash // 5
            pennies = cash % 5

print(f"There are {dollars} dollars, {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.")
