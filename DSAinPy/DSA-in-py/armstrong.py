# Armstrong Number
# An Armstrong number is a number that is equal to the sum of its digits each raised to the power of the number of digits 

num = int(input('Enter a number: '))
original = num
length = len(str(num))
total = 0
while num > 0:
    digit = num % 10
    total = total + digit**length
    num //= 10
if original == total:
    print(f'Your number {original} is an Armstrong number')
else:
    print(f'Your number {original} is not an Armstrong number')
# Time Complixity = O(log n)        Space Complixity = O(log n)








