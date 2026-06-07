# from datetime import datetime

# x = datetime.now()
# print(x.strftime("%X"))


def my_func(greetings, *names):
    for name in names:
        print(greetings, name)

my_func("Hello", "Sathvk", "Dixit")