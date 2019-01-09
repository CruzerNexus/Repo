def listAverage(nums):
    num = 0
    for i in range(len(nums)):
        num += nums[i]
        print(num)
    return num / len(nums)

n = 0
nums = []
while True:
    n = input('Please enter a number. If done, enter "done": ')
    # should add whatever "n" is to "a"
    if n == ("done"):
        break
    n = int(n)
    nums.append(n)

print(f"{listAverage(nums)}")
