import random

eyes = [":", ";", "X", "8", "B"]
noses = ["-", "^", ">", ""]
mouths = [")", "D", "S", "(", "P", "3"]

emote = random.choice(eyes) + random.choice(noses) + random.choice(mouths)
print(emote)
