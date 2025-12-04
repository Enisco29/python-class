# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale
        
#     def drive(self):
#         print(f"You drive a {self.model}")
        
# car1 = Car("Benz", 2026, "Black", False)

# print(car1.model)
# car1.drive()

# class Student:
    
#     class_year = 2025
#     num_student = 0
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_student += 1
        
# student1 = Student("Spongebob", 30)
# student2 = Student("Patrick", 35)

# print(student1.name)
# print(student1.age)
# print(Student.class_year)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Dog(Animal):
    def speak(self):
        print("woof!!")

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("Scooby")
cat = Dog("Garfield")
mouse = Dog("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.speak()