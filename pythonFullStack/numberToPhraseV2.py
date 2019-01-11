ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
tens = {2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

def intToEngV2(x):
	word = ""
	number = int(x)
	if number == 0:
		#if zero
		return "zero"
	elif 9 < number < 20:
		#if 10 or teens
		word = teens[number]
	elif 0 < number < 10:
		#if in the ones
		word = ones[number]
	elif number // 100 == 0 and number % 100 // 10 != 0 and number % 100 % 10 == 0:
		#if < 100 and ones is 0
		word = (f"{tens[number//10]}")
	elif number // 100 == 0:
		#if < 100
		word = (f"{tens[number//10]}-{ones[number%10]}")
	else:
		if number % 100 // 10 == 1:
			#if > 100 and has 10 or teens
			word = (f"{ones[number//100]}-hundred, {teens[number%100]}")
		elif number % 100 % 10 == 0 and number % 100 // 10 != 0:
			#if > 100 and the ones is 0 but the 10s isn't
			word = (f"{ones[number//100]}-hundred, {tens[number%100//10]}")
		elif number % 100 % 10 == 0:
			#if > 100 and both ones and tens are 0
			word = (f"{ones[number//100]}-hundred")
		elif number % 100 % 10 != 0 and number % 100 // 10 == 0:
			#if > 100 and tens are 0 but ones are not
			word = (f"{ones[number//100]}-hundred-{ones[number%10]}")
		else:
			word = (f"{ones[number//100]}-hundred-{tens[number%100//10]}-{ones[number%10]}")
	return word



"""
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
			"""

x = input("Enter a number between 0 and 999: ")
print(f'You have entered {intToEngV2(x)}.')


