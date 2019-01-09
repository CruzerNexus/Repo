def distToMeters(x, y):
    x = float(x)
    if y == ("ft"):
        return x * 0.3048
    elif y == ("mi"):
        return x * 1609.34
    elif y == ("km"):
        return x * 1000
    else:
        return x

x = input("Enter a distance: ")
y = input("Enter ft, mi, m or km: ")
print(f"{x} {y} is equal to... ")
print(f"{distToMeters(x, y)} meters.")
