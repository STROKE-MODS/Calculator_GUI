import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QGridLayout,QPushButton,QLabel,QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initgui()
        pass
    def initgui(self):
        self.first_number = []  #To check if there is current number
        self.buttonclicked = None #to check which button is clicked
        self.current_operation = None #To verify if there is current operation
        self.numbers_in_list=[] #For the numbers
        self.second_number = []
        self.operator = None
        self.operators = ['+','-','X','/','.','=','AC'] #Assigning the operators
        self.rows = 1
        self.column = 0
        self.rows_operators =1
        self.button_click = [] #To store the buttons cliced
        self.answers = "This will show the answers...."
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.button= {}
    
        box  = QWidget()
        self.setCentralWidget(box)
        
        grid  = QGridLayout()
        box.setLayout(grid)
        for i in range(-1,17):
            if(i<10):
                if(i==-1):
                    self.answerbutton = QLabel("Solution.....")
                    self.answerbutton.setAlignment(Qt.AlignCenter)
                    grid.addWidget(self.answerbutton,0,0,1,4)
                    self.answerbutton.setStyleSheet("height : 150px;" #styling the answer button
                                               "width : 150px;"
                                               "color : black;"
                                               "background-color :#c2b5b4;"
                                               "border-radius : 50px;"
                                               "font-size : 40px;")
                else:
                        button = QPushButton(f"{i}",self)
                        self.button[i] = button
                        grid.addWidget(button,self.rows,self.column)
                        self.button[i].clicked.connect(lambda checked ,num=i:self.clicking(num))
                        self.column+=1
                        if(self.column>=3):
                            self.rows+=1
                            self.column = 0
            elif(i>=10):
                button  = QPushButton(f"{self.operators[i%10]}",self)
                self.button[i] = button
                grid.addWidget(button,self.rows_operators,3)
                self.button[i].clicked.connect(lambda checked ,num=i:self.clicking(num))
                self.rows_operators +=1
                if(self.button[i].clicked in self.operators): 
                    self.button[i].clicked.connect(lambda checked,num = self.operators[i].text():self.clicking(num))
        for i in range(17):
            self.button[i].setStyleSheet("background-color : #c2b5b4;"
                                         "height : 50px;"
                                         "width : 50px;"
                                         "color : black;")
    def keyPressEvent(self,event):
        key  = event.key()
        if (key<=58 and key>=48):
            self.clicking(key-48)
        elif(key==43):
            self.clicking(10)
        
        elif(key==46):
            self.clicking(14)
        
        elif(key==45):
            self.clicking(11)
        
        elif(key==42):
            self.clicking(12)
        
        elif(key==47):
            self.clicking(13)
        
        elif(key==16777220):
            self.clicking(15)
        
        elif(key==16777219 or 16777216):
            self.clicking(16)
        
            
    def clicking(self,num):
            self.buttonclicked = self.button[num].text()
            if(self.buttonclicked in '0123456789.'):
                if(self.operator == None):
                    if self.buttonclicked == '.':
                        if not self.first_number:
                            self.first_number.append("0")
                            self.first_number.append(".")
                            self.answerbutton.setText("".join(self.first_number))
                        else:
                            self.first_number.append(".")
                            self.answerbutton.setText("".join(self.first_number))
                    else : 
                            self.first_number.append(str(self.buttonclicked))
                            self.answerbutton.setText("".join(self.first_number))
                elif(self.operator is not None):
                    if  self.buttonclicked == '.' :
                        if  not self.second_number:
                            self.second_number.append("0")
                            self.second_number.append(".")
                            self.answerbutton.setText("".join(self.second_number))
                        else: 
                            self.second_number.append(str(self.buttonclicked))
                            self.answerbutton.setText("".join(self.second_number))
                                                      
                    else:
                        self.second_number.append(str(self.buttonclicked))
                        self.answerbutton.setText("".join(self.second_number))

            elif(self.buttonclicked in self.operators and self.buttonclicked != '=' and self.buttonclicked != 'AC'):
                self.operator = self.buttonclicked
                self.answerbutton.setText(self.operator)
            elif(self.buttonclicked=='='):
                if(self.operator is None or self.first_number is None or self.second_number is None):
                     self.answerbutton.setText("Insufficient values....")
                     return
                else:
                    if(self.operator == '+'):
                        self.answer =  float("".join(self.first_number)) + float("".join(self.second_number))
                        self.answerbutton.setText(str(self.answer))
                        self.first_number.clear()
                        self.second_number.clear()
                        self.operator = None
                        self.answer =0
                        
                    elif(self.operator == '-'):
                        self.answer = float("".join(self.first_number)) - float("".join(self.second_number))
                        self.answerbutton.setText(str(self.answer))
                        self.first_number.clear()
                        self.second_number.clear()
                        self.operator = None
                        self.answer =0
                        
                    elif(self.operator == 'X'):
                        self.answer = float("".join(self.first_number)) * float("".join(self.second_number))
                        self.answerbutton.setText(str(self.answer))
                        self.first_number.clear()
                        self.second_number.clear()
                        self.operator = None
                        self.answer =0
                        
                    elif(self.operator == '/'):
                        if(self.second_number == '0'):
                            self.answerbutton.setText("Divison cant be possible with zero.")
                        else:
                            self.answer = float("".join(self.first_number)) / float("".join(self.second_number))
                            self.answerbutton.setText(str(self.answer))
                            self.first_number.clear()
                            self.second_number.clear()
                            self.operator = None
                            self.answer = 0
            elif(self.buttonclicked == 'AC'):
                self.answerbutton.setText("0")
                self.first_number.clear()
                self.second_number.clear()
                self.operator = None
                self.answer =0
                return
def main():
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


    
    
    