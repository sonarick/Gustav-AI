from PySide6.QtCore import QThread, Signal
from core.ai import GustavAI


class AIWorker(QThread):
    finished = Signal(str)

    def __init__(self, ai: GustavAI, text: str):
        super().__init__()
        self.ai = ai
        self.text = text

    def run(self):
        try:
            answer = self.ai.ask(self.text)
        except Exception as e:
            answer = f"Ошибка:\n{e}"

        self.finished.emit(answer)