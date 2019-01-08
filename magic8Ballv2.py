import random

question = ("")
question = input("Ask a question and receive my wisdom: ")
while question != ("done"):
    answer = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Indeed.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My soucreces say no.", "Outlook not so good.", "Very doubtful."]
    secure_random = random.SystemRandom()
    print(secure_random.choice(answer))
    question = input('If satisfied, speaketh "done" and I will depart. Else, question again: ')
print("Until your next querry, traveller...")
