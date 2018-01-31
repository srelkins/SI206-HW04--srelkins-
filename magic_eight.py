def ask_question():
    question = input("Enter your question: ")
    while question != "Quit":
        return question
    if question == "Quit":
        break

if question.split([-1]) != "?":
    print("I’m sorry, I can only answer questions.")

ask_question()
