def myDecorator(func):
    def inner():
        print(f"Running {func.__name__} ")
        func()
        print("Completed")
        print()
    return inner


@myDecorator
def do_this():
    print("Done this")

@myDecorator
def do_that():
    print("Doing that")

do_this()
do_that()