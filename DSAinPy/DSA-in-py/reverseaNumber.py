num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(f'Reversed String is: {rev}')

'''This is aritmatic solution *Time Complixity = O(log n)    *Space Complixity = O(1)'''


#Using Slicing method w/ same TC and SC
num = input('Enter the number: ')
print(f'Reversed String using slicing method: {num[::-1]}')
