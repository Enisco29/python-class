# def happy_birthday(name, age):
#     print(f"Happy Birthday to {name}!")
#     print("Happy Birthday to you!")
#     print("Happy Birthday dear friend.")
#     print("Happy Birthday to you!")
#     print()

# happy_birthday("lol")
# happy_birthday("lmao")

# #return
# def add(x, y):
#     z = x = y
#     return z

def create_name(first, last):
    first = first.upper()
    last = last.capitalize() 
    return first + " " + last

full_name = create_name("Ope", "Eniola")

print(full_name)