import random
def ask_question():
    question = input("Enter your question: ")
    return question


def pick_answer():
	answers = ["it is certain", "As I see it, yes","It is decidedly so","Without a doubt"," Yes definitely","You may rely on it",
	"Most likely","Outlook good","Yes","Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now",
	"Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no", "My sources say no"," Outlook not so good","Very doubtful"]

	print(random.choice(answers))
ask_question()
pick_answer()
