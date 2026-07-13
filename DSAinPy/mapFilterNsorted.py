# Here you're gonna learn about Map() Filter() and Sorted() functions. they're the built in functions in python

#Map(): Applies a function to all the objects in the iterable
numbers = [1, 2, 3, 4]
result1 = map(lambda x: x * 2, numbers)
print("This is Map(): ",list(result1))
print()


#Filter(): Keeps only the elements for which a function is true
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result2 = filter(lambda x: x % 2 == 0, numbers)
print("This is Filter(): ", list(result2))
print()


#Sorted(): Returns a new sorted list from a iterable
numbers = [10, 2, 5, 4, 3, 7, 9, 8, 1, 6]
print("This is Sorted(): ", sorted(numbers, reverse=False))