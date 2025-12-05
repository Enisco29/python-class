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

# class Book:
    
#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages
    
#     def __str__(self):
#         return f"'{self.title}' by {self.author}"
    
#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author
    
# book1 = Book("The Hobbit", "Robert", 310)
# book2 = Book("Harry Potter", "Stone", 333)
# book3 = Book("The Witcher", "Walker", 263)

# print(book1)
# print(book1 == book2)

#@property

# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
    
#     @property    
#     def width(self):
#         return f"{self._width:.1f}cm"
    
#     @property
#     def height(self):
#         return f"{self._height:.1f}cm"
    
#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width must be greater than 0")
            
#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("Height must be greater than 0")
            
#     @width.deleter
#     def width(self):
#         del self._width
#         print('Deleted successfully')
            
# rectangle = Rectangle(3, 4)

# rectangle.width =5

# del rectangle.width

# print(rectangle.width)
# print(rectangle.height)

#Decorator

# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("You add sprinkles")
#         func(*args, **kwargs)
#     return wrapper

# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("You add fudge")
#         func(*args, **kwargs)
#     return wrapper 

# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#     print(f"Here is your {flavor} ice cream")
    
# get_ice_cream("vanilla")

#exception

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something went wrong")
finally:
    print("Do some slean up")