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

from dataclasses import dataclass

@dataclass
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


mahi = Person("Maahi","21","student","0$")
mahi.print_info()