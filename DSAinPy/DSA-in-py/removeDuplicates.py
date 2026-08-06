number = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5]
result = []
seen = set()

for num in number:
    if num not in result:
        result.append(num)
        seen.add(num)
print(result)
# Time Complixity: O(n)     Space Complixity: O(n)


'''
number = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5]
result = []

for num in number:
    if num not in result:
        result.append(num)
print(result)   '''
#Time Complixity: O(n^2)    Space Complixity: O(n)