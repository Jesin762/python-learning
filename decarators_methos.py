#class method

class Person:
    species = "Human" 
    def __init__(self, name, age):
        self.name = name    
        self.age = age
        def show_details(self):
            return f"My name is {self.name}, I am {self.age} years old."
            @classmethod
            def show_species(cls):
                return f"We are {cls.species}s."
            @staticmethod
            def is_adult(age):
                return age >= 18

