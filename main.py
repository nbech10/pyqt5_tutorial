from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox


def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()


app = QApplication([])
app.setStyleSheet("QPushButton { margin: 10ex; }")

window = QWidget()

layout = QVBoxLayout()

topButton = QPushButton('Top')
topButton.clicked.connect(on_button_clicked)

bottomButton = QPushButton('Bottom')

layout.addWidget(topButton)
layout.addWidget(bottomButton)

window.setLayout(layout)
window.show()

app.exec_()

