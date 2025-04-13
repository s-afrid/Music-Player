import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# Main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Music Player")
        self.setGeometry(300,700,500,500)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
