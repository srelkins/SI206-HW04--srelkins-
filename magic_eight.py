import random
def ask_question():
    question = input("Enter your question: ")
    answers = ["it is certain", "As I see it, yes","It is decidedly so","Without a doubt"," Yes definitely","You may rely on it",
    "Most likely","Outlook good","Yes","Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now",
    "Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no", "My sources say no"," Outlook not so good","Very doubtful"]
    while question != "Quit":
        if question[-1] != "?":
            print("I'm sorry, I can only answer questions.")
        else:
            print(random.choice(answers))
        return question
    # if question == "Quit":
    #     break

ask_question()
