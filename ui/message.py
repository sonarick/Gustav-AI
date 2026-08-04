from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy,
)


class MessageBubble(QWidget):
    def __init__(self, sender: str, text: str):
        super().__init__()

        is_user = sender.startswith("🙂")

        root = QHBoxLayout(self)
        root.setContentsMargins(5, 5, 5, 5)

        bubble = QFrame()
        bubble.setMaximumWidth(700)
        bubble.setSizePolicy(
            QSizePolicy.Maximum,
            QSizePolicy.Minimum
        )

        bubble.setStyleSheet(f"""
            QFrame {{
                background-color: {"#0E639C" if is_user else "#2B2D31"};
                border-radius:14px;
            }}
        """)

        layout = QVBoxLayout(bubble)
        layout.setContentsMargins(15, 12, 15, 12)
        layout.setSpacing(8)

        title = QLabel(sender)
        title.setStyleSheet("""
            color:#10A37F;
            font-size:12px;
            font-weight:bold;
        """)

        body = QLabel(text)
        body.setWordWrap(True)
        body.setTextInteractionFlags(Qt.TextSelectableByMouse)
        body.setStyleSheet("""
            color:white;
            font-size:14px;
        """)

        layout.addWidget(title)
        layout.addWidget(body)

        if is_user:
            root.addStretch()
            root.addWidget(bubble)
        else:
            root.addWidget(bubble)
            root.addStretch()