#private

"""class student:
    def __init__(self):
        self.__name="jessin"
        self.age=20
    def display(self):
        print(self.__name,self.age)
ob=student()
ob.display()"""

#private with inheritence
 
class student:
    def __init__(self):
        self.__name="jessin"
        self.age=20
    def display(self):       
        print(self.__name,self.age)
class department(student):
    def show(self):
        print("name from student:", self._student__name)
    

ob=department()
ob.display()
ob.show()





    