# def two_sum(nums, target):
#     seen = {}

#     for i, num in enumerate(nums):
#         compliment  = target - num

#         if compliment in seen:
#             return [seen[compliment],i]
#         seen[num] = i
#     return[]

# nums = {2, 3, 5, 8, 9}
# target = 7
# result = two_sum(nums, target)

# print(result)




#-------------------------------------------------------Brute Froce---------------------------------------------------
class Solution:
    def twoSum_indices(self, arr, target):
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] + arr[j] == target:
                    return [i, j]
        return [-1, -1]
    
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 4, 8, 4, 9]
    target = 13

    print("Found at indix: ",sol.twoSum_indices(arr, target))