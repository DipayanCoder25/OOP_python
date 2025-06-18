from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Value passed ",x)
    @abstractmethod    
    def task(self):
        print("We r inside Absclasss") 
class testclass(Absclass):
    def task(self):
        print("We r inside Testclass ")
to=testclass()
to.task()
to.print(1002)                   



class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can run and think") 
class Snake(Animal):
    def move(self):
        print("I can scare ppl") 
h=Human()
h.move()
h=Snake()
h.move()
                    

class Square:
    def __init__(self,side):
        self.side=side
    def area(self):
        print(" my area is ",self.side**2)
class Circle:
    def __init__(self,radious):
        self.radious=radious
    def area(self):
        print("Circle radious is ",3.14*self.radious*self.radious)      
osquare=Square(5)
ocircle=Circle(5)

for shape in (osquare,ocircle):
    shape.area()        
                      