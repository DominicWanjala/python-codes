# Multiple inheritance
class Animal:
    def legs(self):
        print("It has four legs")
    def leneage(self):
        print("it give birth to young ones")
class Canivore:
    def feeding(self):
        print("They eat meat")
class Leo:
    def temp(self):
        print("It is warm blooded")
    def fur(self):
        print("Its body is covered with fur")
class cat(Animal,Leo,Canivore):
    def food(self):
        print(" The cat eats rats")
    def sound(self):
        print("A cat meows")

c = cat()
c.leneage()
c.feeding()
c.temp()
c.legs()
c.fur()
c.sound()
c.food()
