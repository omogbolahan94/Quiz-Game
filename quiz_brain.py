class BrainQuiz:
    """
    :param: q_list is a list of Question objects
    """
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        """

        :return: a boolean is self.question_number is less or more
        than total number of question objects in self.question_list
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        This will call the next question based on the number of question
        :return:
        """
        question_number = self.question_number
        self.question_number += 1
        current_question = self.question_list[question_number].text
        current_answer = self.question_list[question_number].answer.lower()
        answer = input(f"Q.{self.question_number} {current_question} (True/False): ").lower()
        self.check_answer(answer, current_answer)

    def check_answer(self, user_answer, current_answer):
        """
        veriify is selected answer is correct or wrong
        :param user_answer:
        :param current_answer:
        :return:
        """
        if user_answer == current_answer:
            self.score += 1
            print("You're right!")
        else:
            print('You are wrong!')

        print(f"The correct answer is {current_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")










