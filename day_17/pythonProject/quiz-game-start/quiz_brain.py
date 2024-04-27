class QuizBrain:
    def __init__(self, list_of_questions):
        self.questions_list = list_of_questions
        self.questions_number = 0
        self.correct_answers = 0

    def still_have_questions(self):
        return self.questions_number < len(self.questions_list)

    def next_question(self):
        question = self.questions_list[self.questions_number]
        self.questions_number += 1
        answer = input(f'Q{self.questions_number}: {question.question}'
                       f' (True/False): ')
        if self.check_answer(answer, question.answer):
            self.correct_answers += 1


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You are right!!!')
            self.correct_answers += 1
        else:
            print("You've got WRONG!!!")
        print(f'The correct answer is {correct_answer}')
        print(f'Your score is {self.correct_answers}/{self.questions_number}')
