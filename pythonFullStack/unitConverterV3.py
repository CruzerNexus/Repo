def distToMeters(x, y):
    x = float(x)
    if y == ("ft"):
        return x * 0.3048
    elif y == ("mi"):
        return x * 1609.34
    elif y == ("km"):
        return x * 1000
    elif y == ("yd"):
        return x * 0.9144
    elif y == ("in"):
        return x * 0.0254
    else:
        return x

x = input("Enter a distance: ")
y = input("Enter ft, mi, m, km, yd, or in: ")
print(f"{x} {y} is equal to... ")
print(f"{distToMeters(x, y)} meters.")
