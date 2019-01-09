def calculator(x, y, z):

    if x == ("+"):
        return y + z
    elif x == ("-"):
        return y - z
    elif x == ("*"):
        return y * z
    else:
        return y / z

x = input("Welcome! What opperation would you like to preform (+, -, *, /)? ")
y = input("What is the first number? ")
y = float(y)
z = input("What is the second number? ")
z = float(z)
print(f"{y} {x} {z} = {calculator(x, y, z)}")
