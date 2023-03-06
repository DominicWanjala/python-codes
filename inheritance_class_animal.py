#inheritance
class Animal:
    def legs(self):
        print("I have four legs")
    def fur(self):
        print("My body is covered with fur")
class Dog( ):
    def bark(self):
        print("The dog barks")
class cat(Animal,Dog):
    def canivore(self):
        print("eats rats")
c = cat()
c.bark()
c.legs()
c.fur()
c.canivore()