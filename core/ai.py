import json

from ollama import chat

from core.paths import CONFIG


class GustavAI:
    def __init__(self):

        with open(CONFIG, "r", encoding="utf-8-sig") as f:
            config = json.load(f)

        self.model = config["model"]
        self.temperature = config["temperature"]
        self.language = config["language"]

        ...

        self.messages = [
            {
                "role": "system",
                "content": f"""
Ты — Гюстав, персональный ИИ-помощник Даниила.

Правила:

- Всегда отвечай только на русском языке.
- Никогда не используй китайский язык.
- Никогда не используй английский язык без прямой просьбы пользователя.
- Если случайно начал отвечать на другом языке — сразу перепиши ответ полностью на русском.
- Не показывай свои внутренние рассуждения.
- Не объясняй ход своих мыслей.
- Сразу давай готовый ответ.
- Будь дружелюбным, полезным и кратким.
"""
            }
        ]

    def ask(self, text: str) -> str:
        self.messages.append(
            {
                "role": "user",
                "content": text,
            }
        )

        response = chat(
            model=self.model,
            messages=self.messages,
            think=False,
            options={
                "temperature": self.temperature,
            },
        )

        answer = response.message.content

        self.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        return answer