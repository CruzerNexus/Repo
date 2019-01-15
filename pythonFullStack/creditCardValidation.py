# creditCardValidation.py


def creditCardValidation(num):
    # turns string into list of ints
    num = list(num)
    print(num)
    for i, digit in enumerate(num):
        num[i] = int(num[i])
        # print(i)
        # print(num[i])
    # check digit
    checkNum = num.pop(-1)
    print(checkNum)
    print(num)
    # reverse digits
    num.reverse()
    print(num)
    total = 0
    # doubling every other element
    for i in range(0, len(num), 2):
        num[i] = num[i]*2
        # subtract 9 from every number over 9
    # find sum of all values
    for i in range(len(num)):
        if num[i] > 9:
            num[i] -= 9
        total += num[i]
    print(num)
    print(total)
    # if second digit of sum is the check number, valid
    if total % 10 == checkNum:
        return "valid!"
    else:
        return "invalid."


cardNum = input("Please enter card number: ")
print(f"The card you entered is {creditCardValidation(cardNum)}")
print(creditCardValidation("4556737586899855"))
