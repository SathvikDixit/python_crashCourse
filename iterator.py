# An iterator is an object that allows you to traverse through sequenceone item at a time

myTuple = ("Apple", "Mango", "Orange")
myIter = iter(myTuple)
print(next(myIter))
print(next(myIter))
print(next(myIter))

print()


#Another example using a function

class myNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = myNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
