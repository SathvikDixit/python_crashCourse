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
    print(f'Your number {num} is not an Armstrong number')