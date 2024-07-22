import os
import openai


class Jarvis:
    def __init__(self):
        openai.organization = "org-o55Oob9j6W8HPwMrY4YDFAPT"
        openai.api_key = os.getenv("OPEN_AI_API_KEY")
        self.training_model = os.getenv('TRAINING_MODEL')

    def ask(self, question):
        messages = [
            {"role": "system", "content": "You are Jarvis, Joseph's assistant. Answer questions about Joseph based on the following information:" + self.training_model},
            {"role": "user", "content": question}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.2,
            top_p=0.5
        )
        return response.choices[0].message['content'].strip()