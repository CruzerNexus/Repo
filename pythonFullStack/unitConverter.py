def feetToMeters(x):
    return x * 0.3048

x = input("Enter how many feet (ft) to get the meters (m) equivalent: ")
print(f"{x} feet is equal to... ")
x = float(x)
print(f"{feetToMeters(x)} meters.")
