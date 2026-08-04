from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)


class MessageBubble(QFrame):
    def __init__(self, sender: str, text: str):
        super().__init__()

        is_user = sender.lower().startswith("👤")

        self.setStyleSheet("""
            QLabel{
                color:white;
                font-size:14px;
            }
        """)

        outer = QHBoxLayout(self)

        bubble = QFrame()
        bubble_layout = QVBoxLayout(bubble)

        title = QLabel(sender)
        title.setStyleSheet("""
            font-weight:bold;
            color:#10A37F;
        """)

        body = QLabel(text)
        body.setWordWrap(True)
        body.setTextInteractionFlags(Qt.TextSelectableByMouse)

        bubble_layout.addWidget(title)
        bubble_layout.addWidget(body)

        bubble.setStyleSheet(f"""
            QFrame {{
                background-color: {"#0E639C" if is_user else "#2B2D31"};
                border-radius:12px;
                padding:10px;
            }}
        """)

        if is_user:
            outer.addStretch()
            outer.addWidget(bubble)
        else:
            outer.addWidget(bubble)
            outer.addStretch()