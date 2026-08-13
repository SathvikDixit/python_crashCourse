#Leetcode 1480
def ShuffleTheArray(nums, n):
    ans = []
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i+n])
    return ans
nums = [1, 2, 3, 4, 5, 6]
n = 3
result = ShuffleTheArray(nums, n)
print(result)
# T.C = O(n)
# S.C = O(n)