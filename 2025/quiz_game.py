print("Welcome to my Quiz")

playing = input("Do You Want to Play? ").lower()

if playing != 'yes':
    quit()

print("Lets Play :)")
score = 0

answer = input("What does HTTP stand for? ").lower()
if answer == "Hypertext Transfer Protocol":
    print("correct!")
    score += 1
else:
    print("not correct!")  

answer = input("What is the maximum length of a filename in Windows? ").lower()
if answer == "255 characters":
    print("correct!")
    score += 1
else:
    print("not correct!")  
    
answer = input("What does DNS stand for? ").lower()
if answer == "Domain Name System":
    print("correct!")
    score += 1
else:
    print("not correct!")
    
answer = input("Which programming language is known as the 'mother of all languages'? ").lower()
if answer == "C":
    print("correct!")
    score += 1
else:
    print("not correct!")


print(f"You got {score} questions correct")
print(f"You got {score / 4 * 100} %")


#Using Function
def play_quiz():
    print("Welcome to the Python Quiz!")
    
    playing = input("Do you want to play? (yes/no): ").strip().lower()
    if playing != "yes":
        print("Okay, maybe next time!")
        return
    
    print("\nLet's play! Answer the following questions:")
    questions = [
        {"question": "What is the output of print(2 * 3 + 4)?", "answer": "10"},
        {"question": "What data type does type(3.14) produce?", "answer": "<class 'float'>"},
        {"question": "How do you create a list in Python? (Hint: Use square brackets)", "answer": "[]"},
        {"question": "What is the purpose of the len() function?", "answer": "to get the length of a list"},
        {"question": "What will this code output: my_dict = {'a': 1, 'b': 2}; print(my_dict.get('c', 'Not Found'))?", "answer": "Not Found"},
        {"question": "What keyword is used to define a function in Python?", "answer": "def"},
        {"question": "What does this code return: my_set = {1, 2, 3}; print(2 in my_set)?", "answer": "True"},
        {"question": "How can you make a Python loop iterate exactly 5 times? (Hint: Use range)", "answer": "for i in range(5)"},
        {"question": "What is the difference between 'is' and '==' in Python?", "answer": "is checks for identity, == checks for value equality"},
        {"question": "What is the output of def greet(name='World'): return f'Hello, {name}!'; print(greet('Python'))?", "answer": "Hello, Python!"},
    ]
    
    score = 0
    total_questions = len(questions)
    
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {q['answer']}")
    
    print("\nQuiz Complete!")
    print(f"You scored {score} out of {total_questions}!")
    print(f"Your percentage score is: {score / total_questions * 100:.2f}%")
    
    # Replay option
    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay == "yes":
        play_quiz()
    else:
        print("Thanks for playing!")

# Start the game
play_quiz()
