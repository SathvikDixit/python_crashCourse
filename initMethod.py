
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
print()





# writing a practice code using multiple methods
class playlist:
    def __init__(self):
        # self.name = name
        self.songs = [ ]

    def add_songs(self, song):
        self.songs.append(song)
        print(f"{song} Song Added")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"{song} song removed")
    
    def show_songs(self):
        for song in self.songs:
            print(f"- {song}")

my_playlist = playlist()
my_playlist.add_songs("Massa Massa")
my_playlist.add_songs("Helloallo")
my_playlist.show_songs()
my_playlist.remove_song("Massa Massa")
my_playlist.show_songs()