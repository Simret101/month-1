class Vechicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def describe(self):
  
        print( self.model,self.make)
class Car(Vechicle):
    def __init__(self,make,model,num_doors):
        super().__init__(make,model)
        self._num_doors=num_doors
    def describe(self):
        print( self.model,self.make,self._num_doors)
    def color(self):
        print("The car is red color!")
class Bike(Car):
    def __init__(self,make,model,speed,_num_doors):
        super().__init__(make,model,_num_doors)
     
        self.__speed=speed
    def describe(self):
        print( self.make,self.model,self._num_doors,self.__speed)
    def color(self):
        print("The bike is blue color!")
obj=Vechicle("Toyota","Made by Suzuki")
obj2=Car("Made by Toyota","Lambergini",5)
obj3=Bike("Made by Lambergini","Suzuki",5,"130 m/s")
obj.describe()
obj2.describe()
obj2.color()
obj3.describe()
obj3.color()
