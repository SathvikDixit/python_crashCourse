# Fibonaccie Series with numbers
# Time Complexity: O(n)
# Space Comolexity: O(1)

n = int(input("Enter the number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end = " ")
    c = a + b
    a = b
    b = c


# Recursion method TC is O(2^n) and SC is O(n) so this is not a good method to use for large numbers