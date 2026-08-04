from PySide6.QtCore import QObject, Signal, Slot

from core.ai import GustavAI


class AIWorker(QObject):
    finished = Signal(str)
    error = Signal(str)

    def __init__(self):
        super().__init__()
        self.ai = GustavAI()

    @Slot(str)
    def ask(self, text):
        try:
            answer = self.ai.ask(text)
            self.finished.emit(answer)
        except Exception as e:
            self.error.emit(str(e))