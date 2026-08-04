from ollama import chat


class GustavAI:
    def __init__(self, model="qwen2.5:7b"):
        self.model = model

        self.messages = [
            {
                "role": "system",
                "content": (
                    "Ты — Гюстав, персональный ИИ-помощник Даниила.\n"
                    "Всегда отвечай только на русском языке.\n"
                    "Будь дружелюбным, понятным и полезным.\n"
                    "Не переходи на другие языки без просьбы пользователя."
                ),
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
        )

        answer = response.message.content

        self.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        return answer