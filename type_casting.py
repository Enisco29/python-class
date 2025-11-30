#str(), int(), float(), bool()

# name = "Opeyemi Eniola"
# age = 17
# gpa = 5.0
# is_student = True

# gpa = int(gpa)
# age = float(age)
# age = str(age)

# print(type(age))

# name = input("What is yor name?:")
# age = int(input("What is ur age?: "))

# age = age + 1

# print(f"Hello {name}")
# print(f"you are now {age} years old")

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
    
# print(add(1, 2, 3))

# numbers = [1, 2,3 ,4 ,5 ]

# for number in numbers:
#     print(number)

email = "ope@gmailcom"

if "@" in email or "." in email:
    print("lol")

doubles = [x*2 for x in range(1, 11)]
print(doubles)

def is_week(dat):
    match(dat):
        case "lol":
            return True