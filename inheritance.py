class Person:
    
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(f"First name is: {self.firstname}, Second name is: {self.lastname}")
    
x = Person("Sathvik", "Dixit")
x.printname()



