from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QLineEdit,
    QPushButton,
    QLabel,
)

from ui.chat import ChatArea
from core.ai import GustavAI
from core.worker import AIWorker


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ai = GustavAI()
        self.resize(1200, 700)

        self.setStyleSheet("""
        QWidget{
            background:#202123;
            color:white;
            font-size:13px;
        }

        QListWidget,QLineEdit{
            background:#2B2D31;
            border:1px solid #444;
            border-radius:8px;
        }

        QPushButton{
            background:#10A37F;
            border:none;
            border-radius:8px;
            padding:8px;
        }

        QPushButton:hover{
            background:#18c497;
        }
        """)

        # ===== Основной Layout =====

        main = QHBoxLayout(self)

        # ===== Меню =====

        side = QListWidget()
        side.addItems([
            "💬 Новый чат",
            "💻 Работа",
            "🎮 Игры",
            "📚 Учёба"
        ])
        side.setMaximumWidth(220)

        # ===== Правая часть =====

        right = QVBoxLayout()

        title = QLabel("🤖 Gustav 2.0")

        self.chat = ChatArea()
        self.chat.add_message("🤖 Гюстав", "Добро пожаловать!")

        self.input = QLineEdit()
        self.input.setPlaceholderText("Напишите сообщение...")

        self.button = QPushButton("➤")

        bottom = QHBoxLayout()
        bottom.addWidget(self.input)
        bottom.addWidget(self.button)

        right.addWidget(title)
        right.addWidget(self.chat)
        right.addLayout(bottom)

        main.addWidget(side)
        main.addLayout(right)

        # ===== Сигналы =====

        self.button.clicked.connect(self.send_message)
        self.input.returnPressed.connect(self.send_message)

    # ===================================

    def send_message(self):

        text = self.input.text().strip()

        if not text:
            return

        self.chat.add_message("🙂 Вы", text)

        self.input.clear()

        self.button.setEnabled(False)

        print(AIWorker)

        self.worker = AIWorker(self.ai, text)
        self.worker.finished.connect(self.ai_answer)
        self.worker.start()

    # ===================================

    def ai_answer(self, text):

        self.chat.add_message("🤖 Гюстав", text)

        self.button.setEnabled(True)