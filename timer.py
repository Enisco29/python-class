# import time

# my_time = int(input("Enter the time in secs: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     min = int(x / 60) % 60
#     hrs = int(x / 3600)
#     print(f"{hrs}:{min:02}:{seconds:02}")
#     time.sleep(1)

# print("Time's up")

# rows = int(input("Enter the no of rows: "))
# coloums = int(input("Enter the no of rows: "))
# symbol = input("Enter a symbol to use: ")


# for y in range(rows):
#     for x in range(coloums):
#         print(symbol, end="")
#     print()    

# fruits = ["apple", "orange", "banana", "coconut"]

# fruits.append("pineapple")
# fruits.insert(0, "mango")

# print(fruits)

# print(dir(fruits))

# question = "appl" in fruits
# print(question)

# print(fruits[::-1])

# for x in fruits:
#     print(x)

import random

low = 1
high = 100
options = ("rock", "paper", "scissor")
cards = ["2", "3", "4", "k", "j"]

# number = random.randint(low, high)
# number = random.random()
# option = random.choice(options)
random.shuffle(cards)


print(cards)

import type_casting

result = type_casting.pi

print(result)

def func1():
    x = 1
    def func2():
        print(x)
    func2()


func1() 