from Question import question_data

from LOGO import logo

print(logo)

from question_model import Question

from brain import Brain


question_bank = []

for question in question_data :
  question_text = question["text"]
  question_answer = question["answer"]
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)

quiz = Brain(question_bank)

while quiz.still_have_questions() :
  quiz.next_question()
  
print("You have completed the quiz..")
print(f"Your final score is : {quiz.score}/{quiz.number}")
