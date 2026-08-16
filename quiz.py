print("*****welcome to the quiz game*****")
question_bank = [
    {"text": "What is the capital of France?", "answer": "Paris"},
    {"text": "What is 2 + 2?", "answer": "4"},
    {"text": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"text": "What is the capital of India?", "answer": "New Delhi"},      
]
options = [
    ["London", "Berlin", "Madrid", "Paris"],
    ["3", "4", "5", "6"],
    ["Earth", "Mars", "Jupiter", "Saturn"],
    ["Mumbai", "New Delhi", "Chennai", "Kolkata"]
] 
score=0 
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False
for question_num in range (len(question_bank)):
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
    
    guess = input("enter your answer")
    is_correct = check_answer(guess,question_bank[question_num]["answer"])
    if is_correct:
        print("you are correct")
        score += 1
    else:
        print("you are wrong")
        print(f"the correct answer is {question_bank[question_num]['answer']}")
    print(f"your final score is {score}")
    
        
    
