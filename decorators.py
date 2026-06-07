# def myDecorator(func):
#     def inner():
#         print(f"Running {func.__name__} ")
#         func()
#         print("Completed")
#         print()
#     return inner

# @myDecorator
# def do_this():
#     print("Done this")

# @myDecorator
# def do_that():
#     print("Doing that")
# do_this()
# do_that()





# def changeCase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changeCase
# def myy_func():
#     return "hello bro!"

# print(myy_func())





def smart_div(func):
    def myInner(a,b):
        if a < b:
            a,b = b,a    
            return func(a, b)
        else:
            print(a / b)
    return myInner

@smart_div
def div(a,b):
    print(a/b)
div(10, 5)