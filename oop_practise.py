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