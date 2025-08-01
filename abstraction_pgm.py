from abc import ABC,abstractmethod
class parent(ABC):
    @abstractmethod
    def fun(self):
        pass

class child(parent):
    def display(self):
        print("hola!")
    def fun(self):
        print("hi there")

ob=child()
ob.display()  
ob.fun()      