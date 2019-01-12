import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']
socks = {'ankle': 0, 'crew': 0, 'calf': 0, 'thigh': 0}

for i in range(100):
	sock = random.choice(sock_types)
	socks[sock] += 1


print(sock)

for key in socks:
	if socks[key] % 2 != 0:
		print(f"{key} has a loner.")