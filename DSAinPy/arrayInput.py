# With fixed size in an array [Integer]:
''' n = int(input("Enter the size of the array: "))
print("Now exter the array elements: \n")
arr =[]
for i in range (n):
    arr.append(int(input()))
print(arr) '''





# Without fixed array size [Integer]:
''' arr = list(map(int, input("Enter numbers use space and press enter after entering numbers: ").split()))
print(arr)'''




# Without fixed array size [String]:
arr = input("Enter words: ").split()
print(arr)