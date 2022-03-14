from data import question_data
from question_model import Question
from quiz_brain import BrainQuiz

# store all the Question object in an empty list
# where the text and the answer attribute is from the question_data(list of dictionary with text and answer keys)
# the text and and the answer becomes the attributes of the Question object

question_bank = []

for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    # crete question objects for each question and answer in question_data
    new_question_obj = Question(q_text, q_answer)
    # append each question objects to the question_bank list
    question_bank.append(new_question_obj)

quiz = BrainQuiz(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final result is {quiz.score}/{quiz.question_number}")
