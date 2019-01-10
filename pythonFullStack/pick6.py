import random

def pick6():
	randCount = 0
	lotto = []
	while randCount < 6:
		lotto.append(random.randint(1,99))
		randCount += 1
	return lotto

def num_matches(lotto, ticket):
	winnings = 0
	for i in range(len(lotto)):
		if lotto[i] == ticket[i]:
			winnings += 1
	return winnings

balance = 0
winBalance = 0
tryCount = 0
lotto = pick6()
while tryCount < 100000:
	balance -= 2
	ticket = pick6()
	winnings = num_matches(lotto, ticket)
	if winnings == 1:
		winBalance += 4
	elif winnings == 2:
		winBalance += 7
	elif winnings == 3:
		winBalance += 100
	elif winnings == 4:
		winBalance += 50000
	elif winnings == 5:
		winBalance += 1000000
	elif winnings == 6:
		winBalance += 25000000
	tryCount += 1

balance += winBalance
ROI = (winBalance - 200000)/200000
print(f"After buying 100,000 lotto tickets (costing $200,000 total) your final account balance is ${balance}.")
print(f"You won a total of ${winBalance}")
print(f"Your ROI is {ROI}. Congratulations!")




