num = int(input('Enter the number: '))
rev = 0
original = num
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if original == rev:
    print ("Given number is Palindrome")
else:
    print("Given number is not a Palindrome")

# Time Complixity = O(log n)
# Space Complixity = O(1)
# This method is only for Integer values or numbers
print()
print()
print()









# This is universal palindrome checker(Integer, String)
# Same TC and SC 
pal = input("Enter palindrome: ")
notPal = pal[::-1]
if notPal == pal:
    print(f"{pal} is palindrome")
else:
    print(f"{pal} is not a palindrome")