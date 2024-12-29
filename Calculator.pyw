from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtGui import QTextCursor


class Window(QWidget):
    def __init__(self):
        # Initiating the main window
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(500, 430)
        
        # Set the background color using QPalette, it only affects the window background
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#2E2E2E"))  # Dark color
        self.setPalette(palette)
        
        # Setting the layouts
        vertical_layout1 = QVBoxLayout()
        horizontal_layout1 = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()
        horizontal_layout3 = QHBoxLayout()
        horizontal_layout4 = QHBoxLayout()
        self.setLayout(vertical_layout1)
        vertical_layout1.setContentsMargins(10, 10, 10, 10)
        vertical_layout1.setAlignment(Qt.AlignCenter)
        
        # This part is for the text box
        text_box1 = QTextEdit(readOnly = True)
        text_box1.setFixedSize(475, 80)
        text_box1.setFontPointSize(25)
        
        # Define a font size for all buttons
        button_fontsize = "font-size: 25px;"
        
        # This part is for the buttons (1st row)
        button_1 = QPushButton("1", clicked = lambda: when_button1_is_clicked())
        button_1.setFixedSize(90, 75)
        button_1.setStyleSheet(button_fontsize)
        button_2 = QPushButton("2", clicked = lambda: when_button2_is_clicked())
        button_2.setFixedSize(90, 75)
        button_2.setStyleSheet(button_fontsize)
        button_3 = QPushButton("3", clicked = lambda: when_button3_is_clicked())
        button_3.setFixedSize(90, 75)
        button_3.setStyleSheet(button_fontsize)
        button_del = QPushButton("DEL", clicked = lambda: when_button_del_is_clicked())
        button_del.setFixedSize(90, 75)
        button_del.setStyleSheet(button_fontsize)
        button_ac = QPushButton("AC", clicked = lambda: when_button_ac_is_clicked())
        button_ac.setFixedSize(90, 75)
        button_ac.setStyleSheet(button_fontsize)
        
        # This part is for the buttons (2nd row)
        button_4 = QPushButton("4", clicked = lambda: when_button4_is_clicked())
        button_4.setFixedSize(90, 75)
        button_4.setStyleSheet(button_fontsize)
        button_5 = QPushButton("5", clicked = lambda: when_button5_is_clicked())
        button_5.setFixedSize(90, 75)
        button_5.setStyleSheet(button_fontsize)
        button_6 = QPushButton("6", clicked = lambda: when_button6_is_clicked())
        button_6.setFixedSize(90, 75)
        button_6.setStyleSheet(button_fontsize)
        button_multiply = QPushButton("*", clicked = lambda: when_button_multiply_is_clicked())
        button_multiply.setFixedSize(90, 75)
        button_multiply.setStyleSheet(button_fontsize)
        button_divide = QPushButton("/", clicked = lambda: when_button_divide_is_clicked())
        button_divide.setFixedSize(90, 75)
        button_divide.setStyleSheet(button_fontsize)
        
        # This part is for the buttons (3rd row)
        button_7 = QPushButton("7", clicked = lambda: when_button7_is_clicked())
        button_7.setFixedSize(90, 75)
        button_7.setStyleSheet(button_fontsize)
        button_8 = QPushButton("8", clicked = lambda: when_button8_is_clicked())
        button_8.setFixedSize(90, 75)
        button_8.setStyleSheet(button_fontsize)
        button_9 = QPushButton("9", clicked = lambda: when_button9_is_clicked())
        button_9.setFixedSize(90, 75)
        button_9.setStyleSheet(button_fontsize)
        button_add = QPushButton("+", clicked = lambda: when_button_add_is_clicked())
        button_add.setFixedSize(90, 75)
        button_add.setStyleSheet(button_fontsize)
        button_minus = QPushButton("-", clicked = lambda: when_button_minus_is_clicked())
        button_minus.setFixedSize(90, 75)
        button_minus.setStyleSheet(button_fontsize)
        
        # This part is for the buttons (4th row)
        button_0 = QPushButton("0", clicked = lambda: when_button0_is_clicked())
        button_0.setFixedHeight(75)
        button_0.setStyleSheet(button_fontsize)
        button_dot = QPushButton(".", clicked = lambda: when_button_dot_is_clicked())
        button_dot.setFixedHeight(75)
        button_dot.setStyleSheet(button_fontsize)
        button_answer = QPushButton("=", clicked = lambda: when_button_answer_is_clicked())
        button_answer.setFixedHeight(75)
        button_answer.setStyleSheet(button_fontsize)
        
        # Adding the buttons (1st row) to horizontal_layout1
        horizontal_layout1.addWidget(button_1)
        horizontal_layout1.addWidget(button_2)
        horizontal_layout1.addWidget(button_3)
        horizontal_layout1.addWidget(button_del)
        horizontal_layout1.addWidget(button_ac)
        
        # Adding the buttons (2nd row) to horizontal_layout2
        horizontal_layout2.addWidget(button_4)
        horizontal_layout2.addWidget(button_5)
        horizontal_layout2.addWidget(button_6)
        horizontal_layout2.addWidget(button_multiply)
        horizontal_layout2.addWidget(button_divide)
        
        # adding the buttons (3rd) to horizontal_layout3
        horizontal_layout3.addWidget(button_7)
        horizontal_layout3.addWidget(button_8)
        horizontal_layout3.addWidget(button_9)
        horizontal_layout3.addWidget(button_add)
        horizontal_layout3.addWidget(button_minus)
        
        # adding the buttons (4th) to horizontal_layout4
        horizontal_layout4.addWidget(button_0)
        horizontal_layout4.addWidget(button_dot)
        horizontal_layout4.addWidget(button_answer)
        
        # Adding widgets to the layouts
        vertical_layout1.addWidget(text_box1)
        vertical_layout1.addLayout(horizontal_layout1)
        vertical_layout1.addLayout(horizontal_layout2)
        vertical_layout1.addLayout(horizontal_layout3)
        vertical_layout1.addLayout(horizontal_layout4)
        
        # This is the method for button_1
        def when_button1_is_clicked():
            text_box1.insertPlainText("1")
            
        # This is the method for button_2
        def when_button2_is_clicked():
            text_box1.insertPlainText("2")
        
        # This is the method for button_3
        def when_button3_is_clicked():
            text_box1.insertPlainText("3")
        
        # This is the method for button_del
        def when_button_del_is_clicked():
            current_text = text_box1.toPlainText()
            if current_text:
                current_text_turn_to_list = list(current_text)
                current_text_turn_to_list.pop()
                list_to_text = "".join(current_text_turn_to_list)
                text_box1.setText(list_to_text)
            else:
                text_box1.setText(text_box1.toPlainText())
            
        # This is the method for button_ac
        def when_button_ac_is_clicked():
            text_box1.clear()
            
        # This is the method for button_4
        def when_button4_is_clicked():
            text_box1.insertPlainText("4")
        
        # This is the method for button_5
        def when_button5_is_clicked():
            text_box1.insertPlainText("5")
        
        # This is the method for button_6
        def when_button6_is_clicked():
            text_box1.insertPlainText("6")
        
        # This is the method for button_multiply
        def when_button_multiply_is_clicked():
            text_box1.insertPlainText("*")
        
        # This is the method for button_divide
        def when_button_divide_is_clicked():
            text_box1.insertPlainText("/")
        
        # This is the method for button_7
        def when_button7_is_clicked():
            text_box1.insertPlainText("7")
        
        # This is the method for button_8
        def when_button8_is_clicked():
            text_box1.insertPlainText("8")
        
        # This is the method for button_9
        def when_button9_is_clicked():
            text_box1.insertPlainText("9")
        
        # This is the method for button_add
        def when_button_add_is_clicked():
            text_box1.insertPlainText("+")
            
        # This is the method for button_minus
        def when_button_minus_is_clicked():
            text_box1.insertPlainText("-")
            
        # This is the method for button_0
        def when_button0_is_clicked():
            text_box1.insertPlainText("0")
        
        # This is the method for button_dot
        def when_button_dot_is_clicked():
            text_box1.insertPlainText(".")
        
        # This is the method for button_answer
        def when_button_answer_is_clicked():
            try:
                current_text = text_box1.toPlainText()
                answer = eval(current_text)
                answer_to_string = str(answer)
                text_box1.setText(answer_to_string)
            except SyntaxError:
                text_box1.setText("Syntax error")
                text_box1.moveCursor(QTextCursor.End)
            
app = QApplication([])
window = Window()
window.show()
app.exec_()