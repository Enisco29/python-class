# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled
        
#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius
        
#     def describe(self):
#         print(f"It is a circle with an area of {3.14 * self.radius ** 2} cm^2")
#         super().describe()

# class Square(Shape):
#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width = width

# class Triangle(Shape):
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height
        
# circle = Circle(color="red", is_filled=True, radius=5)

# print(circle.describe())

#Duck typing
# class Animal:
#     alive = True
    
# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")
    
# class Cat(Animal):
#      def speak(self):
#         print("MEOW!")

#class methods

# class Students:
    
#     count = 0
#     total_gpa = 0
    
#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Students.count += 1
#         Students.total_gpa += gpa
     
    #INSTANCE METHOD   
#     def get_info(self):
#         return f"{self.name} {self.gpa}"
    
#     @classmethod
#     def get_count(cls):
#         return f"Total no of students: {cls.count}"
    
#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"{cls.total_gpa / cls.count}"
    
# student1 = Students("Spongebob", 3.2)
# student1 = Students("Patrick", 2.5)
    
# print(Students.get_count())
# print(Students.get_average_gpa())

class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
book1 = Book("The Hobbit", "Robert", 310)
book2 = Book("Harry Potter", "Stone", 333)
book3 = Book("The Witcher", "Walker", 263)

print(book1)
print(book1 == book2)