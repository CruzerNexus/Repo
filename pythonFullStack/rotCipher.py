userLetter = ['a', 'b', 'c', 'd', "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cipherLetter = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 'a', 'b', 'c', 'd', "e", "f", "g", "h", "i", "j", "k", "l", "m"]
def encode(userInput):
    pcOutput = ""
    for char in (userInput):
        if char in (userLetter):
            idx = userLetter.index(char)
            pcOutput += cipherLetter[idx]
        else:
            pcOutput += char
    return pcOutput

def decode(userInput):
	pcOutput = ""
    for char in (userInput):
        if char in cipherLetter:
            idx = cipherLetter.index(char)
            pcOutput += userLetter[idx]
        else:
            pcOutput += char
    return pcOutput


userInput = input("Give me a secret message and I'll encode it: ")

print(encode(userInput))
print(f"and {encode(userInput)} decoded is {decode(userInput)}.")
