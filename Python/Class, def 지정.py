# 클래스, 함수 지
'''
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def getName(self): #접근자
        print(self.name)
        
    def getAge(self): #접근자
        print(self.age)
    
class Employee(Person):
    def __init__(self, empName, empAge, empID):
        super().__init__(empName,empAge)
        self.empID=empID
        
    def getID(self):
        print(self.empID)
        
Obj=Employee("김대한", 65, 20123)
Obj.getName()
Obj.getAge()
Obj.getID()
'''
# class, 함수 지정
class Quadrangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    
    def getWidth(self):
        return self.width
        
    def getHeight(self):
        return self.height
    
    def periphery(self):
        self.periphery=2*(self.width+self.height)
        return self.periphery
        
    def area(self):
        self.area=self.width*self.height
        return self.area

class Square(Quadrangle):
    def __init__(self, width, height):
        super( ).__init__(width, height)
    
   
class Trapezoid(Quadrangle):
     def __init__(self, lowerside,height, topside):
        super( ).__init__(lowerside, height)
        self.topside=topside
        
     def area(self):
         self.area=(self.width+self.topside)*self.height/2
         return self.area
        
objSqu=Square(5,5)
print("squre info")
print("width:",objSqu.getWidth(),"height:",objSqu.getHeight(),end='')
print(" periphery:",objSqu.periphery(),"area:", objSqu.area())
print()
objTra=Trapezoid(10,5,2)
print("trapezoid info")
print("lowerside:",objTra.getWidth(),"topside:",objTra.topside,end='')
print(" height:",objTra.getHeight(),"area:", objTra.area())
