# from datetime import datetime

# x = datetime.now()
# print(x.strftime("%X"))


print()


# *args
def my_func(greetings, *names):
    print(type(names))
    for name in names:
        print(greetings, name)

my_func("Hello", "Sathvk", "Dixit")


print()


# **kwargs
def func(**names):
    print(type(names))
    print("His last name is "+names["lname"])

func(fname = "Sathivk", lname = "Dixit")