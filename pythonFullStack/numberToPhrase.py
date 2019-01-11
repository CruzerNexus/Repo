ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
tens = {2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

def intToEng(x):
	word = ""
	if x == "10":
		return("ten")
	elif x == "11":
		return("eleven")
	elif x == "12":
		return("twelve")
	elif x == "0":
		return("zero")
	else:
		number = int(x)
		if 12 < number < 20:
			if x[-1] == "3":
				return "thirteen"
			elif x[-1] == "4":
				return "fourteen"
			elif x[-1] == "5":
				return "fifteen"
			elif x[-1] == "6":
				return "sixteen"
			elif x[-1] == "7":
				return "seventeen"
			elif x[-1] == "8":
				return "eighteen"
			else:
				return "nineteen"
		else:
			for i in range(len(x)):
				if len(x) == 2 and number % 10 !=0:
					word = (f"{tens[number // 10]}-{ones[number % 10]}")
				elif len(x) == 2:
					word = (tens[number // 10])
				else:
					word = (ones[number%10])
			return word

x = input("Enter a number between 0 and 99: ")
print(f'You have entered {intToEng(x)}.')


