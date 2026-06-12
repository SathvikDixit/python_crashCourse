def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        compliment  = target - num

        if compliment in seen:
            return [seen[compliment],i]
        seen[num] = i
    return[]

nums = {2, 3, 5, 8, 9}
target = 7
result = two_sum(nums, target)

print(result)