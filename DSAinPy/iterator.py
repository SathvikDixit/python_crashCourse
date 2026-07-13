nums = [1, 2, 3, 4]
it = iter(nums)
# print(next(it))
# print(next(it))


# OR
# for num in it:
#     print(num)

# OR
while True:
    try:
        print(next(it))
    except StopIteration:
        break