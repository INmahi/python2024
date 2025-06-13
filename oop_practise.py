from vector import Vector as v

# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound

#     def speak(self):
#         print(f"{self.name} says {self.sound}")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, "Woof")
#         self.breed = breed

#     def fetch(self, item):
#         print(f"{self.name} fetches the {item}.")

# class Cat(Animal):
#     def __init__(self, name, color):
#         super().__init__(name, "Meow")
#         self.color = color

#     def scratch(self):
#         print(f"{self.name} scratches the furniture.")

# # Example usage
# dog = Dog("Buddy", "Golden Retriever")
# cat = Cat("Whiskers", "Tabby")

# dog.speak()
# dog.fetch("ball")

# cat.speak()
# cat.scratch()


##EASY ONE 

# from dataclasses import dataclass

# @dataclass
# class Person():
#     name :str
#     age : str
#     job : str
#     salary : str

#     def print_info(self):
#         print(f"Person's name is {self.name}. Person is {self.age} years old. Job: {self.job}. Salary: {self.salary}")

# a = Person("Mahi","21","St","0$")

# a.print_info()


#traditional


class Person():
    def __init__(self,name,age,job,salary):
        self.name = name
        self.age = age
        self.job = job
        self.salary = salary

    def print_info(self):
        print(f"Person's name is {self.name}. Person is {self.age} years old. Job: {self.job}. Salary: {self.salary}")


# mahi = Person("Maahi","21","student","0$")
# mahi.print_info()

#decorator
# a function that modifies other functions


# mechanism: @deco means func = deco(func)  or deco(func)(). so func now refers to mfx because this is was is being returned
def deco(fx):
    def mfx():
        print("Decorator Prefix")
        fx()
        print("decorator suffix")
    return mfx
@deco
def func():
    print("Hello main function")

# func()

class Model():
    def __init__(self, name):
        self.name = name
        self.accuracy = 0
    @classmethod
    def update_accuracy(cls, new_accuracy):
        if 0 <= new_accuracy <= 100:
            cls.accuracy = new_accuracy
        else:
            print("Invalid accuracy value!")

    def summary(self):
        print(f"{self.name} model accuracy: {self.accuracy}%")

# clf = Model("RandomForest")
# clf.summary()                     # 0%
# clf.update_accuracy(91.3)
# clf.summary()                     # 91.3%

# print(Model.accuracy)


# print("---------")

class NewEmp:

    company = "apple"

    @classmethod
    def cng_company(self,new_companny):

        self.company = new_companny

    def show_details(self):

        print(f"{self.name}'s company is {self.company}")


# e1 = NewEmp()
# e1.name = "Mahi"
# e1.show_details()

# e1.cng_company("tesla")

# e1.show_details()

# print(NewEmp.company) #tesla


v1 = v(1,2,3)
v2 = v(4,5,6)

# print(v1.angle_with(v2))

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
    def anatomy(self):
        print("Anatomy of the pet")
class Dog(Pet):
    def __init__(self, name, breed):
        Pet.__init__(self, name, species="Dog")
        self.breed = breed
    def fetch(self, thing):
        print(f"{self.name} goes after the {thing}!")
    def make_sound(self):
        print("Bark!")
class Cat(Pet):
    def __init__(self, name, breed):
        Pet.__init__(self, name, species="Cat")
        self.breed = breed
    def scratch(self, thing):
        print(f"{self.name} the cat scratches  {thing}!")

    def make_sound(self):
        print("Meow!")
    

# d = Dog("Dog", "Doggerman")
# d.make_sound()
# d.fetch("ball")
# c= Cat("Cat", "Catman")
# c.make_sound()

# c.anatomy()
