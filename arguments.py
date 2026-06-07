# from datetime import datetime

# x = datetime.now()
# print(x.strftime("%X"))


# *args
def my_func(greetings, *names):
    for name in names:
        print(greetings, names)

my_func("Hello", "Sathvk", "Dixit")



# **kwargs
def func(**names):
    print("His last name is "+names["lname"])

func(fname = "Sathivk", lname = "Dixit")