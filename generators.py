# def func():
#     yield 1
#     yield 2
#     yield 3
# for i in func():
#     print(i)


# A generator is a function that can pause and resume its execution. When a generator function is called it returns a generator object the produces the values one item at a time, on demand insted of storing all the values at once.


# this generator prints numbers from 1 to 5
def myfunc(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in myfunc(5):
    print(num)
