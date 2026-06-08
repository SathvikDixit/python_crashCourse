# Recursion function calling itself

def recr(n):
    if n < 0:
        print("Done!")
    else: 
        print(n)
        recr(n - 1)

recr(5)



# Find 7th number of fibonacci sequence
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)
    
print(fibo(7))