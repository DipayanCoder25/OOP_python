'''class Student:
    __School="XYZ"
    def __init__(self,name,age):
        self.__name=name
    def __display(self):
        print()    
std=Student("Ali",13)
print(std.__School)
'''
class Computer:
    __mxprize=900
    def __init__(self):
        pass
    def sell(self):
        print(f"The price is {self.__mxprize}")    
    def Asd(self,price):
        self.__mxprize=price
cd=Computer()
cd.sell()
cd.__mxprize=1000
cd.sell()                    
cd.Asd(1000)
cd.sell()

class Exam:
    def __init__(self,student_name):
        self.student_name=student_name
        self.__marks=0
    def set_marks(self,marks):
        if 0<=marks <=100:
            self.__marks=marks
        else:
            print("Invalid marks . Marks must be between 0 and 100")
    def get_marks(self):
        return self.__marks        
stu=Exam("Dipayan")
stu.set_marks(92)
print(f"{stu.student_name} Got {stu.get_marks()} Marks ") 

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y 
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
                      
p2=Point(2,4)
print(p2)
        