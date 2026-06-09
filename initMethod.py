
# __init__ method is a special method used for initilizing objects. It is called when the object is created
class myClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# __str__ method is a special method used to define user readable string representation of an object
    def __str__(self):
        return f"My name is: {self.name}, Age is: {self.age}"


b1 = myClass("Sathvik", 22)
print(b1.name)
print(b1.age)

print(b1) # printed using __str__ method