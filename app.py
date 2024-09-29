from PyQt6.QtWidgets import QApplication



app = QApplication([])

from main_window import *


def change_box():
    if btn_next.text() == "Відповісти":
        radio_button_box.hide()
        answer_box.show()
        btn_next.setText("Наступне питання")
    elif btn_next.text() == "Наступне питання":
        radio_button_box.show()
        answer_box.hide()
        btn_next.setText("Відповісти")
    

 
btn_next.clicked.connect(change_box)

 

window.show()
app.exec()

