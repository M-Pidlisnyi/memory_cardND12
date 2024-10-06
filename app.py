from random import choice, shuffle
from PyQt6.QtWidgets import QApplication
app = QApplication([])

from main_window import *

class Question():
    def __init__(self, question_text, answer_text, wrong:tuple) -> None:
        self.question_text = question_text
        self.answer_text = answer_text
        # self.wrong1 = wrong1
        # self.wrong2 = wrong2
        # self.wrong3 = wrong3
        self.wrong_answers = wrong

    def got_right(self):
        ...
    def got_wrong(self):
        ...


q1 = Question("Яблуко", "apple", ("application", "ape", "pineapple"))
q2 = Question("Миша", "mouse", ("muse", "moose", "mile"))
q3 = Question("Дім", "house", ("hurry", "course", "loose"))
q4 = Question("Друг", "friend", ("fiend", "fred", "fed"))


questions_list = [ q1,q2,q3,q4 ]
radio_button_list = [rb_answer_1,rb_answer_2, rb_answer_3, rb_answer_4 ]

def new_question():
    random_question = choice(questions_list)

    shuffle(radio_button_list)

    question_lb.setText(random_question.question_text)

    radio_button_list[0].setText(random_question.answer_text)
    for i in range(3):
        radio_button_list[i+1].setText(random_question.wrong_answers[i])

new_question()

def change_box():
    if btn_next.text() == "Відповісти":
        radio_button_box.hide()
        answer_box.show()
        btn_next.setText("Наступне питання")
    elif btn_next.text() == "Наступне питання":
        radio_button_box.show()
        answer_box.hide()
        btn_next.setText("Відповісти")
        new_question()

 
btn_next.clicked.connect(change_box)

 

window.show()
app.exec()

