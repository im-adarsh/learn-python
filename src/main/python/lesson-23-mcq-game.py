from src.main.python.classes.Question import Question

questions_prompts = [
    "What color are apples?\n(a) Red\n(b) Green\n(c) Purple\n(d) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Purple\n(d) Yellow\n\n",
    "What color are strawberries?\n(a) Pink\n(b) Green\n(c) Purple\n(d) Orange\n\n"
]

questions = [
    Question(questions_prompts[0], "a"),
    Question(questions_prompts[1], "d"),
    Question(questions_prompts[2], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        if(question.answer == input(question.prompt)):
            score+=1

    return score

print("You got " + str(run_test(questions)) + " out of "+str(len(questions))+" correct.")
