# lenght = int(input("enter the length"))
# width = int(input("enter the width"))
# area = lenght * width

# print(f"the area is {area}")

# adjective1 = input("Enter an adjective: (description)")
# noun1 = input("Enter a noun: (person, place, or thing)")
# adjective2 = input("Enter another adjective: (description)")
# verb1 = input("Enter a verb: (doing word)")
# adjective3 = input("Enter one more adjective: (description)") 

# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}")

# x = 3.14
# y = 4
# z = 5

# result = round(x)
# result = abs(y)
# result = pow(2, 3)

# print(result)

capitals = {
            "USA": "LA",
            "India": "New Dehli",
            "China": "Beijing"
            }

# print(capitals.get("US"))
# capitals.update({"germany": "Berlin"})

items = capitals.items()

for key, vlaue in items:
    print(f"{key}: {vlaue}")