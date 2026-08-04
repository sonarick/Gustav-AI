
from PySide6.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QListWidget,QLineEdit,QPushButton,QLabel
from ui.chat import ChatArea

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🤖 Gustav 2.0")
        self.resize(1200,700)

        self.setStyleSheet('''
        QWidget{background:#202123;color:white;font-size:13px;}
        QListWidget,QLineEdit{background:#2B2D31;border:1px solid #444;border-radius:8px;}
        QPushButton{background:#10A37F;border:none;border-radius:8px;padding:8px;}
        QFrame#bubble{background:#2B2D31;border-radius:10px;padding:8px;margin:6px;}
        ''')

        main=QHBoxLayout(self)
        side=QListWidget()
        side.addItems(["💬 Новый чат","💻 Работа","🎮 Игры","📚 Учёба"])
        side.setMaximumWidth(220)

        right=QVBoxLayout()
        title=QLabel("🤖 Gustav 2.0")
        self.chat=ChatArea()
        self.chat.add_message("🤖 Гюстав","Добро пожаловать в Gustav 2.0!")
        self.input=QLineEdit()
        self.input.setPlaceholderText("Напишите сообщение...")
        btn=QPushButton("➤")
        right.addWidget(title)
        right.addWidget(self.chat)
        bottom=QHBoxLayout()
        bottom.addWidget(self.input)
        bottom.addWidget(btn)
        right.addLayout(bottom)

        main.addWidget(side)
        main.addLayout(right)
