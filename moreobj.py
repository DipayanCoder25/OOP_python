class IOISring():
    def __init__(self):
        self.str1=""
    def getstring(self):
        self.str1=input("Enter a string ")
    def print_string(self):
        print("The string is ",self.str1.lower())
        
obj=IOISring()
obj.getstring()
obj.print_string()    

class Employee():
    def __init__(self):
        print("Employe Created")
        
    def __del__(self):
        print("Constructor created")
        
def Crete_Obj():
    print("Function Called")
    obj=Employee()
    print("Class called")
    return obj
    
print("Calling obj")
obj=Crete_Obj()
print("Done")

class pair_elements:
    def twosum(self,nums,target):
        lookup={}
        
        for i,num in enumerate(nums):
            if target-nums in lookup:
               return (lookup[target-num],i)
            lookup[num]=i

value=int(input("Enter the number u want to target"))
print("index1=%d, index2=%d" % pair_elements().twosum((10,20,30,40,50,60,70),value))