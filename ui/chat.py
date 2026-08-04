from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
)
from PySide6.QtCore import Qt

from ui.message import MessageBubble


class ChatArea(QListWidget):
    def __init__(self):
        super().__init__()

        self.setSpacing(12)
        self.setWordWrap(True)

        self.setSelectionMode(QListWidget.NoSelection)
        self.setFocusPolicy(Qt.NoFocus)

        self.setVerticalScrollMode(QListWidget.ScrollPerPixel)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setStyleSheet("""
            QListWidget{
                border:none;
                background:#202123;
                padding:15px;
            }
        """)

    def add_message(self, sender: str, text: str):
        bubble = MessageBubble(sender, text)

        item = QListWidgetItem()

        item.setSizeHint(bubble.sizeHint())

        self.addItem(item)
        self.setItemWidget(item, bubble)

        self.scrollToBottom()

    def clear_chat(self):
        self.clear()