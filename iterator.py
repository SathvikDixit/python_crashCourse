# An iterator is an object that allows you to traverse through sequenceone item at a time

myTuple = ("Apple", "Mango", "Orange")
myIter = iter(myTuple)
print(next(myIter))
print(next(myIter))
print(next(myIter))
