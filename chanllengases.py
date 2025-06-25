import random
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y) 
    def __add__(self,other):
        x=self.x+other.x 
        y=self.y+other.y
        return Point(x,y)
          
p1=Point(1,2)
p2=Point(2,3)
print(p1+p2)

class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if(self.a<other.a):
            return "Obj1 is less than Obj2"
        else:
            return "Obj2 is less than Obj1"
    def __eq__(self,other):
        if(self.a==other.a):
            return "Obj1 is euqal to Obj2"
        else:
            return "They aren't equal" 
        
obj=A(1)
Obj2=A(3)
print(obj<Obj2)
print("Passed values are ",obj.a,Obj2.a)

Obj3=A(4)
Obj4=A(4)
print(Obj3==Obj4)
              
              
class Fruitquiz:
    def __init__(self):
        self.fruits={'Apple':'red',
                     'Banana':'yellow',
                     'Watermelon':'green',
                     'Pumkin':'orange' }    
        
        
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruits.items()))
            
            print("What color is it {}".format(fruit))
            user_guess=input().lower()
            
            if(user_guess==color):
                print("You won")
            else:
                print("You lose")
            ioption=int(input(("Press 0 If you want to play again,Otherwise 1")))
        
            if(ioption):
                break
print("Welcome to Fruitquiz ")           
f=Fruitquiz()
f.quiz()
            
            
class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
        
    def __str__(self):
        return self.word + '(' + self.meaning  + ')'
flash=[]
    
while(True):
    word=input("Enter the word: ")
    meaning=input("Enter the meaning of the word")

    flash.append(flashcard(word,meaning))
    
    option=input("Enter 0 if u want to play again,otherwise 1")
    if(option):
        break
    
for i in flash:
    print("<",i)
                  
                    
                                  