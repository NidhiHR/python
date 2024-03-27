
# from data import question_data
# Score=0

# question_bank=[]

# class Quiz:
#     def __init__(self,question,answer):
#         self.question=question
#         self.answer=answer

# class Question:
#     def __init__(self,q_list) :
#         self.question_number=0
#         self.question_list=q_list

#     def next_question(self):
#         while self.question_number<len(self.question_list):
#             cur_question=self.question_list[self.question_number]
#             ip=input(f"{self.question_number+1} : {cur_question.question} (True/False): ")
#             if ip.lower()==cur_question.answer.lower():
#                 global Score
#                 Score+=1
#                 print(f"YOUR ANSWER IS CORRECT AND YOUR SCORE IS {Score}")
#             else:
#                 print(f"YOUR ANSWER IS Wrong AND YOUR SCORE IS {Score}")
#             self.question_number+=1
#         else:
#             print("END OF QUIZ")

# for question in question_data:
#     question_text=question['text']
#     question_answer=question["answer"]
#     new_question=Quiz(question_text,question_answer)
#     question_bank.append(new_question)

# quiz=Question(question_bank)
# quiz.next_question()




from data import question_data

question_bank=[]

class Quiz:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer

class Question:
    def __init__(self,q_list) :
        self.question_number=0
        self.score=0
        self.question_list=q_list

    def still_has_question(self):
       return self.question_number<len(self.question_list)    
        
    def next_question(self):
        cur_question=self.question_list[self.question_number]
        self.question_number+=1
        ip=input(f"\n\n{self.question_number} : {cur_question.question} (True/False): ")
        self.check_answer(ip,cur_question.answer)

    def check_answer(self,ip,cur_ans):
        if ip.lower()==cur_ans.lower():
            print("ITS CRT ANSWER")
            self.score+=1
            print(f"ur current score is {self.score}/{self.question_number}")
        else:
            print("ITS WRONG ANSWER")
            print(f"THE CRT ANSWER IS {cur_ans}....and ur score is {self.score}/{self.question_number}")
         

for question in question_data:
    question_text=question['text']
    question_answer=question["answer"]
    new_question=Quiz(question_text,question_answer)
    question_bank.append(new_question)

quiz=Question(question_bank)

while quiz.still_has_question():
    quiz.next_question()
else:
    print("\n\n ITS THE END OF THE GAME")
    print(f"UR SCORE IS {quiz.score}/{len(quiz.question_list)}")


