def listAverage(nums):
    num = 0
    for i in range(len(nums)):
        num += nums[i]
        print(num)
    return num / len(nums)

print(f"{listAverage(nums = [5, 0, 8, 3, 4, 1, 6])}")
