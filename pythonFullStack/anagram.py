#anagram.py
def check_anagram(word, drow):
	newWord = word.lower().replace(" ", "")
	newDrow = drow.lower().replace(" ", "")
	wordList = sorted(newWord)
	drowList = sorted(newDrow)
	if wordList == drowList:
		print(f'"{word}" and "{drow}" are anagrams of each other.')
		return True
	else:
		print(f'"{word}" and "{drow}" are not anagrams of each other.')
		return False
	

print("Welcoming to the anagram detector (by Cruzertech)!")
word = input("Please enter the first word: ")
drow = input("Please enter the second word: ")

check_anagram(word, drow)