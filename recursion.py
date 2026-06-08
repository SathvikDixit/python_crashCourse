# Recursion function calling itself

def recr(n):
    if n < 0:
        print("Done!")
    else: 
        print(n)
        recr(n - 1)

recr(5)