from PySide6.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QListWidget,QLineEdit,QPushButton,QLabel
from ui.chat import ChatArea
from core.ai import GustavAI
from core.worker import AIWorker
from memory.chat_manager import ChatManager

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ai=GustavAI()
        self.chat_manager=ChatManager()
        self.chat_manager.new_chat()
        self.setWindowTitle('🤖 Gustav 2.0')
        self.resize(1200,700)
        main=QHBoxLayout(self)
        self.side=QListWidget()
        self.side.addItems(['💬 Новый чат','💻 Работа','🎮 Игры','📚 Учёба'])
        self.side.setMaximumWidth(220)
        right=QVBoxLayout()
        title=QLabel('🤖 Gustav 2.0')
        self.chat=ChatArea()
        self.chat.add_message('🤖 Гюстав','Добро пожаловать!')
        self.input=QLineEdit()
        self.button=QPushButton('➤')
        bottom=QHBoxLayout()
        bottom.addWidget(self.input)
        bottom.addWidget(self.button)
        right.addWidget(title)
        right.addWidget(self.chat)
        right.addLayout(bottom)
        main.addWidget(self.side)
        main.addLayout(right)
        self.button.clicked.connect(self.send_message)
        self.input.returnPressed.connect(self.send_message)

    def send_message(self):
        text=self.input.text().strip()
        if not text:return
        self.chat.add_message('🙂 Вы',text)
        self.chat_manager.save_message('user',text)
        self.input.clear()
        self.button.setEnabled(False)
        self.worker=AIWorker(self.ai,text)
        self.worker.finished.connect(self.ai_answer)
        self.worker.start()

    def ai_answer(self,text):
        self.chat.add_message('🤖 Гюстав',text)
        self.chat_manager.save_message('assistant',text)
        self.button.setEnabled(True)
