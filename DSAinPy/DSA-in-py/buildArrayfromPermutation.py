#Leetcode: 1920
#Build an array from permutation
def buildArrPermut(nums):
    ans = []

    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    return ans

nums = [0, 2, 1, 5, 3, 4]
result = buildArrPermut(nums)
print(result)
