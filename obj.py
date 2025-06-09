class fruit:
    taste="Sweet"
    def __init__(self,name,color):
        self.name=name
        self.color=color
        
apple=fruit('Apple','Red')
banana=fruit('Banana','Yellow')
print(apple.name,apple.color)
print(banana.name,banana.color) 

class vechile:
    def __init__(self,mx_speed,milleages):
        self.mx_speed=mx_speed
        self.milleages=milleages
Modelx=vechile(240,19)
print("ModelX  Mx Speeed ",Modelx.mx_speed)
print("ModelX mileages is :",Modelx.milleages)         

class parrot:
    specices='Bird'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
blu=parrot("Blu",10)
woo=parrot("Woo",15)

print("Blu is {}".format(blu.specices))
print("Woo is {}".format(woo.specices))

print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age)) 
         
class dog:
    def __init__(self,breed_name,age):
        self.breed_name=breed_name
        self.age=age
    def disply(self):
        print("The breed name of dog is ",self.breed_name)
        print("The age of the dog is ",self.age) 
        
mix1=dog("Mixed",13)
mix1.disply()                    