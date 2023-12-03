from question_model import Question
from quiz_brain import QuizBrain
from get_api import API

question_bank = []
api = API("https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
question_api = api.get_json_data()

for question in question_api["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

has_question = True
quiz = QuizBrain(question_bank)

while has_question:
    quiz.next_question()
    has_question = quiz.still_has_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
