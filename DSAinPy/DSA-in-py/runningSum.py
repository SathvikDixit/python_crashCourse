#Leetcode 1480
def runningSumm(nums):
    ans = []
    total = 0
    for num in nums:
        total += num
        ans.append(total)
    return ans
nums = [1, 2, 3, 4]
result = runningSumm(nums)
print(result)
