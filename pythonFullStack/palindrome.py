alphabet = 'abcdefghijklmnopqrstuvwxyz'

def check_palindrome(word):
	palCheck = word.lower().strip(" .,!?'")
	palIndex = 0
	word = word.lower()
	for char in reversed(word):
		if char in alphabet:
			if char == palCheck[palIndex]:
				palIndex += 1
			else:
				print(f"{word} is not a palindrom")
				return False
		else:
			continue
	print(f"{word} is a palindrom")
	return True

word = input("Please enter a palindrom (a phrase that is spelled the same way both forward and backward): ")
check_palindrome(word)