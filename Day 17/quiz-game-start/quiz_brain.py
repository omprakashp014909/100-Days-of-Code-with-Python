class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number  < len(self.questions_list) 

        
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        response =  input(f"Q.{self.question_number}: {current_question.text} (True/False?)\n")
        self.check_answer(response, current_question.answer)


    def check_answer(self, response, answer):
        if response.lower() == answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was {answer}.")
        print(f"Your current score is {self.score}/{self.question_number }.\n\n")


       