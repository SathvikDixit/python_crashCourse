num = int(input("Enter the number: "))

if num <= 1:
    print("Not Prime")
else:
    isPrime = True

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        print("Prime Number")
    else:
        print("Not Prime")