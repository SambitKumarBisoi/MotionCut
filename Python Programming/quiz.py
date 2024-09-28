# Step 1: Define the quiz questions, options, and answers.
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. J.K. Rowling", "C. William Shakespeare", "D. Mark Twain"],
        "answer": "C"
    }
]

# Step 2: Function to ask a question and validate the answer.
def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    
    user_answer = input("Enter your answer (A, B, C, D): ").upper()
    while user_answer not in ['A', 'B', 'C', 'D']:
        print("Invalid input. Please enter a valid option (A, B, C, D).")
        user_answer = input("Enter your answer (A, B, C, D): ").upper()
    
    return user_answer

# Step 3: Function to check if the user's answer is correct.
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.\n")
        return False

# Step 4: Main function to run the quiz.
def run_quiz():
    score = 0
    total_questions = len(questions)

    for question_data in questions:
        user_answer = ask_question(question_data)
        if check_answer(user_answer, question_data["answer"]):
            score += 1

    print(f"You got {score} out of {total_questions} correct!")

# Step 5: Run the quiz
if __name__ == "__main__":
    run_quiz()
