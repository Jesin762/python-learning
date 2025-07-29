"""class laptops:
    def spec(self):
        print(self)
        self.RAM="4gb"
        self.MODEL="dell"
lap1=laptops()
lap1.spec()
print(lap1.RAM)"""


"""class laptops:
    owner="one team"
    def __init__(self,a,b):
        #print(self)
        self.RAM=a
        self.MODEL=b
lap1=laptops("16gb","dell")
lap2=laptops("4gb",'accer')

print(lap1.RAM)
print(lap2.RAM)
print(laptops.owner)"""

#inheritence--single inhertience
"""
class vehicles:
    def __init__(self,m,p):
        self.model=m
        self.power=p

class car(vehicles):
    def __init__(self,c,k,m,p):
        self.color=c
        self.make=k
        super().__init__(m,p)

c1=car("red","2008","ferarri","201bhp")
print(c1.color,c1.model)"""


#multiple inheritence

"""class father:
    def working(self):
        print("father:fashion designer")
class mother:
    def working(self):
        print("mother:model")
class child(father,mother):
    def working(self):
        father.working(self)
        mother.working(self)
        print("child:devolper")
c=child()
c.working()"""

#multiple inheritence using init

class person:
    def __init__(self,name):
        self.name=name
        super().__init__(name)
class salary:
    def __init__(self,salary):
        self.salary=salary
        super().__init__()
class department(person,salary):
    def __init__(self,name,salary,department):
        self.department=department
        super().__init__(name)
        salary.__init__(self,salary)
    def display(self):
        print(f"name:{self.name}")
        print(f"salary:{self.salary}")
        print(f"department:{self.department}")

m=department("aswin","2000","front end")
m.display()


   


