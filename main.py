#This is my first python program
# print("I love plantain")
# print("It's really tasty!")

#variables

# first_name = "Eniola"
# food = "plaintain"
# email = "fake.gmail.com"

# age=3 

# is_student = True

# if is_student: 
#     print("You are a student")
# else: 
#     print("You are not a student")

# print(f"Hello {first_name}")
# print(f"You like {food}")
# print(f"Your email is {email}")





# is_rich = False

# if is_rich: 
#     print('flex your money')
# else: print("keep coding")

#2d lists in python

# num_pad = ((1,2,3),
#            (4,5,6),
#            (7,8,9),
#            ("*",0,"#"))

# for num in num_pad:
#     for nums in num:
#         print(nums, end=" ")
#     print()

#Python quiz game

questions = (
             "Which animal lays the largest eggs?: ",
             "What is the best programming language?: ",
             "Which ai is the best?: "
             )

options = (
            ("A. Whale", "B. Elephant", "C. Ostrich"),
            ("A, Python", "B. Javascript", "C. Java"),
            ("A. ChatGPT", "B. Claude", "C. gemini")
        )

answers = ("C", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------")
    print(question)
    for option in options[question_num]:  
            print(option)  

    guess = input("Enter (A, B, C): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")   
    question_num += 1

print("---------------")
print("    RESULTS    ")
print("---------------")

print("answer: ", end="")
for answer in answers:
     print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
     print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")