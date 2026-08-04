from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QScrollArea,
)

from ui.message import MessageBubble


class ChatArea(QScrollArea):
    def __init__(self):
        super().__init__()

        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.container = QWidget()
        self.layout = QVBoxLayout(self.container)

        self.layout.setSpacing(12)
        self.layout.setContentsMargins(15, 15, 15, 15)
        self.layout.addStretch()

        self.setWidget(self.container)

    def add_message(self, sender: str, text: str):
        bubble = MessageBubble(sender, text)

        self.layout.insertWidget(
            self.layout.count() - 1,
            bubble
        )

        self.verticalScrollBar().setValue(
            self.verticalScrollBar().maximum()
        )

    def clear_chat(self):
        while self.layout.count() > 1:
            item = self.layout.takeAt(0)

            if item.widget():
                item.widget().deleteLater()