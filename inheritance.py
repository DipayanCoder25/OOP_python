'''class dad:
    def __init__(self,eyes,aggresive):
        self.eyes=eyes
        self.aggresive=aggresive
        
    def display(self):
        print("Your eyeball is",self.eyes)
        print("Your aggresiveness is ",self.aggresive) 
class son(dad):
    def __init__(self,name,age,eyes,aggresive):
        self.name=name
        self.age=age 
        
        dad. __init__(self,eyes,aggresive)
            
obj=son("Penguin",10,"Blue",True)
obj.display()
    
class  person():
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber) 
class Employee(person):
    def  __init__(self, name, idnumber,salary,position):
        self.salary=salary
        self.position=position
        super().__init__(name, idnumber)                   
obj=Employee("Rahul",1221221,2000000,"Ceo") 
obj.display() 
'''   
class Bird():
    def __init__(self):
        print("Bird is ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("Bird swims faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()                                
        print("Penguin is ready")
    def whoisThis(self):
        print("Penguin")
    def Run(self):
        print("Penguin runs faster") 
peggy=Penguin()
peggy.whoisThis()
peggy.swim()
peggy.Run()
           