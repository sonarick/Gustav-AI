
import sys
from PySide6.QtWidgets import QApplication
from ui.window import MainWindow

app=QApplication(sys.argv)
w=MainWindow()
w.show()
sys.exit(app.exec())
