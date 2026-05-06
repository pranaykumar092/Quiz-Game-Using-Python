questions = ("How many bones in humnan body: ",
              "How many planets in the solar system: ",
                "Which is The largest animal? : ",
                  "Which is the Longest river? : ",
                    "Which is the Largest ocean? : ",)
options = (("A. 207", "B. 206", "C. 209", "D. 203"),
           ("A. 5", "B. 4", "C. 8", "D. 9"),
           ("A. Tiger", "B. Whale", "C. ELephant", "D. Girrafe"),
           ("A. Ganga", "B. Amazon", "C. Nile", "D. None"),
           ("A. Pacific", "B. Arctic", "C. Indian", "D. Atlantic"))

answers = ("B", "C", "B", "C", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A B C D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    
    question_num += 1

print("---------------------------")
print("----------RESULT-----------")
print("---------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print("---------------------------")

print("Final Result")
result = int(score/ len(questions) * 100)
print(f"Your final Result is {result}%")
print("---------------------------")
