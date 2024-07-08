import os 
from LOGO import logo
def clear_screen() :
  os.system('cls' if os.name == 'nt' else 'clear')


class Brain :
  def __init__ (self , question_list) :
    self.number = 0
    self.score = 0 
    self.list = question_list

  def still_have_questions(self) :
    if self.number < len(self.list) :
      return True 
    else :
      False 
  

  def next_question(self) :
    current_question = self.list[self.number]
    current_question_text = current_question.text
    self.number += 1
    user = input(f"Q:{self.number}- {current_question_text} (True/False)?\nYour Answer: ")
    self.check_answer (user , current_question.answer)

  def display_logo():
    clear_screen()
    print(logo)
    
  def check_answer(self , correct_answer , user) :
    if user.lower() == correct_answer.lower() :
      self.score += 1 
      print('You got it right...')
    else :
      print("You got it wrong....\nBetter luck next time....")
    print(f"The correct answer was : {correct_answer}")
    print(f"Your current score is : {self.score}")
    print("\n")
    

