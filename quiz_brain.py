class QuizBrain:
    def __init__(self,q_list):
        self.q_number=0
        self.score=0
        self.list=q_list
    def next_question(self):
        q_text=self.list[self.q_number].text
        q_answer=self.list[self.q_number].answer
        q_option=self.list[self.q_number].ans_no
        self.q_number += 1
        print(f"Q.{self.q_number}:{q_text}")
        self.options()
        user_answer=int(input("choose your option "))
        self.check_answer(user_answer,q_option,q_answer)
    def still_has_questions(self):
        return self.q_number<len(self.list)
    def options(self):
        n=1
        q_options = self.list[self.q_number-1].options
        for option in q_options:
            print(f"{n}.{option}")
            n+=1
    def check_answer(self,user_answer,q_option,q_answer):
        if user_answer==int(q_option)+1:
            self.score+=1
            print("you got it right")
        else:
            print("thats wrong answer")
        print(f"the correct answer was:  {q_answer}")
        print(f"your current score is {self.score}/{self.q_number}")


