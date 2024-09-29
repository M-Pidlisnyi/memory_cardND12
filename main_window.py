from PyQt6.QtWidgets import (QWidget, QLabel, 
                             QRadioButton, QPushButton,
                             QGroupBox, QButtonGroup,
                             QVBoxLayout, QHBoxLayout
                             )

card_width, card_height = 600, 500

window = QWidget()
window.resize(card_width, card_height)
window.setWindowTitle("Memory Card. Автор: ......")


question_lb = QLabel()

rb_answer_1 = QRadioButton()
rb_answer_2 = QRadioButton()
rb_answer_3 = QRadioButton()
rb_answer_4 = QRadioButton()

btn_next = QPushButton("Відповісти")

radio_button_box = QGroupBox("Варіанти відповідей")
radio_button_group = QButtonGroup()

radio_button_group.addButton(rb_answer_1)
radio_button_group.addButton(rb_answer_2)
radio_button_group.addButton(rb_answer_3)
radio_button_group.addButton(rb_answer_4)


answer_box = QGroupBox("Результат")
result_lb = QLabel("правильно/неправильно")
correct_answer_lb = QLabel("правильна відповідь")


main_v_line = QVBoxLayout()


radio_button_box_v_line = QVBoxLayout()
radio_button_box_h_line_1 = QHBoxLayout()
radio_button_box_h_line_2 = QHBoxLayout()

radio_button_box_h_line_1.addWidget(rb_answer_1)
radio_button_box_h_line_1.addWidget(rb_answer_2)

radio_button_box_h_line_2.addWidget(rb_answer_3)
radio_button_box_h_line_2.addWidget(rb_answer_4)

radio_button_box_v_line.addLayout(radio_button_box_h_line_1)
radio_button_box_v_line.addLayout(radio_button_box_h_line_2)

radio_button_box.setLayout(radio_button_box_v_line)

main_v_line.addWidget(question_lb)
main_v_line.addWidget(radio_button_box)



answer_box_v_line = QVBoxLayout()
answer_box_v_line.addWidget(result_lb)
answer_box_v_line.addWidget(correct_answer_lb)

answer_box.setLayout(answer_box_v_line)

main_v_line.addWidget(answer_box)

main_v_line.addWidget(btn_next)



answer_box.hide()
window.setLayout(main_v_line)

 