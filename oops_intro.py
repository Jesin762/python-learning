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

#inheritence

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
print(c1.color,c1.model)

